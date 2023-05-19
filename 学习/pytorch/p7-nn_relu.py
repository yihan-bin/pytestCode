#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：p7-nn_relu.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/2/1 10:19 
'''
import torch
import torchvision
from torch import nn
from torch.nn import ReLU, Sigmoid
from torch.utils.data import DataLoader
from torch.utils.tensorboard import SummaryWriter
import numpy as np
input = torch.tensor([[1, -0.5],
                      [-1, 3]])

input = torch.reshape(input, (-1, 1, 2, 2))
print(input.shape)

dataset = torchvision.datasets.CIFAR10("../data", train=False, download=True,
                                       transform=torchvision.transforms.ToTensor())

dataloader = DataLoader(dataset, batch_size=64)

class Tudui(nn.Module):
    def __init__(self):
        super(Tudui, self).__init__()
        #激活函数x=MAX(x,0)
        self.relu1 = ReLU()
        #sigmoid函数，x=1/(1+1/(exp(x))把数据映射到-1到1上面，由于图片数据都是大于0，所以，得到的数据都是在0-1之间
        self.sigmoid1 = Sigmoid()

    def forward(self, input):
        output = self.sigmoid1(input)
        return output

tudui = Tudui()

writer = SummaryWriter("../logs")
step = 0
for data in dataloader:
    imgs, targets = data
    writer.add_images("input", imgs, global_step=step)
    output = tudui(imgs)
    temArr=np.array(output)
    writer.add_images("output", output, step)
    step += 1

writer.close()