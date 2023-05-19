#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：p3-Transforms.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/31 9:21 
'''

from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
from torchvision import transforms

class MyData(Dataset):

    def __init__(self, root_dir, image_dir, label_dir, transform=None):
        self.root_dir = root_dir
        self.image_dir = image_dir
        self.label_dir = label_dir
        self.label_path = os.path.join(self.root_dir, self.label_dir)
        self.image_path = os.path.join(self.root_dir, self.image_dir)
        self.image_list = os.listdir(self.image_path)
        self.label_list = os.listdir(self.label_path)
        self.transform = transform
        # 因为label 和 Image文件名相同，进行一样的排序，可以保证取出的数据和label是一一对应的
        self.image_list.sort()
        self.label_list.sort()

    def __getitem__(self, idx):
        img_name = self.image_list[idx]
        label_name = self.label_list[idx]
        img_item_path = os.path.join(self.root_dir, self.image_dir, img_name)
        label_item_path = os.path.join(self.root_dir, self.label_dir, label_name)
        img = Image.open(img_item_path)
        with open(label_item_path, 'r') as f:
            label = f.readline()

        if self.transform:
            img = transform(img)


        return img, label

    def __len__(self):
        assert len(self.image_list) == len(self.label_list)
        return len(self.image_list)


transform = transforms.Compose([transforms.Resize(400), transforms.ToTensor()])
root_dir = "F:\ChromeCoreDownloads\coco128\images"
image_ants = "train2017"
label_ants = "train2017_lable"
ants_dataset = MyData(root_dir, image_ants, label_ants, transform=transform)
image_bees = "train2018"
label_bees = "train2018_lable"
bees_dataset = MyData(root_dir, image_bees, label_bees, transform=transform)







