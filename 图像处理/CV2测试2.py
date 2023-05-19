import cv2
import cv2 as cv
import numpy as np

pie = cv.imread('data/img.png')
kernel = np.ones((7, 7), np.uint8)
dilate = cv.dilate(pie, kernel, iterations=1)  # 膨胀算法，iterations属于深度大小
erosion = cv.erode(pie, kernel, iterations=1)  # 腐蚀算法，iterations属于深度大小

img = cv.imread('data/zidane.jpg')
kernel = np.ones((5, 5), np.uint8)
# 图像开运算，先腐蚀，在碰撞
opening = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# 图像闭运算，先膨胀，在腐蚀
closing = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)

# 图像礼帽，原始输入-开运算结果
opening = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
# 图像黑帽，闭运算-原始输入
closing = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

img = cv.imread('data/OIP-C.jpg', cv.IMREAD_GRAYSCALE)
sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=3)

sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=3)
sobelx = cv.convertScaleAbs(sobelx)
sobely = cv.convertScaleAbs(sobely)
sobelxy = cv.addWeighted(sobelx, 0.5, sobely, 0.5, 0)

scharrx = cv.Scharr(img, cv.CV_64F, 1, 0)
scharry = cv.Scharr(img, cv.CV_64F, 0, 1)
scharrx = cv.convertScaleAbs(scharrx)
scharry = cv.convertScaleAbs(scharry)
scharrxy = cv.addWeighted(scharrx, 0.5, scharry, 0.5, 0)

laplacian = cv.Laplacian(img, cv.CV_64F)
laplacian = cv.convertScaleAbs(laplacian)

res = np.hstack((sobelxy, scharrxy, laplacian))




v1=cv.Canny(img,80,150)
v2=cv.Canny(img,50,100)

res=np.hstack((v1,v2))

#图像缩放
img=cv.imread('data/zidane.jpg')
up=cv.pyrUp(img)
down=cv.pyrDown(img)
#res=np.hstack((up,down))#图像拼接，行列必须相同

gray=cv.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv.threshold(gray,127,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)

binary,contours,hierarchy=cv.findContours(thresh,cv.RETR_TREE,cv.CHAIN_APPROX_NONE)



cnt=contours[0]#获取第一个轮廓为参数
cv2.contourArea(cnt)#计算轮廓面积
cv.arcLength(cnt,True)#计算轮廓周长，需要闭合轮廓
#近似轮廓，具体用法未知
epsilon=0.1*cv.arcLength(cnt,True)
approx=cv.approxPolyDP(cnt,epsilon.true)

draw_img=img.copy()
res=cv.drawContours(draw_img,[approx],-1,(0,0,255),2)

#求边界矩形
area=cv.contourArea(cnt)
x,y,w,h=cv.boundingRect(cnt)
rect_area=w*h
extent=float(area)/rect_area
print('轮廓面积与边界矩形闭',extent)

#外接圆
(x,y),radius=cv2.minEnclosingCircle(cnt)
center=(int(x),int(y))
radius=int(radius)




draw_img=img.copy()
res=cv.drawContours(draw_img,contours,-1,(9,9,255),2)
cv.imshow('res', res)
cv.waitKey(0)


cv.imshow('res', res)
cv.waitKey(0)
# res = np.hstack((dilate, erosion))  # 图像合并，把两张图像进行合并
#
# cv.imshow('res', res)
# cv.waitKey(0)

cv.destroyWindow()
