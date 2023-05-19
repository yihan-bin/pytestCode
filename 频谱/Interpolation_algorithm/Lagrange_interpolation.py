import numpy as np
import matplotlib
import math
import time
from matplotlib import pyplot

N=10
pi=math.pi
x=[]
y=[]
time1=time.time()
#等分点写法
for i in range(N):
    x.append(round((-1+(2/N)*(N-i)),3))
# #非等分点写法
# for i in range(N):
#     x.append(math.cos(i*pi/N))

def function(x1):
    return math.sin(pi*x1)


for i in range(len(x)):
    y.append(function(x[i]))

def lagrange_interploate(x1):
    p=[]
    L_n=0
    for i in range(len(x)):
        numerator=1
        denominator=1.0
        for j in range(len(x)):
            if j!=i:
                numerator*=(x1-x[j])
                temp=x[i] - x[j]
                denominator*=temp
        if denominator==0:
            i;
        p.append(numerator/denominator)
    for i in range(len(x)):
        L_n+=y[i]*p[i]
    return round(L_n,3)

x1=[]
y1=[]
y2=[]
for i in range(1000):
    x1.append(round((-1+(2/1000)*(1000-i)),3))
for i in range(1000):
    y1.append(lagrange_interploate(x1[i]))
for i in range(1000):
    y2.append(function(x1[i]))
time2=time.time()
pyplot.figure()
pyplot.plot(x1,y1)

error=[]

for i in range(1000):
    error.append(abs(y1[i]-y2[i]))
pyplot.figure()
pyplot.plot(error)
print('耗时：',time2-time1)
print(max(error))

pyplot.show()




















