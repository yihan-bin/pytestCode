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
from torch.utils.tensorboard import SummaryWriter

write=SummaryWriter('logs')





img_path='F:\\ChromeCoreDownloads\\coco128\\images\\train2017\\000000000009.jpg'
img=Image.open(img_path)
tensor_trans=transforms.ToTensor()
tensor_img=tensor_trans(img)

write.add_image('tensor_img',tensor_img)
write.close()




