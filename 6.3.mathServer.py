#!/usr/bin/env python3

import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock):
	s_sock.send(str.encode("Welcome to the Server\n"))
	while True:
		data = s_sock.recv(2048).decode('utf-8')

		if data == '1':
			reply = math.log(float(data))
		elif data == '2':
			reply = math.sqrt(float(data))
		elif data == '3':
			reply = math.exp(float(data))
		else:
			break

		s.sock.sendall(str.encode(str(reply)))
	s_sock.close()

if __name__ == '__main__':
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = ''
	port = 8989

	s.bind((host,port))
	print("Listening...")
	s.listen(3)

	try:
		while True:
			try:
				s_sock, s_addr = s.accept()
				math = Process(target=process_start, args = (s_sock,))
				math.start()
			except socket.error():
				print("An error has occured on the socket!")
	except Exception as e:
		print("An exception has occured!")
		print(e)
