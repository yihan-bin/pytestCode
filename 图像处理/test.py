#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：test.py
@IDE     ：PyCharm 
@Author  ：zw的摸鱼时刻
@Date    ：2023/1/13 8:50 
'''
import numpy as np
import yaml
arr1=[[1,2],[2,1]]
arr2=[[1,0],[1,0]]
arr1=np.array(arr1)
arr2=np.array(arr2)
arr3=arr1*arr2
arr4=arr1.dot(arr2)
print(arr3)
a=np.sum(arr3)
b=np.sum(arr4)
print(sum(arr3))


yaml_path = 'F:\ChromeCoreDownloads\yolov5-master\models\yolov5l.yaml'
def read_yaml():
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data

categorys = read_yaml()
a=1


