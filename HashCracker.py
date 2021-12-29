#!/bin/python3

import hashlib

pass_found=0

hash_input=input("Enter the encrypted pass(Hashed passwd): ")

pass_doc= input("Enter the passwd file name including path: ")

try:
	pass_file=open(pass_doc, 'r')


except:
	print("Error in opening file")
	print(pass_doc, " is not found, Please enter the path correctly!")
	quit()

for word in pass_file:
	enc_word = word.encode('utf-8')
	hash_word =hashlib.md5(enc_word.strip())
	digest=hash_word.hexdigest()

	if digest==hash_input:
		print("Passwd found. The passwd is: ",)
		pass_found=1
		break


if not pass_found:
	print("Passwd is not found in the ",pass_doc," file")
	

