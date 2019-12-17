import paho.mqtt.client as mqtt

def on_connect(clien, userdata, flags, rc):
	print("connected with" + str(rc))

	client.subscribe("CoreElectronics/test")
	client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
	print(msg.topic + "" str(msg.payload))

	if msg.payload == "Hello":
		print("Received msg #1")

	if msg.payload == "World!":
		print("Receive msg #2")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connected("192.168.66.19", 1883, 60)

client.loop.forever()