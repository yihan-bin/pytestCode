#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：p1-Dataset.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/31 9:20 
'''
from torch.utils.data import Dataset
import cv2
from PIL import Image
import os
import torch
torch.version
class MyData(Dataset):
    '''
    Dataset对应的是数据集的加载，吧所需数据集加载到一起，定义一个可以迭代的对象，方便索引
    和定义一个路径文件，确认数据的来源。
    '''
    def __init__(self,root_dir,label_dir):
        self.root_dir = root_dir
        self.label_dir = label_dir
        self.path = os.path.join(self.root_dir, self.label_dir)
        self.img_path = os.listdir(self.path+'\\')


    def __getitem__(self, idx):
        img_name = self.img_path[idx]
        img_item_path = os.path.join(self.root_dir, self.label_dir, img_name)
        img = Image.open(img_item_path)
        label = self.label_dir
        return img, label

    def __len__(self):
        return len(self.img_path)

root_dir = "F:\ChromeCoreDownloads\coco128\images"
ants_label_dir = "train2017"
bees_label_dir = "train2018"
ants_dataset = MyData(root_dir, ants_label_dir)
bees_dataset = MyData(root_dir, bees_label_dir)
train_dataset = ants_dataset + bees_dataset
img, label = train_dataset[50]
img.show()
