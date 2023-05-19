#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：内存操作.py
@IDE     ：PyCharm 
@Author  ：zw的摸鱼时刻
@Date    ：2023/1/11 11:59 
'''

import ctypes

value = 'hello world'  # 定义一个字符串变量
address = id(value)  # 获取value的地址，赋给address
get_value = ctypes.cast(9290793213, ctypes.py_object)  # 读取地址中的变量
print(address,get_value)