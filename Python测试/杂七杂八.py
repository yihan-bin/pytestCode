import socket
import time
udp_socket=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
send_data='ijeijx'
send_addr=('192.168.1.174',8081)
udp_socket.sendto(send_data.encode('utf-8'),send_addr)
#rec_data=udp_socket.recvfrom(1024)
#print(rec_data)
a=[1,2,3]
a=a-2
print(a)
while True:
    t=time.localtime()
    print(t.tm_year)