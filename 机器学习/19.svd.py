#!/usr/bin/env python
# coding: utf-8

# #### SVD

# In[1]:


import numpy as np


# In[2]:


A = np.array([[0,1],[1,1],[1,0]])
A


# In[3]:


u, s, vt = np.linalg.svd(A, full_matrices=True)
print(u.shape, s.shape, vt.shape)


# In[4]:


u


# In[5]:


s


# In[6]:


vt.T


# In[8]:


np.allclose(A, np.dot(u[:,:2]*s, vt))


# In[10]:


np.dot(u[:,:2]*s, vt)


# In[17]:


s_ = np.zeros((3,2))
for i in range(2):
    s_[i][i] = s[i]

s_


# In[22]:


np.dot(np.dot(u, s_), vt)


# In[7]:


import numpy as np
import os
from PIL import Image
from tqdm import tqdm

# 定义恢复函数，由分解后的矩阵恢复到原矩阵
def restore(u, s, v, K): 
    '''
    u:左奇异矩阵
    v:右奇异矩阵
    s:奇异值矩阵
    K:奇异值个数
    '''
    m, n = len(u), len(v[0])
    a = np.zeros((m, n))
    for k in range(K):
        uk = u[:, k].reshape(m, 1)
        vk = v[k].reshape(1, n)
        # 前k个奇异值的加总
        a += s[k] * np.dot(uk, vk)   
    a = a.clip(0, 255)
    return np.rint(a).astype('uint8')

A = np.array(Image.open("./louwill.jpg", 'r'))
# 对RGB图像进行奇异值分解
u_r, s_r, v_r = np.linalg.svd(A[:, :, 0])    
u_g, s_g, v_g = np.linalg.svd(A[:, :, 1])
u_b, s_b, v_b = np.linalg.svd(A[:, :, 2])

# 使用前50个奇异值
K = 50 
output_path = r'./svd_pic'
# 
for k in tqdm(range(1, K+1)):
    R = restore(u_r, s_r, v_r, k)
    G = restore(u_g, s_g, v_g, k)
    B = restore(u_b, s_b, v_b, k)
    I = np.stack((R, G, B), axis=2)   
    Image.fromarray(I).save('%s\\svd_%d.jpg' % (output_path, k))


# In[4]:


A.shape


# In[ ]:




