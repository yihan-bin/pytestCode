import numpy as np
import matplotlib.pyplot as plt

"""
Q 系统噪声
R 测量噪声
X(k|k-1)   上一次状态预测结果
X(k-1|k-1) 上一时刻的最优预测值
P(k|k-1)   X(k|k-1)对应的convariance协方差
P(k-1|k-1) X(k-1|k-1) 对应的convariance协方差
"""


p_last = 0
Q = 0.1  # 系统噪声
R = 20  # 测量噪声
aaa=open("D:\\PycharmProjects\\learn\\Python测试\\大成\\exportdata\\1.txt", "rb", )
list1 = np.genfromtxt(aaa, delimiter="\t", encoding='utf-8',)
x_last = list1[0]
def kalman(z_measure, x_last=0, p_last=0, Q=0.018, R=20):
    x_mid = x_last
    p_mid = p_last + Q
    kg = p_mid / (p_mid + R)
    x_now = x_mid + kg * (z_measure - x_mid)
    p_now = (1 - kg) * p_mid
    p_last = p_now
    x_last = x_now
    return x_now, p_last, x_last


real = np.sin(np.linspace(0, 10, 100))
chao = np.random.rand(100) - 0.5
y1 = []
for i in range(len(list1)):
    pred, p_last, x_last = kalman(list1[i], x_last, p_last, Q, R)
    y1.append(pred)





aaa=open("D:\\PycharmProjects\\learn\\Python测试\\大成\\exportdata\\2.txt", "rb", )
list2 = np.genfromtxt(aaa, delimiter="\t", encoding='utf-8',)
x_last = list2[0]

y2 = []
for i in range(len(list2)):
    pred, p_last, x_last = kalman(list2[i], x_last, p_last, Q, R)
    y2.append(pred)


aaa=open("D:\\PycharmProjects\\learn\\Python测试\\大成\\exportdata\\3.txt", "rb", )
list3 = np.genfromtxt(aaa, delimiter="\t", encoding='utf-8',)
x_last = list3[0]

y3 = []
for i in range(len(list3)):
    pred, p_last, x_last = kalman(list3[i], x_last, p_last, Q, R)
    y3.append(pred)



aaa=open("D:\\PycharmProjects\\learn\\Python测试\\大成\\exportdata\\4.txt", "rb", )
list4 = np.genfromtxt(aaa, delimiter="\t", encoding='utf-8',)
x_last = list4[0]

y4 = []
for i in range(len(list4)):
    pred, p_last, x_last = kalman(list4[i], x_last, p_last, Q, R)
    y4.append(pred)










plt.figure()
#plt.plot(real, color="b")  # 真实值
plt.plot(list1, color="g")  # 测量值
plt.plot(y1, color="r")  # 预测值
plt.figure()
plt.plot(list2, color="g")  # 测量值
plt.plot(y2, color="r")  # 预测值

plt.figure()
plt.plot(list3, color="g")  # 测量值
plt.plot(y3, color="r")  # 预测值

plt.figure()
plt.plot(list4, color="g")  # 测量值
plt.plot(y4, color="r")  # 预测值


np.savetxt("1.txt", y1, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("2.txt", y2, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("3.txt", y3, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("4.txt", y4, fmt='%f', delimiter=',')  # 数组保存



plt.show()
