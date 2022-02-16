import socket
import requests
# Task 5i
url = 'https://www.abweb.biz'
r = requests.get(url)
print(r.text)
# Task 5ii
print("Status code:")
print("\t *", r.status_code, "OK")
# Task 5iii
h = requests.head(url)
print("Header:")
print("**********")
for x in h.headers:
    print("\t ", x, ":", h.headers[x])
print("**********")
# Task iv
headers = {
    'User-Agent': 'mobile'
    }
url2 = 'https://www.abweb.biz/'
rh = requests.get(url2, headers=headers)
print(rh.text)
# Task ?
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
