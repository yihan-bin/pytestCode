#!/usr/bin/env python
# coding: utf-8

# ### kmeans

# In[1]:


import numpy as np
from sklearn.cluster import KMeans


# In[2]:


X = np.array([[0,2],[0,0],[1,0],[5,0],[5,2]])
X


# In[14]:


from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=2, random_state=0).fit(X)
print(kmeans.labels_)


# In[4]:


kmeans.predict([[0, 0], [12, 3]])


# In[5]:


kmeans.cluster_centers_


# In[6]:


import numpy as np
# 定义欧式距离
def euclidean_distance(x1, x2):
    distance = 0
    # 距离的平方项再开根号
    for i in range(len(x1)):
        distance += pow((x1[i] - x2[i]), 2)
    return np.sqrt(distance)

print(euclidean_distance(X[0], X[4]))


# In[7]:


# 定义中心初始化函数
def centroids_init(k, X):
    m, n = X.shape
    centroids = np.zeros((k, n))
    for i in range(k):
        # 每一次循环随机选择一个类别中心
        centroid = X[np.random.choice(range(m))]
        centroids[i] = centroid
    return centroids


# In[8]:


# 定义样本的最近质心点所属的类别索引
def closest_centroid(sample, centroids):
    closest_i = 0
    closest_dist = float('inf')
    for i, centroid in enumerate(centroids):
        # 根据欧式距离判断，选择最小距离的中心点所属类别
        distance = euclidean_distance(sample, centroid)
        if distance < closest_dist:
            closest_i = i
            closest_dist = distance
    return closest_i


# In[9]:


# 定义构建类别过程
def build_clusters(centroids, k, X):
    clusters = [[] for _ in range(k)]
    for x_i, x in enumerate(X):
        # 将样本划分到最近的类别区域
        centroid_i = closest_centroid(x, centroids)
        clusters[centroid_i].append(x_i)
    return clusters


# In[10]:


# 根据上一步聚类结果计算新的中心点
def calculate_centroids(clusters, k, X):
    n = X.shape[1]
    centroids = np.zeros((k, n))
    # 以当前每个类样本的均值为新的中心点
    for i, cluster in enumerate(clusters):
        centroid = np.mean(X[cluster], axis=0)
        centroids[i] = centroid
    return centroids


# In[11]:


# 获取每个样本所属的聚类类别
def get_cluster_labels(clusters, X):
    y_pred = np.zeros(X.shape[0])
    for cluster_i, cluster in enumerate(clusters):
        for X_i in cluster:
            y_pred[X_i] = cluster_i
    return y_pred


# In[12]:


# 根据上述各流程定义kmeans算法流程
def kmeans(X, k, max_iterations):
    # 1.初始化中心点
    centroids = centroids_init(k, X)
    # 遍历迭代求解
    for _ in range(max_iterations):
        # 2.根据当前中心点进行聚类
        clusters = build_clusters(centroids, k, X)
        # 保存当前中心点
        prev_centroids = centroids
        # 3.根据聚类结果计算新的中心点
        centroids = calculate_centroids(clusters, k, X)
        # 4.设定收敛条件为中心点是否发生变化
        diff = centroids - prev_centroids
        if not diff.any():
            break
    # 返回最终的聚类标签
    return get_cluster_labels(clusters, X)


# In[13]:


# 测试数据
X = np.array([[0,2],[0,0],[1,0],[5,0],[5,2]])
# 设定聚类类别为2个，最大迭代次数为10次
labels = kmeans(X, 2, 10)
# 打印每个样本所属的类别标签
print(labels)


# In[ ]:




