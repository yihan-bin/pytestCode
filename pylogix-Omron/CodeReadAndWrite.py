#import numpy as np
from pylogix import PLC
import time
comm = PLC()
comm.IPAddress = '192.168.250.1'
filename='AxisID.txt'
def read_err_code(id,index,subindex):
    comm.Write('CoESdoIndex', index)
    comm.Write('CoESdoSubIndex', subindex)
    comm.Write('CoESdoNode', id)
    comm.Write('CoESdoReadEnableT', 2)
    time.sleep(0.2)
    done=comm.Read('CoESdoReadEnable')
    Err=comm.Read('CoESdoReadErr')
    # while not (done.Value[0] or Err.Value[0]) :
    #     done = comm.Read('CoESdoReadEnable')
    #     Err = comm.Read('CoESdoReadErr')
    ret = comm.Read('CoESdoReadData')
    comm.Write('CoESdoReadEnableT', 1)
    comm.Write('CoESdoReadData', 0)

    if id>60:
        pass
    if Err.Value[0]:
        print('{}号电机读取失败'.format(id))
    if ret.Value != 0:
        print('{0}号电机读取数据：{1}'.format(id,ret.Value))

def Write_data(id,index,subindex,data):
    comm.Write('CoESdoIndex', index)
    comm.Write('CoESdoSubIndex', subindex)
    comm.Write('CoESdoNode', id)
    for x in range(len(data)):
        comm.Write('CoESdoSubIndex', subindex+x)
        comm.Write('CoESdoWriteData', data[x])
        comm.Write('CoESdoWriteEnableT', 2)
        time.sleep(0.2)
        err = comm.Read('CoESdoWriteErr')
        comm.Write('CoESdoWriteEnableT', 1)
        # while():
        #     err = comm.Read('CoESdoWriteErr')
        if err.Value[0]:
            print('{0}号电机写入失败，序号：{1}'.format(id,x))




with open(filename, 'r',encoding='utf-8') as f:
    # 将txt中的数据逐行存到列表lines里 lines的每一个元素对应于txt中的一行。然后将每个元素中的不同信息提取出来
    lines = f.readlines()
    # i变量，由于这个txt存储时有空行，所以增只读偶数行，主要看txt文件的格式，一般不需要
    # j用于判断读了多少条，step为画图的X轴
    i = 0
    a=[]
    for line in lines:
        if '#' in line:
            continue
        t = line.replace('\n','').replace('[','').replace(']','').replace('','').split(',')
        #t=[int(x) for x in t]
        if len(t)>1:
            staus=int(t[0])
            axisID=[int(x) for x in t[1].split('-')]
            index=int(t[2])
            subindex=int(t[3])
            if t[-1]=='':
                t.remove('')
            data=list(map(int,t[4:]))
            i=axisID[0]
            if staus==0:
                if len(axisID)>=2 :
                    for i in range(axisID[0],axisID[1]+1):
                        read_err_code(i,index,subindex)
                else:
                    read_err_code(i,index,subindex)
            elif staus==1:
                if len(axisID) >= 2:
                    for i in range(axisID[0],axisID[1]+1):
                        Write_data(i, index, subindex,data)
                else:
                    Write_data(i, index, subindex,data)

        # if len(a)>50:
        #     break
f.close()