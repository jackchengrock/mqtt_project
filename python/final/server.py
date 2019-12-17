#!/usr/bin/env python

import paho.mqtt.client as mqtt
from test1 import abc
import datetime
from threading import Timer
import time

def timeTask():
	Timer(5, task, ()).start()

def task():
	print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

def on_connect(clien, userdata, flags, rc):
	print("connected with" + str(rc))

	client.subscribe("CoreElectronics/test")
	client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
	print(msg.topic + "" + str(msg.payload))
	global a, b
	now_time = datetime.datetime.now()
	
	if msg.payload == "Hello":
		print("Received msg #1")
		a = msg.topic + "" + str(msg.payload)
		print(a)
		abc(a,a)
	if msg.payload == "World!":
		print("Receive msg #2")
		b = msg.topic + "" + str(msg.payload)
		print(b)

	while True:
		if now_time.date().year == 2019:
			print("123")

	
if __name__ == '__main__':
    timedTask()
    while True:
		client = mqtt.Client()
		client.on_connect = on_connect
		client.on_message = on_message

		client.connect("192.168.66.19", 1883, 60)

		client.loop_forever()