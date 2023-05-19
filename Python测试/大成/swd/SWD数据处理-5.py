import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
aaa=open("../exportdata/te.csv", "rb", )
list1 = np.genfromtxt(aaa, delimiter="\t", encoding='utf-8',)
sorted_data=np.array(list1)
fre = sorted_data[:, 1]
NumNo = sorted_data[:, 2]
Value = sorted_data[:, 3]
Value = Value * 0.025/1000

# a=[1,2,3,4,5,6]
# b=np.numpy(a)

myset = set(NumNo)
count = Counter(NumNo)
A=[]
for i in range(count[2.0]):
    for j in range(count[1.0]):
        TEM=Value[count[1.0] + i] - Value[count[j]]
        if ((Value[count[1.0] + i] - Value[count[j]]) > 8) and ((Value[count[1.0] + i] - Value[count[j]]) < 9.5):
            A.append(Value[count[1.0] + i]  - Value[count[j]])
A1 = np.array(A)
A1 = sorted(A1)
# x1,x3=[],[]
# x1=list1[:,4]
# x3=list1[0:351,10]
# x4=list1[0:351,14]
# x2=range(0,len(x3),1)
# plt.figure()
# plt.plot(x1)
# plt.figure()
# plt.plot(x3)
# plt.figure()
# plt.plot(x4)

plt.figure()
plt.plot(A1)


# fig,ax1=plt.subplots() #subplots一定要带s
# ax1.plot(x2,x4,c='r')
# ax1.set_ylabel('EXP')
# ax2=ax1.twinx() #twinx将ax1的X轴共用与ax2，这步很重要
# ax2.plot(x2,x3,c='g')
# ax2.set_ylabel('Log')

plt.show()
