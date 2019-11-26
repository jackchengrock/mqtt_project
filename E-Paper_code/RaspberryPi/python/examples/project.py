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
import time
from PIL import Image,ImageDraw,ImageFont
import traceback
from io import BytesIO

logging.basicConfig(level=logging.DEBUG)

img_src1 = 'https://ibb.co/2MXW2GQ'
img_src2 = 'https://ibb.co/DMNFMKY'

response1 = req.get(img_src1)
response2 = req.get(img_src2)

image1 = Image.open(BytesIO(response1.content))
image2 = Image.open(BytesIO(response2.content))

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
	HBlackimage.paste(newimage, (0,0))

	#data
	print("date")
	font18 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 18)
	drawblack.text((70, 323), 'date', font=font18, fill=0)

	#state
	print("state")
	drawblack.text((339,20), 'state', font=font18, fill=0)
	HBlackimage.paste(image1, (399,70))

	#QRCODE
	print("QRCODE")
	drawblack.text((339,263), u'聯絡老師', font=font18, fill=0)
	HBlackimage.paste(image2, (450,250))

	epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))

	time.sleep(2)
	epd.sleep()

        
except IOError as e:
    logging.info(e)
    
except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    epd7in5bc.epdconfig.module_exit()
    exit()