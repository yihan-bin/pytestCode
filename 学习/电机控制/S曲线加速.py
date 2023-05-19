#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：S曲线加速.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/2/9 9:11 
'''
import time

import numpy as np
import matplotlib.pyplot as plt
import random
def curves_init(fre_max,fre_min,acc_Number):
    '''

    :param fre_max: 目标频率
    :param fre_min: 最低频率
    :param acc_Number: 加速时间内执行周期数
    :return:
    '''
    plusCount = np.linspace(-5,5,acc_Number)
    time1=np.linspace(0,1,acc_Number)
    deno = 1. / (1 + np.exp(-plusCount))
    plusSum = deno.sum()
    delt = (fre_max-fre_min)
    frePlus=fre_min+delt*deno
    print(frePlus.sum())
    plt.plot(time1, frePlus)
    plt.show()
    return frePlus
class motor_t():
    def __int__(self):
        self.Status=0
        self.Count=0
        self.CountMax=0
        self.PWMcount=0.
        self.PWMneed=0.

Motor=motor_t()

def pluseOut(Plus,time_interval):
    scan_period=0.0001
    interval=time_interval/scan_period/2
    for i in range(int(interval)):
        output=1
        time.sleep(scan_period)
        output = 0
        time.sleep(scan_period)



if __name__=='__main__':
    frePlus=curves_init(10000,100,20)
    accCount=len(frePlus)
    print(accCount)
    cycleTime=0.1
    for i in range(accCount):
        pluseOut(frePlus[i],cycleTime)