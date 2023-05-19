#!/usr/bin/env python
# coding: utf-8
# ## 机器学习入门
# In[1]:
# 导入numpy模块
import numpy as np
# 将整数列表转换为NumPy数组
a = np.array([1,2,3])
# 查看数组对象
a
# In[2]:
# 查看整数数组对象类型
a.dtype
# In[3]:
# 将浮点数列表转换为NumPy数组
b = np.array([1.2, 2.3, 3.4])
# 查看浮点数数组对象类型
b.dtype
# In[5]:
# 将两个整数列表转换为二维NumPy数组
c = np.array([[1,2,3], [4,5,6]])
c
# In[6]:
# 生成2×3的全0数组
np.zeros((2, 3))
# In[8]:
# 生成3×4的全1数组
np.ones((3, 4), dtype=np.int16)
# In[9]:
# 生成2×3的随机数数组
np.empty([2, 3])
# In[10]:
# arange方法用于创建给定范围内的数组
np.arange(10, 30, 5 )
# In[11]:
# 生成3×2的符合(0,1)均匀分布的随机数数组
np.random.rand(3, 2)
# In[12]:
# 生成0到2范围内长度为5的数组
np.random.randint(3, size=5)
# In[13]:
# 生成一组符合标准正态分布的随机数数组
np.random.randn(3)
# In[14]:
# 创建一个一维数组 
a = np.arange(10)**2
a
# In[15]:
# 获取数组的第3个元素
a[2]
# In[16]:
# 获取第2个到第4个数组元素
a[1:4]
# In[17]:
# 一维数组翻转
a[::-1]
# In[18]:
# 创建一个多维数组
b = np.random.random((3,3))
b
# In[19]:
# 获取第2行第3列的数组元素
b[1,2]
# In[20]:
# 获取第2列数据
b[:,1]
# In[21]:
# 获取第3列前两行数据
b[:2, 2]
# In[22]:
# 创建两个不同的数组
a = np.arange(4)
b = np.array([5,10,15,20])
# 两个数组做减法运算
b-a
# In[23]:
# 计算数组的平方
b**2
# In[24]:
# 计算数组的正弦值
np.sin(a)
# In[25]:
# 数组的逻辑运算
b<20
# In[26]:
# 数组求均值和方差
np.mean(b)
# In[27]:
# 数组求方差
np.var(b)
# In[31]:
# 创建两个不同的数组
A = np.array([[1,1],
              [0,1]])
B = np.array([[2,0],
              [3,4]])
# 矩阵元素乘积
A * B
# In[32]:
# 矩阵点乘
A.dot(B)
# In[33]:
# 矩阵求逆
np.linalg.inv(A)
# In[34]:
# 矩阵求行列式
np.linalg.det(A)
# In[36]:
# 创建一个3×4的数组
a = np.floor(10*np.random.random((3,4)))
a
# In[37]:
# 查看数组维度
a.shape
# In[38]:
# 数组展平
a.ravel()
# In[39]:
# 将数组变换为2×6数组
a.reshape(2,6)
# In[40]:
# 求数组的转置
a.T
# In[42]:
a.T.shape
# In[43]:
# -1维度表示NumPy会自动计算该维度
a.reshape(3,-1)
# In[44]:
# 按行合并代码清单1-7中的A数组和B数组
np.hstack((A,B))
# In[45]:
# 按列合并A数组和B数组
np.vstack((A,B))
# In[46]:
# 创建一个新数组
C = np.arange(16.0).reshape(4, 4)
C
# In[47]:
# 按水平方向将数组C切分为两个数组
np.hsplit(C, 2)
# In[48]:
# 按垂直方向将数组C切分为两个数组
np.vsplit(C, 2)
# In[49]:
# 导入iris数据集和逻辑回归算法模块
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
# 导入数据
X, y = load_iris(return_X_y=True)
# 拟合模型
clf = LogisticRegression(random_state=0).fit(X, y)
# 预测
clf.predict(X[:2, :])
# In[50]:
# 概率预测
clf.predict_proba(X[:2, :])
# In[51]:
# 模型准确率
clf.score(X, y)
# In[ ]:
