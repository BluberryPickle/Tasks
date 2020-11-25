#! /usr/bin/env python3

string = input("Enter the string you want to encode/decode")
key = int(input('Enter your key'))
print("[0] Encoding")
print("[1] Decoding")
option = int(input())

if option == 0 :
	encrypted = ''
	for i in string :
		if i.isupper():
			cipher = ord(i) + key
			while cipher > 90 :
				cipher = (cipher - 90) + 64
			encrypted = encrypted + chr(cipher)
		elif i.islower():
			cipher = (ord(i)+key)
			while cipher > 122:
				cipher = (cipher -122) + 96
			encrypted = encrypted + chr(cipher)
		elif 47 < ord(i) < 58 :
			cipher = ord(i) + key
			while cipher > 57:
				cipher = (cipher-57) + 47
			encrypted = encrypted + chr(cipher)
		else : encrypted = encrypted + i

	print('Encrypted : ',encrypted)

elif option == 1 :
	decrypted = ''
	for i in string:
		if i.isupper() :
			decode = ord(i) - key
			while decode < 65 :
				decode = 91-(65-decode)
			decrypted = decrypted + chr(decode)
		elif i.islower():
			decode = ord(i)-key
			while decode < 97 :
				decode = 123 - (97-decode)

			decrypted = decrypted + chr(decode)

		elif 47 < ord(i) < 58:
			decode = ord(i)-key
			while decode < 48 :
				decode = 58- (48-decode)
			decrypted = decrypted + chr(decode)

		else : decrypted = decrypted + i
	print('Decoded Text : ',decrypted)

else : print('Please make sure you entered the correct ') 


