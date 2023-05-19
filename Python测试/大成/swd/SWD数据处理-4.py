import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
aaa=open("../exportdata/155.csv", "rb", )
list1 = np.genfromtxt(aaa, delimiter="\t", encoding='utf-8',)
sorted_data=[]
sorted_datay=[]


x1,x3=[],[]
x1=list1[:,4]
x3=list1[0:351,10]
x4=list1[0:351,14]
x2=range(0,len(x3),1)
plt.figure()
plt.plot(x1)
plt.figure()
plt.plot(x3)
plt.figure()
plt.plot(x4)


fig,ax1=plt.subplots() #subplots一定要带s
ax1.plot(x2,x4,c='r')
ax1.set_ylabel('EXP')
ax2=ax1.twinx() #twinx将ax1的X轴共用与ax2，这步很重要
ax2.plot(x2,x3,c='g')
ax2.set_ylabel('Log')

plt.show()
