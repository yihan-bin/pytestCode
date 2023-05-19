import time

import numpy as np
import re
import csv
filename='data/2.txt'
# bom=np.genfromtxt(filename,encoding='utf-8',delimiter='\t',dtype=str)
# #print(bom)
# for line in bom:
#     if 'e' in line:
#         print(line)
#########################################################################
starttime=time.time()
dq_type = 'eq', 'er', 'EQ', 'ER', 'Eq', 'Er', 'eR', 'eQ'
f=open(filename,encoding='utf-8')
context=f.read()
boms=context.split('\t')
encoding_extrat=[]
for i in range(len(boms)):
    if boms[i][:2] in dq_type:
        encoding_extrat.append([[boms[i]],[boms[i+1]],[boms[i+2]]])
print(encoding_extrat)
# bom=[]
# for line in f:
#     bom.append(f.readline().split('\t'))
#     if 'e' or 'E' in line:
#         print(line)
#print(encoding_extrat)
print(time.time()-starttime)
starttime=time.time()
compareFile='data/测试.txt'
BOMlist=[]
with open(compareFile,encoding='utf-8') as f:
    context = f.read()
    BOMlist_T=context.split('\t')
    for i  in range(len(BOMlist_T)):
        if BOMlist_T[i]!='':
            if BOMlist_T[i][:2] in dq_type and len(BOMlist_T[i])>4:
                type=BOMlist_T[i].split('-')[0]
                encode=BOMlist_T[i].split('-')[1]
                BOMlist.append([[type],[encode],[BOMlist_T[i+2]],[BOMlist_T[i+7]]])

#print(BOMlist)
print(time.time()-starttime)


















