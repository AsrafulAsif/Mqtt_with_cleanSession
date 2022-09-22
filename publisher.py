import paho.mqtt.client as paho
import sys

client = paho.Client("asif", clean_session=False)

if client.connect("X.X.X.X", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)
while 1:
    msg = input("Enter something:")
    client.publish("asif", msg, 1)