#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：p4-nn_Conv.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/2/1 9:11 
'''

import torch
import torch.nn.functional as F
import numpy as np
input = torch.tensor([[1, 2, 0, 3, 1],
                      [0, 1, 2, 3, 1],
                      [1, 2, 1, 0, 0],
                      [5, 2, 3, 1, 1],
                      [2, 1, 0, 1, 1]])

kernel = torch.tensor([[1, 2, 1],
                       [0, 1, 0],
                       [2, 1, 0]])

input = torch.reshape(input, (1,1,1, 1, 5, 5))
kernel = torch.reshape(kernel, (1, 1, 3, 3))
input=np.array(input)
print(input.shape)
print(kernel.shape)

output = F.conv2d(input, kernel, stride=1)
print(output)

output2 = F.conv2d(input, kernel, stride=2)
print(output2)

output3 = F.conv2d(input, kernel, stride=1, padding=1)
print(output3)