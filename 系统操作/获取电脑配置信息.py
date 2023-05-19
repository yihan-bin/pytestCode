#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：获取电脑配置信息.py
@IDE     ：PyCharm 
@Author  ：zw的摸鱼时刻
@Date    ：2023/1/11 11:41 
'''
import uuid
import wmi
import pymysql
import socket
class information:
    w = wmi.WMI()  # 获取配置信息
    list = []
    # db = pymysql.connect(host='',  # ip
    #                      user='',  # 用户名
    #                      password='',  # 密码
    #                      db='',  # 数据库
    #                      port=3306,
    #                      charset='utf8')


class INFO(information):
    def __init__(self):
        self.info()

    # 获取配置信息
    def info(self):

        for BIOSs in information.w.Win32_ComputerSystem():
            information.list.append("电脑名称: %s" % BIOSs.Caption)
            information.list.append("使 用 者: %s" % BIOSs.UserName)
        print(socket.gethostname())
        localIP = socket.gethostbyname(socket.gethostname())
        information.list.append("IP地址: %s" % localIP)

        address = hex(uuid.getnode())[2:]
        information.list.append("MAC地址: %s" % address)

        for BIOS in information.w.Win32_BIOS():
            information.list.append("使用日期: %s" % BIOS.Description)
            information.list.append("主板型号: %s" % BIOS.SerialNumber)

        for processor in information.w.Win32_Processor():
            information.list.append("CPU型号: %s" % processor.Name.strip())

        for memModule in information.w.Win32_PhysicalMemory():
            totalMemSize = int(memModule.Capacity)
            information.list.append("内存厂商: %s" % memModule.Manufacturer)
            information.list.append("内存型号: %s" % memModule.PartNumber)
            information.list.append("内存大小: %.2fGB" % (totalMemSize / 1024 ** 3))

        for disk in information.w.Win32_DiskDrive(InterfaceType="IDE"):
            diskSize = int(disk.size)
            information.list.append("磁盘名称: %s" % disk.Caption)
            information.list.append("磁盘大小: %.2fGB" % (diskSize / 1024 ** 3))

        for xk in information.w.Win32_VideoController():
            information.list.append("显卡名称: %s" % xk.name)


infor = information()
INFOs = INFO()
print(information.list)

