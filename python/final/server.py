#!/usr/bin/env python
import paho.mqtt.client as mqtt
import datetime
import threading
import time
from apscheduler.schedulers.gevent import GeventScheduler
import schedule
from project import drawpic

today = datetime.datetime.now().strftime("%Y/%m/%d")
head = ''
state = ''
qrcode = ''

def on_connect(clien, userdata, flags, rc):
	print("connected with" + str(rc))

	client.subscribe("Project/head")
	client.subscribe("Project/state")
	client.subscribe("Project/qrcode")

def on_message(client, userdata, msg):
	print(msg.topic + "" + str(msg.payload))
	global today, head, state, qrcode

	if msg.topic == "Project/head":
		head = msg.payload
		drawpic(head[1::], state, qrcode, today)
	if msg.topic == "Project/state":
		print(msg.payload)
		state = msg.payload 
		drawpic(head[1::], state, qrcode, today)
	if msg.topic == "Project/qrcode":
		print(msg.payload)
		qrcode = msg.payload
		drawpic(head[1::], state, qrcode, today)

def changtime():
	global today
	today = datetime.datetime.now().strftime("%Y/%m/%d")
	print(today)

schedule.every().day.at("00:00").do(changtime)
schedule.every(60).seconds.do(changtime)

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


	
	
	
	
