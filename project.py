import epd7in5b
import time
from PIL import Image, ImageDraw, ImageFont
import traceback

try:
	epd = epd7in5b.EPD()
	epd.init()
	print("Clear")
	epd.Clear(0xFF)

	#Drawing on the Horizontal image
	HBlackimage = image.new('1', (epd7in5b.EPD.WIDTH, epd7in5b.EPD.HEIGHT), 255)
	HRedimage = image.new('1', (epd7in5b.EPD.WIDTH, epd7in5b.EPD.HEIGHT), 255)

	#horizontal
	print("Drawing")
	drawblack = ImageDraw.Draw(HBlackimage)
	drawred = ImageDraw.Draw(HRedimage)
	font24 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy.microhei.ttc', 24)

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
	newimage = Image.open("pic.bmp")
	HBlackimage.paste(newimage, (0,0))

	#data
	print("date")
	font18 = ImageFont.truetype('/usr/share/fonts/truetype/wqy/wqy.microhei.ttc', 18)
	drawblack.text((70, 323), 'date', font=font18, fill=0)

	#state
	print("state")
	drawblack.text((70,323), u'狀態', font=font18, fill=0)
	HBlackimage.paste(newimage, (399,70))

	#QRCODE
	print("QRCODE")
	drawblack.text((70,323), u'聯絡老師', font=font18, fill=0)
	HBlackimage.paste(newimage, (450,250))

	epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRedimage))

	time.sleep(2)
	epd.sleep()

except:
	print('traceback.format_exc()\n%s', traceback.format_exc())
	exit()
