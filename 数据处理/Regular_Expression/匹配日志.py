import numpy as np
import re
import matplotlib.pyplot as plt
from collections import Counter
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker

file=open("../数据/DaPa_20221130.txt", "r", encoding='ANSI')
context=file.read()
#print(context)
MacNo=re.findall(r'架号:(\d+)',context)
MacNo=[ int(x) for x in MacNo]
Value=re.findall(r'检测值:(\d+)',context)
Value=[ int(x) for x in Value]
print(MacNo)
print(Value)
b=[]
for i in range(len(MacNo)-1):
    if (MacNo[i+1]-MacNo[i]==1) and MacNo[i+1]==2:
        b.append(Value[i+1]/Value[i])


plt.figure()
plt.plot(b)
plt.show()