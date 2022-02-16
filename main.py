import socket
import sys

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket created successfully")
except socket.error as err:
    print("Socket creation failed with error %s" % (err))

port=80
try:
    host_ip = socket.gethostbyname("www.facebook.com")
except socket.gaierror:
    sys.exit()
s.connect((host_ip, port))
print("Successfully connect to the website given %s:%s" % (host_ip, port))

s = socket.socket()
print("Socket created")
s.bind(('', port))
print("Socket bind to %s" % (port))
s.listen(5)
print("Socket is listening...")
while True:
    c, addr = s.accept()
    print("Connection from", addr)

import argparse

def ploadconnect(websiteN, portN):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created successfully")
    except socket.error as err:
        print("Socket creation failed with error %s"%(err))

    ports= portN

    try:
        host_ip =socket.gethostbyname(websiteN)
    except socket.gaierror:
        print("There is a problem resolving the host")
        sys.exit()
        s.connect((host_ip,ports))
        print("Succesfully connected to the website given %s:%s"%(host_ip,ports))

praser=argparse.ArgumentParser(description="Learn to connect to a website with port number")
praser.add_argument("-H","--host",required=True, help="specify the hostname or website name")
praser.add_argument("-p","-port",type=int, default=80, help="specify the port number eg. 80 for website")

args=praser.parse_args()
ploadconnect(args.host,args.port)