# import numpy as np
#
# def data_zoom(idata,needed_len):
#     data_zoomed=[]
#     idata_len=len(idata)
#     for i in range(idata_len):
#         if idata_len>needed_len:
#

import numpy as np
from scipy import interpolate #插值
import matplotlib.pyplot as plt #Pyplot 是 Matplotlib 的子库，提供了和 MATLAB 类似的绘图 API。Pyplot 是常用的绘图模块，能很方便让用户绘制 2D 图表。
x0 = np.array([0, 3, 5, 7, 9, 11, 12, 13, 14, 15])
y0 = np.array([0, 1.2, 1.7, 2.0, 2.1, 2.0, 1.8, 1.2, 1.0, 1.6])
x1 = np.arange(0, 15, 0.1)#numpy.arange(start, stop, step, dtype)  np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
plt.figure(figsize=(8, 6))#创建一个8*6点（point）的点图

###将图作在一张图上
for method in [ "slinear", "cubic"]:  # 插值方式
    f = interpolate.interp1d(x0, y0, kind=method) #一维数据的插值运算可以通过方法 interp1d() 完成。kind=method指插值方法
    y1 = f(x1)#得到插值结果
    plt.plot(x1, y1, label=method)
plt.plot(x0,y0,'o',label="datas")
plt.title('Interpolation')
plt.legend(loc="lower right")#图例的位置
plt.show()

###3张子图
i=1
for method in [ "slinear", "cubic"]:  # 插值方式
    f = interpolate.interp1d(x0, y0, kind=method) #一维数据的插值运算可以通过方法 interp1d() 完成。kind=method指插值方法
    y1 = f(x1)#得到插值结果
    plt.subplot(1, 3, i)
    plt.plot(x1, y1)
    plt.title(method)
    i=i+1
plt.subplot(1, 3, i)
plt.plot(x0,y0,'o-')
plt.title("Piecewise linear")
plt.suptitle('Interpolation')
plt.show()

