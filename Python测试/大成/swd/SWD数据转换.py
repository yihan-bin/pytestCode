import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
import struct
list1 = np.genfromtxt(open("../exportdata/2444.csv", "rb"), delimiter=",", encoding='GBK')


def int4Lint(a):
    f = 0
    z1 = ''
    try:
        for k in range(4):
            z = hex(a[-k - 1])[2:].zfill(4)  # 取0x后边的部分 右对齐 左补零
            z1 = z1 + z
        f = struct.unpack('!q', bytes.fromhex(z1))[0]  # 返回浮点数
    except BaseException as e:
        f = e
    return f

def realtobyte(a):

    try:
        f = struct.pack('!d', a)
        q = struct.unpack('!q', f)  # 返回浮点数# 返回浮点数
    except BaseException as e:
        q = e
    return q
for i in range(len(list1)):
    if list1[i][2]==6:
        list1[i][3]=realtobyte(list1[i][3])[0]


np.savetxt("qqqq.txt", list1, fmt='%f', delimiter=',')  # 数组保存



