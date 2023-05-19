import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

list = np.genfromtxt(open("../exportdata/666.csv", "rb"), delimiter=",", encoding='GBK')
filter_data=[]
arrSortedIndex = np.lexsort((list[:, 1], list[:, 2]))  # 排序，按照第三列在第四列进行排序
sorted_data = list[arrSortedIndex, :]
print(sorted_data[0][2])
sorted_data[:, 3] = sorted_data[:, 3]* 0.025/1000
#np.savetxt("dets.txt", sorted_data, fmt='%f', delimiter=',')  # 数组保存
for i in range(len(sorted_data[:, 3])-1):
    if (sorted_data[i+1, 3]-sorted_data[i, 3]>0) and (sorted_data[i+1, 3]-sorted_data[i, 3]<4):
        filter_data.append(sorted_data[i+1, :])
filter_data=np.array(filter_data)
np.savetxt("exportdata/dets.txt", sorted_data, fmt='%f', delimiter=',')  # 数组保存
fre = filter_data[:, 1]
NumNo = filter_data[:, 2]
Value = filter_data[:, 3]
#Value = Value * 0.025/1000

# a=[1,2,3,4,5,6]
# b=np.numpy(a)

myset = set(NumNo)
count = Counter(NumNo)
print(count[1.0])
no2 = count[1.0]
no3 = no2 + count[2.0]
no4 = no3 + count[3.0]
no5 = no4 + count[4.0]

A = []
dec=[]
for i in range(len(Value)-1):
    tem=Value[i+1]-Value[i]
    if tem>0 and tem <4:
        dec.append(tem)
for i in range(count[2.0]):

    for j in range(count[1.0]):
        TEM=Value[no2 + i] - Value[count[j]]
        if ((Value[no2 + i] - Value[count[j]]) > 8) and ((Value[no2 + i] - Value[count[j]]) < 9.5):
            A.append(Value[no2 + i]  - Value[count[j]])
A1 = np.array(A)
#A1 = sorted(A1)
B = []
for i in range(count[3.0]):
    for j in range(count[2.0]):
        tem=Value[no3 + i] - Value[count[no2]+j]

        if ((Value[no3 + i] - Value[count[no2]+j]) > 59.3) and ((Value[no3 + i] - Value[count[no2]+j]) < 59.4):
            B.append(Value[no3 + i] - Value[count[no2]+j])
B1 = np.array(B)
#B1 = sorted(B1)
C = []
for i in range(count[4.0]):
    for j in range(count[3.0]):
        if ((Value[no4 + i] - Value[count[no3]+j]) > 12.6) and ((Value[no4 + i] - Value[count[no3]+j]) < 12.9):
            C.append(Value[no4 + i] - Value[count[no3]+j])
C1 = np.array(C)
#C1 = sorted(C1)
D = []
for i in range(count[5.0]):
    for j in range(count[4.0]):
        if ((Value[no5 + i] - Value[count[no4]+j]) > 69.8) and ((Value[no5 + i] - Value[count[no4]+j]) < 70):
            D.append(Value[no5 + i] - Value[count[no4]+j])

D1 = np.array(D)
#D1 = sorted(D1)

# len_arr=[]
# len_arr.append(len(A1))
# len_arr.append(len(B1))
# len_arr.append(len(C1))
# len_arr.append(len(D1))
# len_arr = sorted(len_arr)
# y = np.zeros([len_arr[-1], 4], dtype=float, order='C')
# y[:len(A1), 0] = A1
# y[:len(B1), 1] = B1
# y[:len(C1), 2] = C1
# y[:len(D1), 3] = D1
# print(y)
np.savetxt("exportdata/1.txt", A1, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("exportdata/2.txt", B1, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("exportdata/3.txt", C1, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("exportdata/4.txt", D1, fmt='%f', delimiter=',')  # 数组保存
print(count)
plt.figure()
plt.plot(A1)
plt.figure()
plt.plot(B1)
plt.figure()
plt.plot(C1)
plt.figure()
plt.plot(D1)
plt.figure()
plt.plot(dec)
np.savetxt("exportdata/5.txt", dec, fmt='%f', delimiter=',')  # 数组保存
plt.show()
