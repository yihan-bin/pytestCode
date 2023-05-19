import cv2
import cv2 as cv
import numpy as np

img=cv.imread('data/zidane.jpg')
template=cv.imread('data/OIP-C.jpg')
#模板匹配
res=cv.matchTemplate(img,template,cv.TM_SQDIFF)
#可能匹配到多个模板，需要自己筛选和
methods=['cv.TM_CCOEFF','cv.TM_CCOEFF_NORMED','cv.TM_CCORR',
         'cv.TM_CCORR_NORMED','cv.TM_SQDIFF','cv.TM_SQDIFF_NORMED']


min_val,max_val,min_loc,max_loc=cv.minMaxLoc(res)

# #模板匹配筛选
# threshold=0.8#筛选阈值
# loc=np.where(res>=threshold)
# for pt in zip(*loc[::-1]):
#     bottom_right=(pt[0]+w,pt[1]+h)
#     #cv2.rectangle(img)#画矩形框
#

#图像特征，拐角检测，交点检测

img=cv.imread('data/zidane.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

dst=cv.cornerHarris(gray,2,3,0.004)
img[dst>0.01*dst.max()]=[0,0,255]
cv.imshow('dst',img)
cv.waitKey(0)



















