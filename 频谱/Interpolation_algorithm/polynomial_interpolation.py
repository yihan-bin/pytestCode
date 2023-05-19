import numpy as np
import matplotlib
import math
import time
from matplotlib import pyplot
import numpy.linalg as lg

N=10
pi=math.pi
x=[]
y=[]
time1=time.time()
#等分点写法
for i in range(N):
    x.append(round((-1+(2/N)*(N-i)),3))#保留几位小数
# #非等分点写法
# for i in range(N):
#     x.append(math.cos(i*pi/N))

def function(x1):
    return math.sin(pi*x1)


for i in range(len(x)):
    y.append(function(x[i]))


print(x)
n=len(x)
X=np.zeros((n,n))

for i in range(n):
    for j in range(n):
        X[i][j]=math.pow(x[i],j)

print(X)

A=[]
XT=lg.inv(X)
Y=np.zeros((n,1))

for i in range(len(y)):
    Y[i][0]=y[i]

A=lg.solve(X,Y)

def polynomial_interploate(x1):
    p=0
    for i in range(len(x)):
        p+=A[i][0]*math.pow(x1,i)
    return p

x1=[]
y1=[]
y2=[]
for i in range(1000):
    x1.append(round((-1+(2/1000)*(1000-i)),3))
for i in range(1000):
    y1.append(polynomial_interploate(x1[i]))
for i in range(1000):
    y2.append(function(x1[i]))
time2=time.time()

pyplot.plot(x1,y1)

error=[]

for i in range(1000):
    error.append(abs(y1[i]-y2[i]))

print('耗时：',time2-time1)
print(max(error))

pyplot.show()




















