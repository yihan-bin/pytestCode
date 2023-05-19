#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：p2-TensorBoard.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/31 9:21 
'''
from torch.utils.tensorboard import SummaryWriter
import random
import time
writer = SummaryWriter(log_dir='runs/mock_accuracy')
for i in range(100):
    '''
    数据显示，注意坐标，相同的tag，数据会写道一起，不同的tag，相互独立，数据也相互独立
    '''
    writer.add_scalar(tag="accuracy", # 可以暂时理解为图像的名字
                      scalar_value=i * random.uniform(0.8, 1),  # 纵坐标的值
                      global_step=i  # 当前是第几次迭代，可以理解为横坐标的值
                      )
    writer.add_scalar(tag="accuracy", # 可以暂时理解为图像的名字
                      scalar_value=i * i,  # 纵坐标的值
                      global_step=i  # 当前是第几次迭代，可以理解为横坐标的值
                      )
    writer.add_scalar(tag="x=y", # 可以暂时理解为图像的名字
                      scalar_value=i,  # 纵坐标的值
                      global_step=i  # 当前是第几次迭代，可以理解为横坐标的值
                      )
    #time.sleep(2 * random.uniform(0.5, 1.5))
