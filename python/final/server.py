import paho.mqtt.client as mqtt
from test1 import abc

def on_connect(clien, userdata, flags, rc):
	print("connected with" + str(rc))

	client.subscribe("CoreElectronics/test")
	client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
	print(msg.topic + "" + str(msg.payload))
	global a, b
	if msg.payload == "Hello":
		print("Received msg #1")
		a = "msg.topic + "" + str(msg.payload)"
		abc()
	if msg.payload == "World!":
		print("Receive msg #2")
		b = "msg.topic + "" + str(msg.payload)"
		abc()
		
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.66.19", 1883, 60)

client.loop_forever()