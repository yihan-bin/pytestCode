import numpy as np
import matplotlib.pyplot as plt
import pylab

from matplotlib import pyplot as plt

filename = '../数据/6-横向趋势-右.txt'
man, mac, x_ray = [], [], []
# 相比open(),with open()不用手动调用close()方法
with open(filename, 'r') as f:
    # 将txt中的数据逐行存到列表lines里 lines的每一个元素对应于txt中的一行。然后将每个元素中的不同信息提取出来
    lines = f.readlines()
    # i变量，由于这个txt存储时有空行，所以增只读偶数行，主要看txt文件的格式，一般不需要
    # j用于判断读了多少条，step为画图的X轴
    i = 0

    a=[]
    b=[]
    c=[]
    k=0.0
    g=0.0
    m=0

    for line in lines:

        t = line.split('\t')
        j=len(t)
        if t[0]!="":
            f = t[0].split('\n')
            if f[0] != "":
                mac.append(float(f[0]))

        if j>1:
            f = t[1].split('\n')
            if f[0] != "":
                x_ray.append(float(f[0])+370)

        if j>2:
            f = t[2].split('\n')
            if f[0]!="":
                man.append(float(f[0])-35)
                m=m+1
                c.append(m)

a_len=len(mac)
b_len=len(x_ray)
c_len=len(man)
a_temp=c_len/a_len
b_temp=c_len/b_len
while(i<a_len)  :
    a.append(k)
    k=k+a_temp
    i=i+1
i=0
while (i<b_len) :
    b.append(g)
    g=g+b_temp
    i=i+1


# fig = plt.figure(figsize=(10, 5))  # 创建绘图窗口，并设置窗口大小
# # 画第一张图
# ax1 = fig.add_subplot(211)  # 将画面分割为2行1列选第一个
# ax1.plot(a,mac, 'red', label='mac')  # 画dis-loss的值，颜色红
# ax1.legend(loc='upper right')  # 绘制图例，plot()中的label值
# ax1.set_xlabel('step')  # 设置X轴名称
# ax1.set_ylabel('Discriminator-loss')  # 设置Y轴名称
#
# # 画第二张图
# ax2 = fig.add_subplot(212)  # 将画面分割为2行1列选第二个
# ax2.plot( b,x_ray, 'blue', label='x_ray')  # 画gan-loss的值，颜色蓝
# ax2.legend(loc='upper right')  # loc为图例位置，设置在右上方，（右下方为lower right）
# ax2.set_xlabel('step')
# ax2.set_ylabel('Generator-loss')
# plt.show()  # 显示绘制的图

plt.figure()
plt.plot(c, man, 'red', label='man')
plt.plot(a, mac, 'blue', label='mac')
plt.plot(b, x_ray, 'green', label='x_ray')
plt.title('6-横向趋势-右',fontproperties='SimHei')
plt.legend()
plt.show()

