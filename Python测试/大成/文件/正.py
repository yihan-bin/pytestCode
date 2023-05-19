import numpy as np
import matplotlib.pyplot as plt
import pylab

from matplotlib import pyplot as plt
import random
filename = '../数据/正1.txt'
writename= '数据/正正1.txt'
mac, x_ray = [], []
k=0
write_mark=0
# 相比open(),with open()不用手动调用close()方法
with open(filename, 'r') as f:
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
    t = line.split('\t')
    if t[0]!="":
        f = t[0].split('\n')
        if f[0] != "":
            mac.append(float(f[0]))
length=len(mac)
for i in range(length) :
    if mac[i]>560 :
        x_ray.append(mac[i])
        write_mark=1
    if mac[i]<560 :
        k=0
        if write_mark !=0 :
            write_mark = 0

            text_save(writename, x_ray)
            x_ray.clear()






