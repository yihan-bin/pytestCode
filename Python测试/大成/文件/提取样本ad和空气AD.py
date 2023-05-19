import numpy as np
import matplotlib.pyplot as plt
import pylab

from matplotlib import pyplot as plt
import random
import re
filename = '../数据/20211220.log'
writename= '../数据/正-4.txt'
air, samp ,temp = [], [] ,[]
k=0
write_mark=0
# 相比open(),with open()不用手动调用close()方法
with open(filename, 'r' ) as f:
    # 将txt中的数据逐行存到列表lines里 lines的每一个元素对应于txt中的一行。然后将每个元素中的不同信息提取出来
    lines = f.readlines()
    # i变量，由于这个txt存储时有空行，所以增只读偶数行，主要看txt文件的格式，一般不需要
    # j用于判断读了多少条，step为画图的X轴
    i = 0

def text_save(filename, data):#filename为写入CSV文件的路径，data为要写入数据列表.
  file = open(filename,'a')
  for i in range(len(data)):
    s = str(data[i]).replace('[','').replace(']','')#去除[],这两行按数据不同，可以选择
    s = s.replace("'",'') +','  #去除单引号，逗号，每行末尾追加换行符
    file.writelines(s)
  file.writelines('\n')
  file.close()

for line in lines:
    if '比值异常' in line:
        t=re.findall(r'[[](.*?)[]]', line)
        if len(t)>2:
             air_temp = t[1]
             samp_temp = t[2]
        temp.append(air_temp)
        temp.append(samp_temp)
        text_save(writename, temp)
        temp.clear()














