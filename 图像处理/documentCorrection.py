#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：documentCorrection.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/16 11:17 
'''
import cv2 as cv
import matplotlib.pyplot as plt
import cv2
import numpy as np


img=cv.imread('source/test.jpg',cv.IMREAD_COLOR)

max_dim=max(img.shape)
dim_limit=1080

if max_dim>dim_limit:
    resize_tor=dim_limit/max_dim
    img=cv.resize(img,None,fx=resize_tor,fy=resize_tor)

origin_img=img.copy()

kernel=np.ones((5,5),np.uint8)
img=cv.morphologyEx(img,cv.MORPH_CLOSE,kernel,iterations=5)


# 通过GrabCut算法实现前景对象的分割
mask = np.zeros(img.shape[:2],np.uint8)
bgdModel = np.zeros((1,65),np.float64)
fgdModel = np.zeros((1,65),np.float64)
rect = (20,20,img.shape[1]-20,img.shape[0]-20)
cv.grabCut(img,mask,rect,bgdModel,fgdModel,1,cv.GC_INIT_WITH_RECT)
mask2 = np.where((mask==2)|(mask==0),0,1).astype('uint8')
img = img*mask2[:,:,np.newaxis]

#边缘检测
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (11, 11), 0)
# Edge Detection.
canny = cv2.Canny(gray, 100, 200)
canny = cv2.dilate(canny, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5)))
#轮廓检测
con = np.zeros_like(img)
# 对检测得到的边缘获取其轮廓
contours, hierarchy = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)
# 保留最大的轮廓，将其绘制在画布上，效果如下图：
page = sorted(contours, key=cv2.contourArea, reverse=True)[:5]
con = cv2.drawContours(con, page, -1, (0, 255, 255), 3)


#角点检测
# 对轮廓检测后的数据进行角点检测
con = np.zeros_like(img)
for c in page:
    # arcLength计算轮廓周长或曲线长度
    epsilon = 0.02 * cv2.arcLength(c, True)
    corners = cv2.approxPolyDP(c, epsilon, True)
    if len(corners) == 4:
        break
cv2.drawContours(con, c, -1, (0, 255, 255), 3)
cv2.drawContours(con, corners, -1, (0, 255, 0), 10)
corners = sorted(np.concatenate(corners).tolist())

for index, c in enumerate(corners):
    character = chr(65 + index)
    cv2.putText(con, character, tuple(c), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 1, cv2.LINE_AA)



# 透视变换
M = cv2.getPerspectiveTransform(np.float32(corners), np.float32(destination_corners))
# Perspective transform using homography.
final = cv2.warpPerspective(orig_img, M, (destination_corners[2][0], destination_corners[2][1]), flags=cv2.INTER_LINEAR)

cv.imshow('img',img)



cv.waitKey(0)

