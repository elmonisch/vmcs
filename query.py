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

cur.execute("select * from vmcs_filter;")
res = cur.fetchall()
# print(res)

_, _, _, b, _ = res[-1]
print(b)
print(b['parameter'])

# c = b['value']
# print(c, type(c))
# print(c['parameter'])