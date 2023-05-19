#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：cocomarkShow.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/17 11:12 
'''
from pathlib import Path
import cv2 as cv
import numpy as np
import os
import sys
import yaml

ROOT = Path('F:\ChromeCoreDownloads\datasets\coco128')
FILE = Path(__file__).resolve()
# ROOT = FILE.parents[0]  # YOLOv5 root directory
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))  # add ROOT to PATH
image_path = ROOT / 'images\\train2017'
label_path = ROOT / 'labels\\train2017'
dir_list = os.listdir(image_path)
yaml_path = 'F:\ChromeCoreDownloads\yolov5-master\data\coco128.yaml'


def read_yaml():
    with open(yaml_path, encoding='utf-8') as f:
        data = yaml.load(f.read(), Loader=yaml.FullLoader)
        return data['names']

categorys = read_yaml()
for name in dir_list:
    img_name = image_path / str(name)
    label_name_t = name.split('.')[0] + '.txt'
    label_name = label_path / label_name_t
    img = cv.imread(str(img_name))
    labels = np.loadtxt(label_name, encoding='utf-8', delimiter=' ')
    n = labels.shape[-1]
    (w, h, d) = img.shape
    print(name, n)
    if labels.ndim > 1:
        for label in labels:
            category = categorys[int(label[0])]
            w1, h1 = int(label[1] * w - label[3] * w / 2), int(label[2] * h - label[4] * h / 2)
            w2, h2 = int(label[1] * w + label[3] * w / 2), int(label[2] * h + label[4] * h / 2)
            # w1, h1 = int(label[3] * w - label[1] * w / 2), int(label[4] * h + label[2] * h / 2)
            # w2, h2 = int(label[3] * w + label[1] * w / 2), int(label[4] * h - label[2] * h / 2)
            w1, h1 = int(label[1] * h - label[3] * h / 2), int(label[2] * w - label[4] * w / 2)
            w2, h2 = int(label[1] * h + label[3] * h / 2), int(label[2] * w + label[4] * w / 2)
            # w1, h1 = int(label[1] * w), int(label[2] * h)
            # w2, h2 = int(label[3] * w ), int(label[4] * h)
            cv.rectangle(img, (w1, h1), (w2, h2), (0, 0, 255))
            cv.putText(img, category, (w1, h1), cv.FONT_HERSHEY_PLAIN, 2.0, (100, 200, 200))
    elif labels.ndim == 1:
        category = categorys[int(labels[0])]
        w1, h1 = int(labels[1] * h - labels[3] * h / 2), int(labels[2] * w - labels[4] * w / 2)
        w2, h2 = int(labels[1] * h + labels[3] * h / 2), int(labels[2] * w + labels[4] * w / 2)
        cv.rectangle(img, (w1, h1), (w2, h2), (0, 0, 255))
        cv.putText(img, category, (w1, h1), cv.FONT_HERSHEY_DUPLEX, 2.0, (255, 200, 200))
    cv.imshow(name, img)
    # cv.imshow('123', img[:30][:30][:])
    cv.waitKey(0)
    cv.destroyWindow(name)
