#!/usr/bin/env python

import paho.mqtt.client as mqtt
from test1 import abc
import datetime

def on_connect(clien, userdata, flags, rc):
	print("connected with" + str(rc))

	client.subscribe("CoreElectronics/test")
	client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
	print(msg.topic + "" + str(msg.payload))
	global a, b
	
	if msg.payload == "Hello":
		
	if msg.payload == "World!":
		

	
if __name__ == '__main__':
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message

	client.connect("192.168.66.19", 1883, 60)
	client.loop_forever()

	while True:
		now_time = datetime.datetime.now()
		if now_time.second == 20:
			print(now_time)