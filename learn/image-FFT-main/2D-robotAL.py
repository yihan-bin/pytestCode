import matplotlib.pyplot as plt
import numpy as np
import math
def pf(x):
    return pow(x,2)
x1=[0,3]
y1=[0,4]
i=0.1
x2=np.zeros(2)
y2=np.zeros(2)

y=[]
spoint=[2,2]
gpoint=[4,5]
thelt=np.arctan2((gpoint[1]-spoint[1]),(gpoint[0]-spoint[0]))
locus=[]
angle=[]
l=np.sqrt((gpoint[1]-spoint[1])**2+(gpoint[0]-spoint[0])**2)
l1=5
l2=4
k=100
for i in range(k+1):
    x=spoint[0]+l*i/k*np.cos(thelt)
    y=spoint[1]+l*i/k*np.sin(thelt)
    locus.append([x,y])
    tem=-(pow(l2,2)-pow(l1,2)-pow(x,2)-pow(y,2))/2/l1/np.sqrt(pow(x,2)+pow(y,2))
    fthelt=np.arccos(tem)
    thelt1=np.arctan2(y,x)-fthelt
    thelt2=np.arccos((x**2+y**2-l1**2-l2**2)/2/l1/l2)
    angle.append([thelt1,thelt2+thelt1])
# plt.plot(locus[:,0],locus[:,1])
# plt.show()


point1=[]
point2=[]

for i in range(k):
    plt.cla()
    x1[1]=l1*np.cos(angle[i][0])
    y1[1]=l1*np.sin(angle[i][0])
    x2[0]=x1[1]
    y2[0]=y1[1]
    x2[1]=x1[1]+l2*np.cos(angle[i][1])
    y2[1]=y1[1]+l2*np.sin(angle[i][1])
    point1.append(x2[1])
    point2.append(y2[1])

    # x1[1]=
    # y1[1]=
    # x2[0]=
    # y2[0]=
    # x2[1]=
    # y2[1]=


#    plt.scatter(x1[1], y1[1], color='black', s=5)
    plt.scatter(spoint[0], spoint[1], color='black', s=5)
    plt.scatter(gpoint[0], gpoint[1], color='black', s=5)
    plt.scatter(point1, point2, color='r', s=2)

    plt.plot(x1, y1, linewidth=2, color='black')
    plt.plot(x2, y2, linewidth=2, color='black')
    plt.xlim(-10,10)
    plt.ylim(-10,10)
    plt.pause(0.001)
# plt.subplot(1,2,1)
# plt.plot(angle[:,0])
# plt.subplot(1,2,2)
# plt.plot(angle[:,1])

plt.show()