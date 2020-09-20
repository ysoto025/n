#!/usr/bin/env python3

import sys
import socket
from sys import argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)

if len(argv) < 3:

    print("missing arguments")
    sys.exit()
try:
    sock.connect((argv[1], int(argv[2])))
    print("It connected")
except sock.gaierror as err:
    print("Could not connect to host due error:" + err)

file = open(argv[3], "rb")
accio = ""

sock.recv(5).decode("utf-8")
while True:

    send = file.read(2048)
    if len(send) < 1:
        break
    sock.send(send)



file.close()

sock.close()
