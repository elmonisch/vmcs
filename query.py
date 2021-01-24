import paho.mqtt.client as mqtt
import psycopg2 as pg
import json

from psycopg2 import Error

def connecting():
    try:

        con = pg.connect(host="localhost", database="postgres", user="postgres", password="mysecretpassword")
        cur = con.cursor()
    except (Exception, Error) as error:
        print("Error while connecting to PostgreSQL", error)
    
    return con, cur

con, cur = connecting()

cur.execute("select * from test_v1_filter;")
res = cur.fetchall()
print(res)

a, b = res[-1]
print(b['value'])