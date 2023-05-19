#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：photoToJPG.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/2/27 11:23 
'''
import os
import cv2
import sys
import numpy as np

from pathlib import Path
path1 = r"G:/Release/images"
path2 = r'G:/Release/images2/'
# path1=Path(path1)
# path2=Path(path2)
images = os.listdir(path1)
for i in os.listdir(path1):
    print(os.path.splitext(i))  # ('34474006827920603', '.png')
    if os.path.splitext(i)[1] == ".jpeg":
        path_TT=path1 + '/'+i
        img = cv2.imread(path_TT)
        # print(img)
        new_imagename = i.replace(".jpeg", ".jpg")
        path_t=path2 + new_imagename
        cv2.imwrite(path_t, img)

    elif os.path.splitext(i)[1] == ".png":
        path_TT=path1 + '/'+i
        img = cv2.imread(path_TT)
        # print(img)
        new_imagename = i.replace(".png", ".jpg")
        path_t=path2 + new_imagename
        cv2.imwrite(path_t, img)

    elif os.path.splitext(i)[1] == ".JPG":
        path_TT=path1 + '/'+i
        img = cv2.imread(path_TT)
        # print(img)
        new_imagename = i.replace(".JPG", ".jpg")
        path_t=path2 + new_imagename
        cv2.imwrite(path_t, img)

    elif os.path.splitext(i)[1] == ".PNG":
        path_TT=path1 + '/'+i
        img = cv2.imread(path_TT)
        # print(img)
        new_imagename = i.replace(".PNG", ".jpg")
        path_t=path2 + new_imagename
        cv2.imwrite(path_t, img)

    elif os.path.splitext(i)[1] == ".jpg":
        path_TT=path1 + '/'+i
        img = cv2.imread(path_TT)
        # print(img)
        new_imagename = i.replace(".jpg", ".jpg")
        path_t=path2 + new_imagename
        cv2.imwrite(path_t, img)