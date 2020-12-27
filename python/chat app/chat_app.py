#! /usr/bin/env python3

#Server side
import os
import hashlib
import socket
from Crypto.Cipher import AES
from Crypto import Random
import hmac
import time

password = 'Super_secret_passPhrase12'

def pad(s):
	block=16
	padding=block-(len(s)%block)
	return s + padding*' '

def encrypt(plaintext, password):
	salt = os.urandom(AES.block_size)
	iv = Random.new().read(AES.block_size)
	private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
	padded_text = pad(plaintext)
	config = AES.new(private_key, AES.MODE_CBC, iv)
	cipher = config.encrypt(padded_text)
	return (cipher,salt,iv)

def hash_gen(text):
	hash = hashlib.sha512(text).hexdigest()
	return hash 

host = 'local host'
port = int(input('Port'))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('',port))
s.listen(1)
c,add = s.accept()	
print('Connection from : ',str(add))
cipher, salt, iv = encrypt(input('Enter your text here: '),password)
password = b'Super_secret_passPhrase12'
hmac_hash = hmac.new(cipher, password, hashlib.sha1)

c.send(cipher)
time.sleep(1)
c.send(salt)
time.sleep(1)
c.send(iv)
time.sleep(1)
c.send(hash_gen(cipher).encode())
time.sleep(1)
c.send(hmac_hash.digest())
c.close()
