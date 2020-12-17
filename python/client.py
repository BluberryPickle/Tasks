#! /usr/bin/env python3
#Client side
import socket
import hmac
import hashlib

def hash_gen(text):
	hash = hashlib.sha256(text).hexdigest()
	return hashlib 

def check(HMAC,cipher):
	password= b'password'
	hmac_hash = hmac.new(cipher, password, hashlib.sha1)
	if hmac_hash.digest() == HMAC:
		print('Authentic')

host = 'local host'
port = int(input('port:'))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect(('', port)) 
li = []
msg = s.recv(2048)
while msg:
	li.append(msg)
	msg = s.recv(2048)

print(len(li))
HMAC = li[4]
cipher = li[0]
check(HMAC,cipher)
s.close() 