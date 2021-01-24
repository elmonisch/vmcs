import paho.mqtt.client as mqtt
import psycopg2 as pg
import json

from psycopg2 import Error

def filter_message(message)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+ str(rc))
    client.subscribe("test/+")

def on_message(client, userdata, msg):
    message = msg.payload.decode("utf-8")
    print(f"Message : {message}")
    json.dumps(message)
    
    # post = {"topic": f"{msg.topic}", "value": f"{message}"}
    # post = json.dumps(post)

    # cur.execute(f"insert into test_v1_filter (lcs_data) values ('{post}')")
    # con.commit()

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