import pandas as pd
import numpy as np
import cchardet



# 获取文件编码类型
def get_encoding(file):
    # 二进制方式读取，获取字节数据，检测类型
    with open(file, 'rb') as f:
        data = f.read()
        return cchardet.detect(data)['encoding']


file_name = '../数据/DaAa_20221129.csv'
encoding = get_encoding(file_name)
print(encoding)

df= pd.read_csv('../数据/DaAa_20221129.csv', encoding='ansi')
#print(df.describe())
#print(df.head())
# print(df.columns)
# print(df['1'])
x=df['1'].tolist()
#print(x)
a=[]
for i in range(len(x)-1):
    if x[i]!=5:
        if x[i+1]-x[i]!=1:
            a.append(i)
    if x[i]==5:
        if x[i]-x[i+1]!=4:
            a.append(i)

print(a)

