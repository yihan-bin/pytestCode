import sys

import CRC
import socket
import time

command = [0xAA, 0xA5, 0x03, 0x41, 0x42, 0x43,0x32]
crc_num = CRC.cal_crc_table(command)
print(crc_num)
BUFFSIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # 创建 socket 对象
remote_host = '192.168.1.146'
local_host='192.168.1.109'
host = socket.gethostname()  # 获取本地主机名
remote_port = 8888  # 设置端口
locale_port=1069
remote_addr = (remote_host, remote_port)
addr=(local_host, locale_port)
#s.connect(remote_addr)  # 绑定端口
s.bind(addr)
s.sendto("acrffd".encode('utf-8'),remote_addr)
recvData, addrs = s.recvfrom(BUFFSIZE)
print(recvData)
print(addrs)
