#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：传递函数3D.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/2/13 11:37 
'''
# import matplotlib.pyplot as plt
#
#
# from matplotlib import cm
# import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
#
#
# X = np.arange(-5, 5, 0.1)
# Y = np.arange(-5, 5, 0.25)
# X, Y = np.meshgrid(X, Y)
# R = np.sqrt(X**2 + Y**2)
# Z = np.sin(R)
# Z=(4*(X+Y)+5)/((X+Y)*(X+Y)+3*(X+Y)+3)
# # Plot the surface
# #fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
# #ax.plot_surface(X, Y, Z, vmin=Z.min() * 2, cmap=cm.Blues)
# ax = plt.axes(projection='3d')
# ax.contour3D(X, Y, Z, 50, cmap='binary')
# ax.set(xticklabels=[],
#        yticklabels=[],
#        zticklabels=[])
# #ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')
# plt.show()
import numpy as np
from matplotlib import pyplot as plt


def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2))
X = np.arange(-5, 5, 0.1)
Y = np.arange(-5, 5, 0.1)
# X, Y = np.meshgrid(X, Y)
# S=complex(X,Y)
S=[]
for i in range(len(X)):
    for j in range(len(X)):
    # S.append(complex(X[i],Y[i]))
        a=complex(X[i],Y[j])
        S.append(a)
S=np.array(S)

Z=(4*(X+Y)+5)/((X+Y)*(X+Y)+3*(X+Y)+3)
Z=(S+1)/(S*(S+2)*(S+3)*(S+4))
x=Z.real
y=Z.imag
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(x, y, Z, 50, cmap='binary')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.plot_surface(X,Y,Z,rstride=1,cstride=1,cmap=plt.get_cmap('rainbow'))
#调整观察角度和方位角。这里将俯仰角设为60度，把方位角调整为35度
ax.view_init(60, 35)
plt.show()
