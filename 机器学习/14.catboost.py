#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import catboost as cb
from sklearn.metrics import f1_score

# 读取数据
data = pd.read_csv('./adult.data', header=None)
# 变量重命名
data.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 
                'marital-status', 'occupation', 'relationship', 'race', 'sex', 
                'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
# 标签转换
data['income'] = data['income'].astype("category").cat.codes
# 划分数据集
X_train, X_test, y_train, y_test = train_test_split(data.drop(['income'], axis=1), data['income'],
                                                    random_state=10, test_size=0.3)
# 配置训练参数
clf = cb.CatBoostClassifier(eval_metric="AUC", depth=4, iterations=500, l2_leaf_reg=1,
                            learning_rate=0.1)
# 类别特征索引
cat_features_index = [1, 3, 5, 6, 7, 8, 9, 13]
# 训练
clf.fit(X_train, y_train, cat_features=cat_features_index)
# 预测
y_pred = clf.predict(X_test)
# 测试集f1得分
print(f1_score(y_test, y_pred))


# In[2]:


data.head()


# In[3]:


data.columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation',
                'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'income']
data.head()


# In[5]:


data['income'] = data['income'].astype("category").cat.codes
data['income'].value_counts()


# In[7]:


from sklearn.model_selection import train_test_split, GridSearchCV
X_train, X_test, y_train, y_test = train_test_split(data.drop(['income'], axis=1), data['income'],
                                                    random_state=10, test_size=0.3)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)


# In[9]:


import catboost as cb
cat_features_index = [1, 3, 5, 6, 7, 8, 9, 13]
params = {'depth': [4, 6],
          'learning_rate': [0.01, 0.1],
          'l2_leaf_reg': [1, 4, 9],
          'iterations': [500]}

cb = cb.CatBoostClassifier()
cb_model = GridSearchCV(cb, params, scoring="roc_auc", cv=3)
cb_model.fit(X_train, y_train, cat_features=cat_features_index)


# In[10]:


print(cb_model.best_score_)  
print(cb_model.best_params_)


# In[13]:


import catboost as cb
clf = cb.CatBoostClassifier(eval_metric="AUC", depth=4, iterations=500, l2_leaf_reg=1,
                            learning_rate=0.1)

clf.fit(X_train, y_train, cat_features=cat_features_index)


# In[14]:


y_pred = clf.predict(X_test)
y_pred.shape


# In[16]:


from sklearn.metrics import f1_score
print(f1_score(y_test, y_pred))


# In[17]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_pred)


# In[18]:


from sklearn.metrics import classification_report
classification_report(y_test, y_pred)


# In[ ]:




