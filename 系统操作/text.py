#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：text.py
@IDE     ：PyCharm 
@Author  ：zw的摸鱼时刻
@Date    ：2023/1/11 14:22 
'''
import os
format1 = '{:<8}\t{:<40}\t{}'
x=bytes(format1.format(r'PID', r'进程名', r'工作目录的绝对路径'),encoding='utf-8')
print(type(x))
with open("data/PID监测1.txt", 'ab') as f:
    f.write(bytes(format1.format(r'PID', r'进程名', r'工作目录的绝对路径') + os.linesep * 2,encoding='utf-8'))
    f.close()

























