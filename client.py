import os
import sys
import socket
from sys import argv
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

if (len(argv) < 4) | (len(argv) > 4):
    sys.stderr.write("missing arguments or too many Arguments")
    sys.exit()

if (argv[1] == ""):
    sys.stderr.write("ERROR: empty string")
    sys.exit(1)
else:
    try:
        socket.gethostbyname(argv[1])
    except socket.error:
        sys.stderr.write("ERROR: wrong host")
        sys.exit(1)

if (int(argv[2]) < 0) | (int(argv[2]) > 65535):
    sys.stderr.write("ERROR: Overflow error")
    sys.exit(1)

if argv[2] == "":
    sys.stderr.write("ERROR: empty string")
    sys.exit(1)

try:
    mySocket.settimeout(10.0)
    mySocket.connect((argv[1], int(argv[2])))
    mySocket.recv(5)
except socket.error:
    sys.stderr.write("ERROR: data not received")
    sys.exit(1)
except socket.timeout:
    sys.stderr.write("ERROR: timeout")
    sys.exit(1)

mySocket.settimeout(None)
fileName = argv[3]
file = open(argv[3], "rb")
fileStats = os.stat(fileName)
mySocket.recv(5)

header1 = "Content-Disposition: attachment; filename= " + argv[3] + "\r\n "
header2 = "Content-Type: application/octet-stream\r\n"
header3 = "Content-Length: {0}\r\n\r\n".format(fileStats.st_size)


while True:
    mySocket.send(bytes(header1.encode()))
    mySocket.send(bytes(header2.encode()))
    mySocket.send(bytes(header3.encode()))
    send = file.read(600000)
    if len(send) < 1:
        break
    try:
        mySocket.send(send)
    except socket.error:
        sys.stderr.write("ERROR: broken pipe")
        sys.exit(0)

file.close()

mySocket.close()