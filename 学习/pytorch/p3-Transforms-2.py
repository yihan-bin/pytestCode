#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：p3-Transforms.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/31 9:21 
'''

from torch.utils.data import Dataset, DataLoader
from PIL import Image
import os
from torchvision import transforms
from torch.utils.tensorboard import SummaryWriter
#日志路径
write=SummaryWriter('logs')


img_path='F:\\ChromeCoreDownloads\\coco128\\images\\train2017\\000000000009.jpg'
img=Image.open(img_path)
tensor_trans=transforms.ToTensor()
tensor_img=tensor_trans(img)

write.add_image('tensor_img',tensor_img)



#Normalize
#print(tensor_img[0][0])
tran_nom=transforms.Normalize([0.5,0.5,0.5],[0.5,0.5,0.5])
img_norm=tran_nom(tensor_img)
#print(img_norm[0][0])
write.add_image('Normalize',img_norm)
tran_nom=transforms.Normalize([0.5,3,0.5],[0.5,0.5,0.5])#ctrl+p,显示输入提示，
#先均值，后标准差，由于图片是三通道，所以输入每个通道对应的均值和标准差
write.add_image('Normalize',img_norm,2)#2代表第二阶段



#Resize
print(tensor_img.shape)
tran_rsize=transforms.Resize((512,512))

img_resize=tran_rsize(tensor_img)#可以是array或者pil数据类型，也可以是tensor数据类型
print(img_resize.shape)


#Compose

tran_rsize_2=transforms.Resize(100)
#transforms.Compose组合方法，比如此例子，先变换，在数据转换，有点类似delegate.combine
trans_compose=transforms.Compose([tran_rsize_2,tensor_trans])
img_resize2=trans_compose(img)
write.add_image('Resize',img_resize2,2)



#RandomCrop随机裁剪

trans_random=transforms.RandomCrop(400)
#trans_random=transforms.RandomCrop((500,1000))
tans_compose_2=transforms.Compose([trans_random,tensor_trans])
for i in range(10):
    img_crop=tans_compose_2(img)
    write.add_image('RandomCrop',img_crop,i)




write.close()



# class person:
#     def __call__(self, name):
#         print('__call__'+'hello'+name)
#     def hello(self,name):
#         print(name)
# per=person()
# per('zhang')
# per.hello('zjxij')