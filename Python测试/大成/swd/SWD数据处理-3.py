import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
import pyecharts.options as opts
from pyecharts.charts import Line
from pyecharts.faker import Faker
list1 = np.genfromtxt(open("../exportdata/222.csv", "rb"), delimiter=",", encoding='GBK')
sorted_data=[]
sorted_datay=[]
x5,x1=[],[]
arrSortedIndex = np.lexsort((list1[:, 1], list1[:, 2]))  # 排序，按照第三列在第四列进行排序
sorted_datax = list1[arrSortedIndex, :]
sorted_datax=np.array(sorted_datax)

for i in range(len(sorted_datax)):
    if sorted_datax[i][2]==5:
        x5.append(sorted_datax[i,:])
    if sorted_datax[i][2]==1:
        x1.append(sorted_datax[i,:])
#         if sorted_datax[i][3]>5600000:
#             sorted_datay.append(sorted_datax[i,:])
#         else:
#             sorted_datay.append(sorted_datax[i, :])
#sorted_datay=np.array(sorted_datay)
print(len(sorted_datax))
np.savetxt("dets.txt", sorted_datax, fmt='%f', delimiter=',')  # 数组保存

Valuex = sorted_datax[:, 3]
Valuex = Valuex * 0.025/1000

dec=[]
#x_base=[]
for i in range(len(Valuex)-1):
    tem=Valuex[i+1]-Valuex[i]
    if tem>0 and tem <1000:
        dec.append(tem)
        sorted_data.append(sorted_datax[i, :])

sorted_data=np.array(sorted_data)
np.savetxt("dets1.txt", sorted_data, fmt='%f', delimiter=',')  # 数组保存
# for i in range(len(dec)):
#     x_base.append(i+1)
x_base=range(1,len(dec),1)

fre = sorted_data[:, 1]
NumNo = sorted_data[:, 2]
Value = sorted_data[:, 3]
Value = Value * 0.025/1000

# a=[1,2,3,4,5,6]
# b=np.numpy(a)

myset = set(NumNo)
count = Counter(NumNo)
print(count[1.0])
no2 = count[1.0]
no3 = no2 + count[2.0]
no4 = no3 + count[3.0]
no5 = no4 + count[4.0]
print(sorted_data[0][2])

A = []




for i in range(count[2.0]):
    for j in range(count[1.0]):
        TEM=Value[no2 + i] - Value[j]
        if ((Value[no2 + i] - Value[j]) > 9.2) and ((Value[no2 + i] - Value[j]) < 9.3):
            A.append(Value[no2 + i] - Value[j])
A1 = np.array(A)
#A1 = sorted(A1)
B = []
for i in range(count[3.0]):
    for j in range(count[2.0]):
        tem=Value[no3 + i] - Value[count[no2]+j]
        #print(count[no2+j])
        if ((Value[no3 + i] - Value[no2+j]) > 58.7) and ((Value[no3 + i] - Value[no2+j]) < 58.9):
            B.append(Value[no3 + i] - Value[no2+j])
B1 = np.array(B)
#B1 = sorted(B1)
C = []
for i in range(count[4.0]):
    for j in range(count[3.0]):
        if ((Value[no4 + i] - Value[no3+j]) > 12.75) and ((Value[no4 + i] - Value[no3+j]) < 13):
            C.append(Value[no4 + i] - Value[no3+j])
C1 = np.array(C)
#C1 = sorted(C1)
D = []
D_i=[]
D_j=[]
for i in range(count[5.0]):
    for j in range(count[4.0]):
        if ((Value[no5 + i] - Value[no4+j]) > 68) and ((Value[no5 + i] - Value[no4+j]) < 69.05):
            D.append(Value[no5 + i] - Value[no4+j])
            D_i.append(i)
            D_j.append(j)

D1 = np.array(D)
#D1 = sorted(D1)

E = []

for i in range(count[5.0]):
    for j in range(count[1.0]):
        if ((Value[no5 + i] - Value[j]) > 149.5) and ((Value[no5 + i] - Value[j]) < 149.8):
            E.append(Value[no5 + i] - Value[j])
            # D_i.append(i)
            # D_j.append(j)

E1 = np.array(E)
#D1 = sorted(D1)

# len_arr=[]
# len_arr.append(len(A1))
# len_arr.append(len(B1))
# len_arr.append(len(C1))
# len_arr.append(len(D1))
# len_arr = sorted(len_arr)
# y = np.zeros([len_arr[-1], 4], dtype=float, order='C')
# y[:len(A1), 0] = A1
# y[:len(B1), 1] = B1
# y[:len(C1), 2] = C1
# y[:len(D1), 3] = D1
# print(y)
np.savetxt("exportdata/1.txt", A1, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("exportdata/2.txt", B1, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("exportdata/3.txt", C1, fmt='%f', delimiter=',')  # 数组保存
np.savetxt("exportdata/4.txt", D1, fmt='%f', delimiter=',')  # 数组保存

# (
#     Line(init_opts=opts.InitOpts(width="1600px", height="800px"))
#     .add_xaxis(xaxis_data=x_base)
#     .add_yaxis(
#         series_name="均最低点",
#         y_axis=dec,
#         markpoint_opts=opts.MarkPointOpts(
#         data=[opts.MarkPointItem(type_="max", name="最大值")],
#         label_opts=opts.LabelOpts(is_show=False),
#         ),
#         markline_opts=opts.MarkLineOpts(
#             data=[
#                 opts.MarkLineItem(type_="average", name="平均值"),
#                 opts.MarkLineItem(symbol="circle", type_="max", name="最高点"),
#             ]
#         ),
#
#     )
#     .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
#     .set_global_opts(
#         title_opts=opts.TitleOpts(title="距离差值", subtitle="zw"),
#         tooltip_opts=opts.TooltipOpts(trigger="axis"),
#         toolbox_opts=opts.ToolboxOpts(is_show=True),
#         xaxis_opts=opts.AxisOpts( boundary_gap=True),
#     )
#     .render("temperature_change_line_chart.html")
# )
print(count)
plt.figure()
plt.plot(A1)
plt.figure()
plt.plot(B1)
plt.figure()
plt.plot(C1)
plt.figure()
plt.plot(D1)
# plt.figure()
# plt.plot(E1)
plt.figure()
plt.plot(dec)
plt.figure()
plt.plot(D_i)
plt.figure()
plt.plot(D_j)
np.savetxt("exportdata/5.txt", D1, fmt='%f', delimiter=',')  # 数组保存
plt.show()

