#!/usr/bin/env python
# coding: utf-8

# ### Naive Bayes

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


### 构造数据集
### 来自于李航统计学习方法表4.1
x1 = [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3]
x2 = ['S','M','M','S','S','S','M','M','L','L','L','M','M','L','L']
y = [-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]

df = pd.DataFrame({'x1':x1, 'x2':x2, 'y':y})
df.head()


# In[3]:


X = df[['x1', 'x2']]
y = df[['y']]


# In[6]:


def nb_fit(X, y):
    classes = y[y.columns[0]].unique()
    class_count = y[y.columns[0]].value_counts()
    class_prior = class_count/len(y)
    
    prior = dict()
    for col in X.columns:
        for j in classes:
            p_x_y = X[(y==j).values][col].value_counts()
            for i in p_x_y.index:
                prior[(col, i, j)] = p_x_y[i]/class_count[j]
    return classes, class_prior, prior


# In[8]:


classes, class_prior, prior = nb_fit(X, y)
print(classes, class_prior, prior)


# In[6]:


X_test = {'x1': 2, 'x2': 'S'}


# In[7]:


classes, class_prior, prior = nb_fit(X, y)

def predict(X_test):
    res = []
    for c in classes:
        p_y = class_prior[c]
        p_x_y = 1
        for i in X_test.items():
            p_x_y *= prior[tuple(list(i)+[c])]
        res.append(p_y*p_x_y)
    return classes[np.argmax(res)]


# In[10]:


print('测试数据预测类别为：', predict(X_test))


# In[15]:


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=0)
gnb = GaussianNB()
y_pred = gnb.fit(X_train, y_train).predict(X_test)
print("Accuracy of GaussianNB in iris data test:", 
      accuracy_score(y_test, y_pred))


# In[ ]:




