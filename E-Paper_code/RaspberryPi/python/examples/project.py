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
import traceback
from io import BytesIO

logging.basicConfig(level=logging.DEBUG)

img_src1 = 'https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/11214290_979728228728313_6464220580933024886_n.jpg?_nc_cat=105&_nc_eui2=AeExGUqRxcZU4upTetprXJyv_Op4AKU9Oi0KerZLpKGeJ1eNelyKE8Va-EMuyfLeMAnEZ1jPtl2Q3kfCGkqxbtXdZlUhJaJEKiF-E1SavOs0xQ&_nc_ohc=k0ZZmaA6kdEAQkCfmXYSTOBPC0T1JsPb1y8boEcDjKwqiECZRTPWLAivA&_nc_ht=scontent-tpe1-1.xx&oh=f1bcf4ad88a887d8ffa735ea151bdeec&oe=5E3F278B'
img_src2 = 'https://i.ibb.co/Jmqs8BQ/2.png'

response1 = req.get(img_src1)
response2 = req.get(img_src2)

image_head = Image.open(BytesIO(response1.content))
image_QRcode = Image.open(BytesIO(response2.content))

x_head = 319
y_head = 283
x_QRcode = 150
y_QRcode = 150

image_head = image_head.resize((x_head,y_head), Image.ANTIALIAS)
image_QRcode = image_QRcode.resize((x_QRcode,y_QRcode), Image.ANTIALIAS)

image_head = image_head.resize((x_head,y_head),Image.ANTIALIAS)
image_QRcode = image_QRcode.resize((x_QRcode,y_QRcode),Image.ANTIALIAS)

strftime("%Y-%m-%d", gmtime())

try:
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
	newimage = Image.open(os.path.join(picdir, '100x100.bmp'))
	HBlackimage.paste(image_head, (0,0))

	#data
	print("date")
	font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
	drawblack.text((70, 323), "strftime", font=font18, fill=0)

	#state
	print("state")
	drawblack.text((339,20), 'state', font=font18, fill=0)
	HBlackimage.paste(newimage, (399,70))

	#QRCODE
	print("QRCODE")
	drawblack.text((339,263), u'聯絡老師', font=font18, fill=0)
	HBlackimage.paste(image_QRcode, (450,250))

	epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))

	time.sleep(2)
	epd.sleep()

        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5bc.epdconfig.module_exit()
    exit()