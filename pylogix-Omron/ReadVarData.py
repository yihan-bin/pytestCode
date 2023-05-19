from pylogix import PLC
import numpy as np


filename = r'data/variable.txt'
man, mac, x_ray = [], [], []
# 相比open(),with open()不用手动调用close()方法
with open(filename, 'r',encoding='utf-8') as f:
    # 将txt中的数据逐行存到列表lines里 lines的每一个元素对应于txt中的一行。然后将每个元素中的不同信息提取出来
    lines = f.readlines()
    # i变量，由于这个txt存储时有空行，所以增只读偶数行，主要看txt文件的格式，一般不需要
    # j用于判断读了多少条，step为画图的X轴
    i = 0
    a=[]
    for line in lines:
        t = line.split('\t')
        if t[0]=='HOST':
            continue
        if 'WorkPos' in t[1]:
            if '.' in t[1]:
                pass
            else:
                a.append(t[1])
        # if len(a)>50:
        #     break
f.close()
print(a)
print(len(a))

temp=[]
comm = PLC()
comm.IPAddress = '192.168.250.1'
for i in range(len(a)):
    print(a[i])
    ret = comm.Read(a[i])
    print(ret.Value)
    temp.append([a[i],ret.Value])
# ret = comm.Read('Load_TrayZAxis1_Para')
# print(ret.Value)
comm.Close()
# temp=np.array(temp)
# np.savetxt('a.txt',temp,delimiter='\t')
with open('33b.txt','w',encoding='utf-8') as f:
    for data in temp:
        i=str(data[1]).strip('[').strip(']').replace(',','\t').replace('\'','')
        f.writelines(data[0]+'\t'+i+'\n')


f.close()