
import sys
import socket
from sys import argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)

if (len(argv) < 4) | (len(argv) > 4):
    print("missing arguments or too many Arguments")
    sys.exit()

if argv[1] == "":
    sys.exit()
else:
    try:
        socket.gethostbyname(argv[1])
    except socket.error:
        sys.exit()

if argv[2] == "":
    sys.exit()

try:
    sock.connect((argv[1], int(argv[2])))
    print("It connected")
except socket.error:
    print("Could not connect to port error")
    sys.exit()

file = open(argv[3], "rb")

sock.recv(5).decode("utf-8")
while True:

    send = file.read(600000000)
    if len(send) < 1:
        break
    sock.send(send)


file.close()

sock.close()