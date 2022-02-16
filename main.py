import socket
import sys
import argparse


def ploadconnect(websiteB, portN):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Socket created succefully")
    except socket.error as err:
        print("Socket creation failed with erorr %s" % (err))

    port = portN

try:
    host_ip=socket.gethostbyname(website)
except socket.gaierror:
    print("There is a problem resolving the host")
    sys.exit()
    s.connect((host_ip, port))
    print("Succesfully connected to the website given %s:%s" % (host_ip, ports))

praser = argparse.ArgumentParser(description="Learn to connect to a website with port number")
praser.add_argument("-H", "--host", required=True, help="specify the hostname or website name")
praser.add_argument("-p", "-port", type=int, default=80, help="specify the port number eg. 80 for website")

args = praser.parse_args()
ploadconnect(args.host, args.port)
