#!/usr/bin/env python

import paho.mqtt.client as mqtt
import datetime
import threading

def on_connect(clien, userdata, flags, rc):
	print("connected with" + str(rc))

	client.subscribe("CoreElectronics/test")
	client.subscribe("CoreElectronics/topic")

def on_message(client, userdata, msg):
	print(msg.topic + "" + str(msg.payload))
	global a, b
	
	if msg.payload == "Hello":
		print(123)
	if msg.payload == "World!":
		print(123)

	
if __name__ == '__main__':
	client = mqtt.Client()
	client.on_connect = on_connect
	client.on_message = on_message

	client.connect("192.168.66.19", 1883, 60)
	client.loop_forever()

	while True:
		now_time = datetime.datetime.now()
		next_time = now_time + datetime.timedelta(days=+1)
        next_year = next_time.date().year
        next_month = next_time.date().month
        next_day = next_time.date().day
        next_time = datetime.datetime.strptime(str(next_year)+"-"+str(next_month)+"-"+str(next_day)+" 00:00:00", "%Y-%m-%d %H:%M:%S")
		timer_start_time = (next_time - now_time).total_seconds()
		timer = threading.Timer(timer_start_time, func)
        timer.start()