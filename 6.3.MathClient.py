#!/usr/bin/env python3

import sys
import socket

Csocket = socket.socket()
host = '172.20.10.6'
port = 8989

print("Waiting for connection.....")

try:
    Csocket.connect((host, port))
except socket.error as e:
    print(str(e))

msg = Csocket.recv(1024)
print(msg.decode('utf-8'))
while True:

    print("\nMathematical Function")
    print("[1] Logarithmic function (log)")
    print("[2] Square Root function (sqrt)")
    print("[3] Exponential function (exp)")
    print("[q] Exit system")
    option = input('Please choose the option you would like to use:  ')

    if option == '1' or option == '2' or option == '3':
        value = input("Enter a value: ")
        option = option + ":" + value
        Csocket.send(str.encode(option))

    elif option == 'q':
        print("Exiting system.")
        b = input("yes?")
        Csocket.send(b.encode())
        sys.exit()

    else:
        print("Input not recognize")
        sys.exit()

    msg = Csocket.recv(1024)
    print(msg.decode("utf-8"))

Csocket.close()
