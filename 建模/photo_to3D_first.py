import cv2
import numpy as np
import open3d as o3d

import time


class point_cloud_generator():
    def __init__(self,rgb_file,depth_file,save_ply,camera_intrinsics=[785.0,779.0,649.0,405.0]):
        self.rgb_file=rgb_file
        self.depth_file=depth_file
        self.save_ply=save_ply

        self.rgb=cv2.imread(rgb_file)
        self.depth=cv2.imread(self.depth_file,-1)
        print('your depth image shape is:',self.depth_file)

        self.width=self.rgb.shape[1]
        self.height=self.rgb.shape[0]

        self.camera_intrinsics=camera_intrinsics
        self.depth_scale=1000
    def compute(self):
        t1=time.time()
        depth=np.asarray(self.depth,dtype=np.uint16).T

        self.Z=depth/self.depth_scale
        fx,fy,cx,cy=self.camera_intrinsics

        X=np.zeros((self.width,self.height))
        Y=np.zeros((self.width,self.height))
        for i in range(self.width):
            X[i,:]=np.full(X.shape[1],i)

        self.X=((X-cx/2)*self.Z)/fx
        for i in range(self.height):
            Y[:,i]=np.full(Y.shape[0],i)
        self.Y=((Y-cy/2)*self.Z)/fy

        data_ply=np.zeros((6,self.width*self.height))
        data_ply[0]=self.X.T.reshape(-1)
        data_ply[1] = self.Y.T.reshape(-1)
        data_ply[2] = self.Z.T.reshape(-1)
        img=np.array(self.rgb,dtype=np.uint8)
        data_ply[3] = img[:,:,0:1].reshape(-1)
        data_ply[4] = img[:,:,1:2].reshape(-1)
        data_ply[5] = img[:,:,2:3].reshape(-1)
        self.data_ply=data_ply
        t2=time.time()
        print('calculate 3D point cloud Done.',t2-t1)
    def write_ply(self):
        start=time.time()
        float_formatter=lambda x:"%.4f"%x
        points=[]
        for i in self.data_ply.T:
            points.append("{}{}{}{}{}{} 0\n".format(
                float_formatter(i[0]),format(i[1]),float_formatter(i[2]),
                int(i[3]),int(i[4]),int(i[5])))
        file=open(self.save_ply,'w')
        file.write('''ply
            format ascii 1.0
            element vertex %d
            property float x
            property float y
            property float z
            property uchar red
            property uchar green
            property uchar blue
            property uchar alpha
            end_header
            %s
            '''%(len(points),"".join(points)))
        file.close()
        end=time.time()
        print('write into .piy file done.',end-start)
    def show_point_cloud(self):
        pcd=o3d.io.read_point_cloud(self.save_ply)
        o3d.visualization.draw([pcd])

if __name__=='__main__':
    camera_intrinsics=[378.998657,378.639863,321.935120,240.766663]
    rgb_file='data/1.jpeg'
    depth_file='data/1.png'
    save_ply='data.ply'
    a=point_cloud_generator(rgb_file,depth_file,save_ply,camera_intrinsics)
    a.compute()
    a.write_ply()
    a.show_point_cloud()
    pcd = o3d.io.read_point_cloud('data/te.pcd')
    o3d.visualization.draw([pcd])























