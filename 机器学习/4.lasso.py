#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd


# In[58]:


data = np.genfromtxt('example.dat', delimiter = ',')
data.shape


# In[61]:


data[0]


# In[74]:


# 选择特征与标签
x = data[:,0:100] 
y = data[:,100].reshape(-1,1)
# 加一列
X = np.column_stack((np.ones((x.shape[0],1)),x))

# 划分训练集与测试集
X_train, y_train = X[:70], y[:70]
X_test, y_test = X[70:], y[70:]
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)


# In[13]:


# 定义参数初始化函数
def initialize(dims):
    w = np.zeros((dims, 1))
    b = 0
    return w, b


# In[1]:


# 定义符号函数
def sign(x):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0


# In[20]:


# 利用numpy对符号函数进行向量化
vec_sign = np.vectorize(sign)
vec_sign(np.zeros((3,1)))


# In[7]:


# 定义lasso损失函数
def l1_loss(X, y, w, b, alpha):
    num_train = X.shape[0]
    num_feature = X.shape[1]
    y_hat = np.dot(X, w) + b
    loss = np.sum((y_hat-y)**2)/num_train + np.sum(alpha*abs(w))
    dw = np.dot(X.T, (y_hat-y)) /num_train + alpha * vec_sign(w)
    db = np.sum((y_hat-y)) /num_train
    return y_hat, loss, dw, db


# In[98]:


# 定义训练过程
def lasso_train(X, y, learning_rate=0.01, epochs=300):
    loss_list = []
    w, b = initialize(X.shape[1])
    for i in range(1, epochs):
        y_hat, loss, dw, db = l1_loss(X, y, w, b, 0.1)
        w += -learning_rate * dw
        b += -learning_rate * db
        loss_list.append(loss)
        
        if i % 300 == 0:
            print('epoch %d loss %f' % (i, loss))
        params = {
            'w': w,
            'b': b
        }
        grads = {
            'dw': dw,
            'db': db
        }
    return loss, loss_list, params, grads


# In[99]:


# 执行训练示例
loss, loss_list, params, grads = lasso_train(X_train, y_train, 0.01, 3000)


# In[100]:


# 获取训练参数
params


# In[101]:


# 定义预测函数
def predict(X, params):
    w = params['w']
    b = params['b']
    
    y_pred = np.dot(X, w) + b
    return y_pred

y_pred = predict(X_test, params)
y_pred[:5]


# In[95]:


y_test[:5]


# In[102]:


from sklearn.metrics import r2_score
r2_score(y_pred, y_test)


# In[78]:


# 简单绘图
import matplotlib.pyplot as plt
f = X_test.dot(params['w']) + params['b']

plt.scatter(range(X_test.shape[0]), y_test)
plt.plot(f, color = 'darkorange')
plt.xlabel('X')
plt.ylabel('y')
plt.show();


# In[79]:


# 训练过程中的损失下降
plt.plot(loss_list, color = 'blue')
plt.xlabel('epochs')
plt.ylabel('loss')
plt.show()


# In[83]:


# 导入线性模型模块
from sklearn import linear_model
# 创建lasso模型实例
sk_lasso = linear_model.Lasso(alpha=0.1)
# 对训练集进行拟合
sk_lasso.fit(X_train, y_train)
# 打印模型相关系数
print("sklearn Lasso intercept :", sk_lasso.intercept_)
print("\nsklearn Lasso coefficients :\n", sk_lasso.coef_)
print("\nsklearn Lasso number of iterations :", sk_lasso.n_iter_)


# In[ ]:




