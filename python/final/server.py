#!/usr/bin/env python

import paho.mqtt.client as mqtt
import datetime
import threading
import time
from apscheduler.schedulers.gevent import GeventScheduler
import schedule

def on_connect(clien, userdata, flags, rc):
	print("connected with" + str(rc))

	client.subscribe("CoreElectronics/test")
	client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
	print(msg.topic + "" + str(msg.payload))
	global a, b
	
	if msg.payload == "Hello":
		print("123")
	if msg.payload == "World!":
		print("123")

def changtime():
	print("123")

schedule.every(10).second.do(changtime)

def job():
	while True:
		#print("qwe")
		schedule.run_pending()
		time.sleep(4)

if __name__ == '__main__':
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message
	client.connect("192.168.66.19", 1883, 60)
	t = threading.Thread(target=job)
	t.start()
	client.loop_forever()


	
	
	
	
