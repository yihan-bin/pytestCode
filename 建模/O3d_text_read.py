import cv2
import numpy as np
import open3d as o3d
import cv2

import time
import pandas as pd

xyz_data=[]
def read_csv_data(file_name):
    df=pd.read_csv(file_name,encoding='ansi')
    data=df.iloc[:,23:]
    data.drop(labels=0)
    data1=data.dropna(axis=0,how='all')
    data2 = data1.dropna(axis=1,how='all' )
    (w,h)=data2.shape
    npdata=np.array(data2)
    print(data2.shape)
    return npdata

def data_to_file(data):
    (w,h)=data.shape
    print(data.shape)
    for i in range(w):
        for j in range(h):
            if not np.isnan(data[i][j]):
                xyz_data.append([i/1000,j/1000,data[i][j]/1000])
    np.savetxt("data/test.xyz", xyz_data, fmt='%f', delimiter=' ')


def show_point_cloud(file_name):
    pcd=o3d.io.read_point_cloud(file_name)
    o3d.visualization.draw([pcd])

if __name__=='__main__':
    rec_data=read_csv_data('data/-1_1234-D_20220623_1.csv')
    data_to_file(rec_data)
    data_com=rec_data.astype(np.uint8)/2
    # cv2.imshow('res',data_com)
    show_point_cloud('data/test.xyz')























