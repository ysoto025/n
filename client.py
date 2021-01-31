
import sys
import socket
from sys import argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)

print (len(argv))
if (len(argv) < 4) | (len(argv) > 4):
    sys.stderr.write("missing arguments or too many Arguments")
    sys.exit()

if (argv[1] == ""):
    sys.stderr.write("ERROR: empty string")
    sys.exit()
else:
    try:
        socket.gethostbyname(argv[1])
    except socket.error:
        sys.stderr.write("ERROR: wrong host")
        sys.exit(1)

if argv[2] == "":
    sys.stderr.write("ERROR: empty string")
    sys.exit()
elif int(argv[2]) < 0 | int(argv[2]) > 65535:
    sys.stderr.write("ERROR: Overflow error")
    sys.exit(1)

try:
    sock.connect((argv[1], int(argv[2])))
except socket.error:
    sys.stderr.write("ERROR: wrong port")
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