#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：串口查询.py
@IDE     ：PyCharm 
@Author  ：zw的摸鱼时刻
@Date    ：2023/1/11 15:20 
'''
import time

import serial
import serial.tools.list_ports
comport_list=[]
plist=list(serial.tools.list_ports.comports())
if len(plist)<=0:
    print('no serial')
else:
    plist_0=list(plist[0])
    serialName=plist_0[0]
    serialFd = serial.Serial(serialName, 9600, timeout=60)
    print("可用端口名>>>", serialFd.name)
    if serialFd.isOpen():
        print('打开')
    else:
        print('close')
    #serialFd.close()
    for i in range(len(plist)):

        comports = str(plist[i]).split('-')  #split一下会得到COMX这样的信息

        comport_list.append(comports[0])
    for comport in comport_list:
        try:
            s = serial.Serial(comport, 9600, timeout=0.8)
            if serialFd.isOpen():
                print('打开')
            else:
                print('close')
            s.close()

        except (OSError, serial.SerialException):
            print(serial.SerialException)
            time.sleep(100)













