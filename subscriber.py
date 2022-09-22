import paho.mqtt.client as paho

import sys

client = paho.Client("asif1", clean_session=False)

if client.connect("X.X.X.X", 1883, 3660) != 0:
    print("Could not connect")
    sys.exit(-1)


def onMessage(client, userdata, msg):
    print(msg.topic + ": " + msg.payload.decode())


client.subscribe("asif", 1)
client.on_message = onMessage

try:
    print("Press CRTL+C to exit...")
    client.loop_forever()
except:
    print("Disconnect from broker")
