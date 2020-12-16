#! /usr/bin/env python3

import socket 

def hash_gen(text):
	hash = hashlib.sha256(text).hexdigest()
	return hashlib 

host = 'local host'
port = 5001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect(('', port)) 

msg = s.recv(2048)
#print(msg)
while msg: 
    print(str(msg)) 
    msg = s.recv(2048)

li=str(msg).split('||') 
s.close() 