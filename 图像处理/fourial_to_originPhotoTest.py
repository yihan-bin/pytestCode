import cv2
import numpy as np
import matplotlib.colors
from scipy import signal
import time
import open3d as o3d

# 读取图片
# file_name='xyz.xyz'
# file_name='xyz.xyzrgb'
file_name = 'data/xyz.xyzn'
img = cv2.imread('data/OIP-C.jpg')
img_1 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# 彩色图像均衡化 需要分解通道 对每一个通道均衡化
(b, g, r) = cv2.split(img)
###########公式一小数形式, YUV   (  U∈[-0.5-0.5]  ,   R，G，B∈[0,1]  )
# y = 0.299 * r + 0.587 * g + 0.114 * b
# u = -0.147 * r - 0.289 *g - 0.436 * b
# v = 0.615 - 0.515 * g - 0.100 * b
#############公式2
y = 0.299 * r + 0.587 * g + 0.114 * b
v = -0.169 * r- 0.331 * g + 0.500 * b
u = 0.500 * r - 0.439 * g - 0.081 * b
bH = cv2.equalizeHist(b)
gH = cv2.equalizeHist(g)
rH = cv2.equalizeHist(r)
y = y.astype(np.uint8)
# a=((y == img_1))
# cv2.imshow("img_1",y)
# # 合并每一个通道
# result = cv2.merge((bH, gH, rH))
# #test = cv2.merge(y, u, v)
# cv2.imshow("Input", img)
# cv2.imshow("Result", result)
# #cv2.imshow("Result", test)
# 等待显示
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# plt.show()
# # 绘制直方图
# plt.figure("Hist")
# # 蓝色分量
# plt.hist(bH.ravel(), bins=256, density=True, facecolor='b', edgecolor='b')
# # 绿色分量
# plt.hist(gH.ravel(), bins=256, density=True, facecolor='g', edgecolor='g')
# # 红色分量
# plt.hist(rH.ravel(), bins=256, density=True, facecolor='r', edgecolor='r')
# plt.xlabel("x")
# plt.ylabel("y")
# plt.show()

y_freq = np.fft.fft2(y)
y_shiftfreq = np.fft.fftshift(y_freq)
(w, h) = y_freq.shape
sig = 20
v1 = signal.gaussian(w, sig)
v2 = signal.gaussian(h, sig)
kernel = 1 - np.outer(v1, v2)
y_shiftfreq1 = y_shiftfreq * kernel
img_freq = np.fft.ifft2(np.fft.ifftshift(y_shiftfreq1))
img_freq = img_freq.astype(np.uint8)

r = (img_freq + 1.400*v - 0.7).astype(np.uint8)
g = (img_freq - 0.343*u - 0.711*v + 0.526).astype(np.uint8)
b = (img_freq + 1.765*u - 0.883).astype(np.uint8)
##################test_return小数形式, YUV   (  U∈[-0.5-0.5]  ,   R，G，B∈[0,1]  )
# r=(y+1.140*v).astype(np.uint8)
# g=(y-0.395*u-0.581*v).astype(np.uint8)
# b=(y+2.032*u).astype(np.uint8)
# ###################公式2
# r = (y + 1.400*v - 0.7).astype(np.uint8)
# g = (y - 0.343*u - 0.711*v + 0.526).astype(np.uint8)
# b = (y + 1.765*u - 0.883).astype(np.uint8)
img_yuv_to_rgb = np.empty(shape=(w, h, 3), dtype=np.uint8)
img_yuv_to_rgb2 = []
# img_rgb=zip(b,g,r)
# img_rgb=list(img_rgb)
# img_rgb1=np.array(img_rgb)
# img_yuv_to_rgb=np.array(img_yuv_to_rgb)
j = 0
temp = [0, 0, 0]
start = time.time()
for b_1, g_1, r_1 in zip(b, g, r):
    for i in range(h):
        # temp[0]=b_1[i]
        # temp[1] = g_1[i]
        # temp[2] = r_1[i]
        # img_yuv_to_rgb[j][i].append(temp)
        img_yuv_to_rgb[j][i][0] = b_1[i]
        img_yuv_to_rgb[j][i][1] = g_1[i]
        img_yuv_to_rgb[j][i][2] = r_1[i]

    j += 1
##########TEst_optimize############
print(time.time() - start)
j = 0
m = 0
temp = [0, 0, 0]
start = time.time()
test_o3d = []
for b_1, g_1, r_1 in zip(b, g, r):
    m = 0
    temp_arr = []
    for b_2, g_2, r_2 in zip(b_1, g_1, r_1):
        temp_arr.append([r_2, g_2, b_2])
        test_o3d.append([r_2, g_2, b_2])
    # print(m)
    img_yuv_to_rgb2.append(temp_arr)
    j += 1
img_yuv_to_rgb2 = np.array(img_yuv_to_rgb2)
print(time.time() - start)
x = []
##########################测试色彩
# for i in range(255):
#     m=0
#     temp_arr=[]
#     for j in range(255):
#         temp_arr.append([0,i,j])
#         #test_o3d.append([b_2, g_2, r_2])
#     #print(m)
#     x.append(temp_arr)
# x=np.array(x).astype(np.uint8)
# cv2.imshow('rgb',x)
# cv2.waitKey(0)
a = 0
data = []
##################显示处理
y_shiftfreq_abs = np.abs(y_shiftfreq1)
for i in range(w):
    for j in range(h):
        data.append([i / w, y_shiftfreq_abs[i][j] / w / h * 10, j / h, y_shiftfreq_abs[i][j] / w / h * 10, 0, y_shiftfreq_abs[i][j] / w / h] * 10)
        if a < y_shiftfreq_abs[i][j] / w / h:
            a = y_shiftfreq_abs[i][j] / w / h

np.savetxt(file_name, data, fmt="%.2f", delimiter=' ')

radius = 0.01  # 搜索半径
max_nn = 30
pcd = o3d.io.read_point_cloud(file_name)
t=time.time()
img3 = cv2.merge([r,g,b])
print(time.time()-t)
# o3d.visualization.draw([pcd],point_show_normal = True)
# pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius, max_nn))
# o3d.visualization.draw_geometries([pcd], point_show_normal=True)
cv2.imshow('rgb', img_yuv_to_rgb2)
cv2.imshow('img3', img3)
cv2.waitKey(0)
