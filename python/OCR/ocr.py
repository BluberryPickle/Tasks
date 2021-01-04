#! /usr/bin/env python3

#import stuff
from PIL import Image
import os,argparse
from pytesseract import image_to_string

#Function to extract operation

def operation(text,index):
	li = list(text[index])
	if li[1]=='+':
		print('The sum is : ',int(li[0])+int(li[2]))
	elif li[1] == '-':
		print("The difference is : ",int(li[0])-int(li[2]))
	elif li[1] == 'x' or li[1] == 'X':
		print("The product is : ",int(li[0])*int(li[2]))
	else : print("Divison : ",int(li[0])/int(li[2]))

	


#extract text from image
text = (image_to_string(Image.open("simple.png"))).rstrip()
text = text.split()

#loops through text to find the line with math operation.
for i in text:
	for j in i:
		if j.isnumeric():
			operation(text,text.index(i))
			break
	print('')

