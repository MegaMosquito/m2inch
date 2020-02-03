#!/usr/bin/python
# -*- coding:utf-8 -*-

# This is the Waveshare example program, with small changes to picdir, libdir.

import time
import sys
import os

#picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
#libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
picdir = '/2inch_LCD_Module_code/RaspberryPi&JetsonNano/python/pic'
libdir = '/2inch_LCD_Module_code/RaspberryPi&JetsonNano/python/lib'

if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
import time
from waveshare_2inch_LCD import ST7789
from PIL import Image,ImageDraw,ImageFont

logging.basicConfig(level=logging.INFO)


try:
    print ("2inch LCD Module")
    disp = ST7789.ST7789()
    # Initialize library.
    disp.Init()

    # Clear display.
    disp.clear()

    # image = Image.new('RGB', (disp.width,disp.height), (255,255,255)) 
    image = Image.new('RGB', (disp.height,disp.width), (255,255,255)) 

    draw = ImageDraw.Draw(image)

    font30 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 30)
    font15 = ImageFont.truetype(os.path.join(picdir, 'Font.ttc'), 15)
    print ("***draw line")
    draw.line([(40,20),(200,20)], fill = "BLUE",width = 5)
    draw.line([(40,20),(40,200)], fill = "BLUE",width = 5)
    draw.line([(40,200),(200,200)], fill = "BLUE",width = 5)
    draw.line([(200,20),(200,200)], fill = "BLUE",width = 5)
    print ("***draw rectangle")
    draw.rectangle([(50,30),(190,70)],fill = "BLUE")
    
    print ("***draw text")
    draw.text((60,30), u'微雪电子', font = font30, fill = "WHITE")
    draw.text((50, 75), 'Waveshare Electronic ', font = font15, fill = "BLUE")
    draw.text((75, 110), '2.0inch LCD ', font = font15, fill = "BLUE")
    draw.text((72, 140), 'Test Program ', font = font15, fill = "BLUE")

    image=image.rotate(180) 
    disp.ShowImage(image)
    time.sleep(3)

    # read bmp file 
    bmp = Image.open(os.path.join(picdir, 'LCD_2inch.bmp'))	
    image.paste(bmp, (0,0))  
    image=image.rotate(180)
    disp.ShowImage(image)

except KeyboardInterrupt:    
    logging.info("ctrl + c:")
    exit()


