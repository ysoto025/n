
import sys
import socket
from sys import argv
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
#sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 2048)


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

if argv[2] == "":
    sys.stderr.write("ERROR: empty string")
    sys.exit(1)

if (int(argv[2]) < 0) | (int(argv[2]) > 65535):
    sys.stderr.write("ERROR: Overflow error")
    sys.exit(1)

try:
    sock.settimeout(10.0)
    sock.connect((argv[1], int(argv[2])))
    sock.recv(5)
except socket.error:
    sys.stderr.write("ERROR: data not received")
    sys.exit(1)
except socket.timeout:
    sys.stderr.write("ERROR: timeout")
    sys.exit(1)

sock.settimeout(None)
file = open(argv[3], "rb")

sock.recv(5)
while True:

    send = file.read(600000)
    if len(send) < 1:
        break
    try:
        sock.send(send)
    except socket.error:
        sys.stderr.write("ERROR: broken pipe")
        sys.exit(0)

file.close()

sock.close()