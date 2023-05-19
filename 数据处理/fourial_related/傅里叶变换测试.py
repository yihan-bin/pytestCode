from scipy.fftpack import fft , ifft
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.pylab as mpl
import re
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
y=[]
filename = '../数据/1.txt'

# y=7*np.sin(2*np.pi*200*x)+5*np.sin(2*np.pi*400*x)+3*np.sin(2*np.pi*600*x)
#---------------------------------------------------------------
with open(filename, 'r' ) as f:
    # 将txt中的数据逐行存到列表lines里 lines的每一个元素对应于txt中的一行。然后将每个元素中的不同信息提取出来
    lines = f.readlines()
    # i变量，由于这个txt存储时有空行，所以增只读偶数行，主要看txt文件的格式，一般不需要
    # j用于判断读了多少条，step为画图的X轴
    i = 0
for line in lines:


    j = len(line)
    if line[0] != "":
        f = line.split('\t')
        if len(f)>1:
            if f[1] != "":
                y.append(float(f[6]))
                i=i+1


x=np.linspace(0,1,i)


############################################################################
plt.figure()
plt.plot(x,y)
plt.title('原始波形图')
plt.figure()
plt.plot(x[0:50],y[0:50])
plt.title('前50组样本')
fft_y=fft(y)
# print(len(fft_y))
# print(fft_y[0:50])
N=1400
x=np.arange(i)
abs_y=np.abs(fft_y)
angle_y=np.angle(fft_y)
plt.figure()
plt.plot(x,abs_y)
plt.title('双边振幅频谱')
plt.figure()
plt.plot(x,angle_y)
plt.title('双边相位谱')
plt.show()


# filename = '../数据/20211220.log'
# writename= '../数据/正-4.txt'
# air, samp ,temp = [], [] ,[]
# k=0
# write_mark=0
# 相比open(),with open()不用手动调用close()方法
