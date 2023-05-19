#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：blueTooth.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/18 8:50 
'''
import sys
import bluetooth
nearby_devices=bluetooth.discover_devices(lookup_names=True)
print('Found {} devices.'.format(len(nearby_devices)))

for addr,name in nearby_devices:
    print('{}-{}'.format(addr,name))


def bt_device_type(device_type):
    if device_type == 5898764 or device_type == 'Android':
        return 'Android'
    if device_type == 7078144 or device_type == 'computer_ubuntu14':
        return 'computer_ubuntu14'
    if device_type == 786700 or device_type == 'computer_ubuntu16':
        return 'computer_ubuntu16'
    if device_type == 655620 or device_type == 'computer_windows':
        return 'computer_windows'
    if device_type == 2360324 or device_type == 'headset':
        return 'headset' #耳机
    if device_type == 2360328 or device_type =='speaker':
        return 'speaker' # 扩音器
    if device_type == 263208 or device_type == 'SV':
        return 'SV' #蓝牙音响
    if device_type == 7995916 or device_type == 'phone':
        return 'phone' #苹果设备
    if device_type == 3670284 or device_type == 'MACBook':
        return 'MACBook'
    if device_type == 7936 or device_type == 2752780 or device_type == 'PC':
        return 'PC'
    if device_type == 6947088 or device_type == 'iPad':
        return 'iPad'
    return 'unknown'
bluetooth.__version__




addr = None

if len(sys.argv) < 2:
    print("No device specified. Searching all nearby bluetooth devices for "
          "the SampleServer service...")
else:
    addr = sys.argv[1]
    print("Searching for SampleServer on {}...".format(addr))
addr='1C:52:16:91:00:3C'
# search for the SampleServer service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
name='QCY Melobuds ANC'
service_matches = bluetooth.find_service(name=name,uuid=uuid, address=addr)

if len(service_matches) == 0:
    print("Couldn't find the SampleServer service.")
    sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"{}\" on {}".format(name, host))

# Create the client socket
sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
sock.connect((host, port))

print("Connected. Type something...")
while True:
    data = input()
    if not data:
        break
    sock.send(data)

sock.close()


















