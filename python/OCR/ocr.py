#! /usr/bin/env python3

from PIL import Image
import os,argparse
from pytesseract import image_to_string

#img = Image.open("captcha.png")
#rint(img.format, img.size, img.mode)

text = image_to_string(Image.open("captcha.png"))
print(text)