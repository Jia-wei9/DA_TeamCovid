import socket
import requests

url = 'https://www.facebook.com'
r = requests.get(url)
print(r.text)

h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")

s = socket.socket()
print("Socket created")
port = 8080
s.bind(('', port))
print("Socket bind to %s" % (port))
s.listen(5)
print("Socket is listening...")
while True:
    c, addr = s.accept()
    print("Connection from", addr)
