#! /usr/bin/env python3
#Client side

import socket
import hmac
import hashlib
from Crypto.Cipher import AES
from Crypto import Random

password = 'Super_secret_passPhrase12'

def hash_gen(text):
	hash = hashlib.sha512(text).hexdigest()
	return hash 

def unpad(text):
	return text.rstrip()

def decrypt(salt,enc,iv,password):
	private_key = hashlib.scrypt(password.encode(), salt=salt, n=2**14, r=8, p=1, dklen=32)
	cipher = AES.new(private_key, AES.MODE_CBC, iv)
	decrypted = cipher.decrypt(enc)
	original = str(unpad(decrypted))
	original = original[2:len(original)-1]
	return original

def check(HMAC,cipher,sha,password,salt,iv):
	passbytes= b'Super_secret_passPhrase12'
	hmac_hash = hmac.new(cipher, passbytes, hashlib.sha1)
	if hmac_hash.digest() == HMAC:
		print('Sender verified')
		if hash_gen(cipher) == sha.decode():
			print('Integrity check Passed.')
			print(decrypt(salt,cipher,iv,password))
		else: print('Integrity failed')
	else: print('Sender unverified.')

password = 'Super_secret_passPhrase12'

host = 'local host'
port = int(input('port:'))
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
s.connect(('', port)) 
li = []
msg = s.recv(2048)
while msg:
	li.append(msg)
	msg = s.recv(2048)

print('len of li : ',len(li))
print(li)
HMAC = li[4]
cipher = li[0]
sha = li[3]
salt = li[1]
iv=li[2]
check(HMAC,cipher,sha,password,salt,iv)
s.close() 