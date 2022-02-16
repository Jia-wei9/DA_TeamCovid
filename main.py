import socket
s = socket.socket()
print("Socket created")
port= 80
s.bind(('',port))
print("Socket bind to %s"%(port))
s.listen(5)
print("Socket is listening...")
while True:
    c, addr=s.accept()
    print("Connection from",addr)