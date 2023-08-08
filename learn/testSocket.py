from socket import socket
sk=socket()
sk.connect(('192.168.250.101',8080))

sk.send('1234'.encode('utf-8'))
print(sk.recv(1024))
sk.close()