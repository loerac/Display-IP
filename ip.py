#!/usr/bin/python
# Imports

# System
import os
import sys
from time import sleep

# Image/Papirus
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from papirus import Papirus

# Socket for IP Address
import socket

# Screen size
SIZE=27

# Fonts
hatdir = '/proc/device-tree/hat'
ipFont = '/usr/share/fonts/truetype/freefont/FreeMonoOblique.ttf'

if __name__=="__main__":
    # Check EPD_SIZE is defined
    EPD_SIZE=0.0
    if os.path.exists('/etc/default/epd-fuse'):
        exec(open('/etc/default/epd-fuse').read())
    if EPD_SIZE==0.0:
        print("Please select your screen size by running 'papirus-config'.")

    papirus=Papirus(rotation=180)
    papirus.clear()

    # Setting the screen color
    BLACK=0
    WHITE=1

    # Set the background to white
    image=Image.new('1',papirus.size,WHITE)
    draw=ImageDraw.Draw(image)

    # Grabbing the width and height of the screen
    width,height=image.size

    # Setting the size/font for the IP Address
    ipSize=int((width-4)/(8*0.65))
    ipFont=ImageFont.truetype(ipFont,ipSize)

    # Grabbing the IP Address
    # This is stating that you already have internet access
    s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8",80))
    ipAddr= s.getsockname()[0]
    s.close()

    # Drawing a white canvas around the screen
    draw.rectangle((0,0,papirus.size[0],papirus.size[1]),fill=WHITE,outline=WHITE)

    # Display the IP Address
    inc=5
    while 1:
        for i in range(0,len(ipAddr)):
            image=Image.new('1',papirus.size,WHITE)
            draw=ImageDraw.Draw(image)
            draw.text(((5-inc),30),ipAddr,fill=BLACK,font=ipFont)
            papirus.display(image)
            papirus.partial_update()
            inc+=25
            sleep(0.5)
        inc=5
        papirus.update()
    
