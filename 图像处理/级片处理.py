import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

pic = cv.imread('data/1.bmp')
print(pic.shape)
(b,g,r)=cv.split(pic)
# cv.imshow('res',b)
chanel=pic.shape
plt.plot()
colour=(r,g,b)
for i in range(chanel[-1]):
    # hist=cv.calcHist(pic,[i],None,[256],[0,256])
    # plt.plot(hist)
    pass
b1=b-r
r1=b-g
g1=r-b
# cv.imshow('b',b1)
# cv.imshow('g',g1)
# cv.imshow('r',r1)
# cv.imshow('res',pic)
a=sum(sum(b1))
#plt.plot(hist)
print('{0},{1},{3}'.format(sum(b1),sum(r1),sum(g1)))
plt.show()
cv.waitKey(0)
cv.destroyWindow()
