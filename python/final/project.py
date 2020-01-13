#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
import os
import requests as req
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd7in5bc
from time import gmtime, strftime
from PIL import Image,ImageDraw,ImageFont
from io import BytesIO

error = "100x100.bmp"
logging.basicConfig(level=logging.DEBUG)

x_head = 319
y_head = 283
x_QRcode = 130
y_QRcode = 130
x_state = 100
y_state = 100

def test(head, state, qrcode, todaytime):
	print(head.decode('utf-8','strict'))
	print(state.decode('utf-8','strict'))
	print(error)
	print(qrcode.decode('utf-8','strict'))
	print(todaytime)


def drawpic(head, state, qrcode, todaytime):
	try:
		try:
			img_src1 = head.decode('utf-8','strict')
			response1 = req.get(img_src1)
			image_head = Image.open(BytesIO(response1.content))
		except:
			image_head = Image.open(os.path.join(picdir, error))

		try:
			img_src2 = qrcode.decode('utf-8','strict')
			response2 = req.get(img_src2)
			image_QRcode = Image.open(BytesIO(response2.content))
		except:
			image_QRcode = Image.open(os.path.join(picdir, error))

		try:
			state = state.decode('utf-8','strict')
			stateimage = Image.open(os.path.join(picdir, state))
		except:
			stateimage = Image.open(os.path.join(picdir, error))

		image_QRcode = image_QRcode.resize((x_QRcode,y_QRcode), Image.ANTIALIAS)
		stateimage = stateimage.resize((x_state,y_state), Image.ANTIALIAS)
		image_head = image_head.resize((x_head,y_head), Image.ANTIALIAS)
		epd = epd7in5bc.EPD()
		epd.init()
		print("Clear")
		epd.Clear()
		#Drawing on the Horizontal image
		HBlackimage = Image.new('1', (epd.width, epd.height), 255)
		HRedimage = Image.new('1', (epd.width, epd.height), 255)
		#horizontal
		print("Drawing")
		drawblack = ImageDraw.Draw(HBlackimage)
		drawred = ImageDraw.Draw(HRedimage)
		font24 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 24)
		print("Drawline")
		drawblack.line(((0,0), (0,383)), fill=0, width=5)
		drawblack.line(((0,0), (639,0)), fill=0, width=5)
		drawblack.line(((639,383), (0,383)), fill=0, width=5)
		drawblack.line(((639,0), (639,383)), fill=0, width=5)
		drawblack.line(((319,0), (319,383)), fill=0, width=5)
		drawblack.line(((0,283), (319,283)), fill=0, width=5)
		drawblack.line(((319,233), (639,233)), fill=0, width=5)
		#headpic
		print("head") 
		HBlackimage.paste(image_head, (0,0))
		#data
		print("date")
		font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
		drawblack.text((70, 323), todaytime, font=font18, fill=0)
		#state
		print("state")
		drawblack.text((339,20), 'state', font=font18, fill=0)
		HBlackimage.paste(stateimage, (420,110))
		if state=="1":
			drawblack.text((400,80), u'暫時外出', font=font18, fill=0)
		elif state=="2":
			drawblack.text((400,80), u'休假中', font=font18, fill=0)
		elif state=="3":
			drawblack.text((400,80), u'請留言', font=font18, fill=0)
		elif state=="4":
			drawblack.text((400,80), u'會議中', font=font18, fill=0)
		elif state=="5":
			drawblack.text((400,80), u'敲門請進', font=font18, fill=0)
		else:
			drawblack.text((400,80), state, font=font18, fill=0)
			
		#QRCODE
		print("QRCODE")
		drawblack.text((339,263), u'聯絡老師', font=font18, fill=0)
		HBlackimage.paste(image_QRcode, (450,240))
		epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))
			
	except IOError as e:
		logging.info(e)
		
	except KeyboardInterrupt:    
		logging.info("ctrl + c:")
		epd7in5bc.epdconfig.module_exit()
		exit()