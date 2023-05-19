#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：redis_test.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/18 11:03 
'''
import redis
import time
import numpy as np

pool = redis.ConnectionPool(host='localhost', port=6379, decode_responses=True)
r = redis.StrictRedis(host='localhost', port=6379, db=0)
arr=4
r.set(1,arr,ex=1)
'''
    set(name, value, ex=None, px=None, nx=False, xx=False)
    
    在 Redis 中设置值，默认，不存在则创建，存在则修改。
    
    参数：
    
    ex - 过期时间（秒）
    px - 过期时间（毫秒）
    nx - 如果设置为True，则只有name不存在时，当前set操作才执行
    xx - 如果设置为True，则只有name存在时，当前set操作才执行
    1.ex - 过期时间（秒） 这里过期时间是3秒，3秒后p，键food的值就变成None
'''
#time.sleep(3)
print(r.get(1))

r.mget({'k1': 'v1', 'k2': 'v2'})
#r.mset(k1="v1", k2="v2") # 这里k1 和k2 不能带引号，一次设置多个键值对
print(r.mget('k1', 'k2'))   # 一次取出多个键对应的值
print(r.mget('k1'))

r.hmset("hash2", {"k2": "v2", "k3": "v3"})
r.hget(name,key)






