#!/usr/bin/env python
# coding: utf-8

# In[2]:


import xgboost as xgb
import lightgbm as lgb
import catboost as cb


# In[3]:


import numpy as np
import pandas as pd
import time
from sklearn.model_selection import train_test_split


# In[4]:


data = pd.read_csv("flights.csv")
data = data.sample(frac=0.01, random_state=10)

data = data[["MONTH","DAY","DAY_OF_WEEK","AIRLINE","FLIGHT_NUMBER","DESTINATION_AIRPORT",
                 "ORIGIN_AIRPORT","AIR_TIME", "DEPARTURE_TIME","DISTANCE","ARRIVAL_DELAY"]]
data.shape


# In[5]:


data = data.reset_index(drop=True)
data.head()


# In[6]:


data["ARRIVAL_DELAY"] = (data["ARRIVAL_DELAY"]>10)*1

cols = ["AIRLINE","FLIGHT_NUMBER","DESTINATION_AIRPORT","ORIGIN_AIRPORT"]
for item in cols:
    data[item] = data[item].astype("category").cat.codes +1
    
X_train, X_test, y_train, y_test = train_test_split(data.drop(["ARRIVAL_DELAY"], axis=1), data["ARRIVAL_DELAY"],
                                                random_state=10, test_size=0.3)
print(X_train.shape, y_train.shape, X_test.shape, y_test.shape)


# In[7]:


y_train.value_counts()


# In[8]:


y_test.value_counts()


# In[13]:


from sklearn.metrics import f1_score
from sklearn.metrics import accuracy_score, roc_auc_score

# 设置模型参数
params = {
    'booster': 'gbtree',
    'objective': 'binary:logistic',   
    'gamma': 0.1,
    'max_depth': 8,
    'lambda': 2,
    'subsample': 0.7,
    'colsample_bytree': 0.7,
    'min_child_weight': 3,
    'eta': 0.001,
    'seed': 1000,
    'nthread': 4,
}
t0 = time.time()
# plst = params.items()
num_rounds = 500
dtrain = xgb.DMatrix(X_train, y_train)
model_xgb = xgb.train(params, dtrain, num_rounds)
print('training spend {} seconds'.format(time.time()-t0))
# 对测试集进行预测
t1 = time.time()
dtest = xgb.DMatrix(X_test)
y_pred = model_xgb.predict(dtest)
print('testing spend {} seconds'.format(time.time()-t1))
y_pred_train = model_xgb.predict(dtrain)
print(roc_auc_score(y_train, y_pred_train))
print(roc_auc_score(y_test, y_pred))


# In[22]:


d_train = lgb.Dataset(X_train, label=y_train)
params = {"max_depth": 5, "learning_rate" : 0.05, "num_leaves": 500,  "n_estimators": 300}

#With Catgeorical Features
cate_features_name = ["MONTH","DAY","DAY_OF_WEEK","AIRLINE","DESTINATION_AIRPORT",
                 "ORIGIN_AIRPORT"]
t0 = time.time()
model_lgb = lgb.train(params, d_train, categorical_feature = cate_features_name)
print('training spend {} seconds'.format(time.time()-t0))
t1 = time.time()
y_pred = model_lgb.predict(X_test)
print('testing spend {} seconds'.format(time.time()-t1))
y_pred_train = model_lgb.predict(X_train)
print(roc_auc_score(y_train, y_pred_train))
print(roc_auc_score(y_test, y_pred))


# In[25]:


cat_features_index = [0,1,2,3,4,5,6]
t0 = time.time()
model_cb = cb.CatBoostClassifier(eval_metric="AUC", one_hot_max_size=50, 
                            depth=6, iterations=300, l2_leaf_reg=1, learning_rate=0.1)
model_cb.fit(X_train,y_train, cat_features= cat_features_index)
print('training spend {} seconds'.format(time.time()-t0))
t1 = time.time()
y_pred = model_cb.predict(X_test)
print('testing spend {} seconds'.format(time.time()-t1))
y_pred_train = model_cb.predict(X_train)
print(roc_auc_score(y_train, y_pred_train))
print(roc_auc_score(y_test, y_pred))


# In[36]:


### RandomSearch
from sklearn.model_selection import RandomizedSearchCV
# from scipy.stats import uniform
model = xgb.XGBClassifier()
param_lst = {'max_depth': [3,5,7], 
                 'min_child_weight': [1,3,6], 
                 'n_estimators': [100,200,300],
                 'learning_rate': [0.01, 0.05, 0.1]
                }
t0 = time.time()
random_search = RandomizedSearchCV(model, param_lst, random_state=0)
random_search.fit(X_train, y_train)
print(random_search.best_params_)
print('randomsearch for xgb spend', time.time()-t0, 'seconds.')


# In[26]:


### GridSearch
from sklearn.model_selection import GridSearchCV
model = xgb.XGBClassifier()
param_lst = {"max_depth": [3,5,7],
              "min_child_weight" : [1,3,6],
              "n_estimators": [100,200,300],
              "learning_rate": [0.01,0.05,0.1]
             }
t0 = time.time()
grid_search = GridSearchCV(model, param_grid=param_lst, cv=3, 
                                   verbose=10, n_jobs=-1)
grid_search.fit(X_train, y_train)
print('gridsearch for xgb spend', time.time()-t0, 'seconds.')


# In[10]:


print(grid_search.best_estimator_)


# In[32]:


### Bayesian Opt
from bayes_opt import BayesianOptimization
from tqdm import tqdm

def xgb_evaluate(min_child_weight,
                 colsample_bytree,
                 max_depth,
                 subsample,
                 gamma,
                 alpha):

    params['min_child_weight'] = int(min_child_weight)
    params['cosample_bytree'] = max(min(colsample_bytree, 1), 0)
    params['max_depth'] = int(max_depth)
    params['subsample'] = max(min(subsample, 1), 0)
    params['gamma'] = max(gamma, 0)
    params['alpha'] = max(alpha, 0)


    cv_result = xgb.cv(params, dtrain, num_boost_round=num_rounds, nfold=5,
             seed=random_state,
             callbacks=[xgb.callback.early_stop(50)])

    return cv_result['test-auc-mean'].values[-1]


# In[30]:


res = xgb_evaluate(3, 0.5, 4, 0.6, 1, 1)
res


# In[33]:


num_rounds = 3000
random_state = 2021
num_iter = 25
init_points = 5
params = {
    'eta': 0.1,
    'silent': 1,
    'eval_metric': 'auc',
    'verbose_eval': True,
    'seed': random_state
}

xgbBO = BayesianOptimization(xgb_evaluate, {'min_child_weight': (1, 20),
                                            'colsample_bytree': (0.1, 1),
                                            'max_depth': (5, 15),
                                            'subsample': (0.5, 1),
                                            'gamma': (0, 10),
                                            'alpha': (0, 10),
                                            })

xgbBO.maximize(init_points=init_points, n_iter=num_iter)


# In[ ]:




