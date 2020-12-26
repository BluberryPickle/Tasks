#! /usr/bin/env python3

from PIL import Image
import os,argparse
import pytesseract

#img = Image.open("captcha.png")
#rint(img.format, img.size, img.mode)

text = pytesseract.image_to_string(Image.open("captcha.png"))
print(text)