#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：调用摄像头.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/17 17:38 
'''
import cv2
import time

cap=cv2.VideoCapture(1)
cap.set(3,900)
cap.set(4,900)
bo=cap.isOpened()
if bo:
    print('摄像头打开成功')
    flag,vshow=cap.read()
    print(flag)
    cv2.imshow('capture',vshow)
    cv2.waitKey(0)
else:
    print('摄像头打开失败')
