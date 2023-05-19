#!/usr/bin/env python
# coding: utf-8

# ### HMM

# In[3]:


import numpy as np

### 定义HMM模型
class HMM:
    def __init__(self, N, M, pi=None, A=None, B=None):
        # 可能的状态数
        self.N = N
        # 可能的观测数
        self.M = M
        # 初始状态概率向量
        self.pi = pi
        # 状态转移概率矩阵
        self.A = A
        # 观测概率矩阵
        self.B = B

    # 根据给定的概率分布随机返回数据
    def rdistribution(self, dist): 
        r = np.random.rand()
        for ix, p in enumerate(dist):
            if r < p: 
                return ix
            r -= p

    # 生成HMM观测序列
    def generate(self, T):
        # 根据初始概率分布生成第一个状态
        i = self.rdistribution(self.pi)  
        # 生成第一个观测数据
        o = self.rdistribution(self.B[i])  
        observed_data = [o]
        # 遍历生成剩下的状态和观测数据
        for _ in range(T-1):        
            i = self.rdistribution(self.A[i])
            o = self.rdistribution(self.B[i])
            observed_data.append(o)
        return observed_data


# In[4]:


# 初始状态概率分布
pi = np.array([0.25, 0.25, 0.25, 0.25])
# 状态转移概率矩阵
A = np.array([
    [0,  1,  0, 0],
    [0.4, 0, 0.6, 0],
    [0, 0.4, 0, 0.6],
[0, 0, 0.5, 0.5]])
# 观测概率矩阵
B = np.array([
    [0.5, 0.5],
    [0.6, 0.4],
    [0.2, 0.8],
    [0.3, 0.7]])
# 可能的状态数和观测数
N = 4
M = 2
# 创建HMM实例
hmm = HMM(N, M, pi, A, B)
# 生成观测序列
print(hmm.generate(5))


# In[6]:


### 前向算法计算条件概率
def prob_calc(O):
    '''
    输入：
    O：观测序列
    输出：
    alpha.sum()：条件概率
    '''
    # 初值
    alpha = pi * B[:, O[0]]
    # 递推
    for o in O[1:]:
        alpha_next = np.empty(4)
        for j in range(4):
            alpha_next[j] = np.sum(A[:,j] * alpha * B[j,o])
        alpha = alpha_next
    return alpha.sum()

# 给定观测
O = [1,0,1,0,0]
print(prob_calc(O))


# In[7]:


### 序列标注问题和维特比算法
def viterbi_decode(O):
    '''
    输入：
    O：观测序列
    输出：
    path：最优隐状态路径
    '''    
    # 序列长度和初始观测
    T, o = len(O), O[0]
    # 初始化delta变量
    delta = pi * B[:, o]
    # 初始化varphi变量
    varphi = np.zeros((T, 4), dtype=int)
    path = [0] * T
    # 递推
    for i in range(1, T):
        delta = delta.reshape(-1, 1)     
        tmp = delta * A
        varphi[i, :] = np.argmax(tmp, axis=0)
        delta = np.max(tmp, axis=0) * B[:, O[i]]
    # 终止
    path[-1] = np.argmax(delta)
    # 回溯最优路径
    for i in range(T-1, 0, -1):
        path[i-1] = varphi[i, path[i]]
    return path

# 给定观测序列
O = [1,0,1,1,0]
# 输出最可能的隐状态序列
print(viterbi_decode(O))


# In[ ]:




