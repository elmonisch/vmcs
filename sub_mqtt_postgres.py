import paho.mqtt.client as mqtt
import psycopg2 as pg
import json

from psycopg2 import Error

def filter_message(plazaID, laneID, message):
    print(message)
    param = message["parameter"]
    datatype = param["dataType"]

    if datatype != "":
        message = json.dumps(message)
        cur.execute(f"insert into vmcs_filter (plazaid, laneid, lcs_data) values ('{plazaID}', '{laneID}', '{message}')")
        con.commit()
    else:
        message = json.dumps(message)
        cur.execute(f"insert into vmcs (plazaid, laneid, lcs_data) values ('{plazaID}', '{laneID}', '{message}')")
        con.commit()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    client.subscribe("ves/+/+")

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    message = json.loads(message)
    message = dict(message)

    topic = msg.topic
    topic = topic.split("/")

    plazaID, laneID = topic[1], topic[2]

    filter_message(plazaID, laneID, message)

def connecting():
    try:
        con = pg.connect(host="localhost", database="postgres", user="postgres", password="mysecretpassword")
        cur = con.cursor()
        
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    
    return con, cur

con, cur = connecting()

client = mqtt.Client("vmcs", clean_session=False)
client.on_connect = on_connect
client.on_message = on_message
client.connect('127.0.0.1', 1883, keepalive=60)

client.loop_forever()