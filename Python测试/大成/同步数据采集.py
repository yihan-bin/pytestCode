import time

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import struct
import os
logger = modbus_tk.utils.create_logger("console")
file_path = os.getcwd()
file_c = os.listdir(file_path)
writename = str(len(file_c) + 1) + '-111.txt'
demo1=[]
pre=[0,1,2,3,4,0,1,2,3,4,0,1,2,3,4,]
z=['','','','',]
k=1
import datetime
encoderValue=[1,2,3,4,5,1,2,3,4,5,1,2,3,4,5,]
for i in range(60):
    demo1.append(i)
def int4Lint(a):
    f=0
    z1=''
    try:
        for k in range(4):
            z=hex(a[-k-1])[2:].zfill(4) #取0x后边的部分 右对齐 左补零
            z1=z1+z
        f=struct.unpack('!q', bytes.fromhex(z1))[0] #返回浮点数
    except BaseException as e:
        f=e
    return f
def int4Real(a):
    f=0
    z1=''
    try:
        for k in range(4):
            z=hex(a[-k-1])[2:].zfill(4) #取0x后边的部分 右对齐 左补零
            z1=z1+z
        f=struct.unpack('!d', bytes.fromhex(z1))[0] #返回浮点数
    except BaseException as e:
        f=e
    return f
def text_save(filename,datas,n):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    now_time = datetime.datetime.now()
    file.writelines(str(now_time) + ',' + str(n+1) + ',' )
    for i in range(3):
        file.writelines(str(datas[n+i*5])+',')
    file.writelines('\n')
    file.close()

if __name__ == "__main__":
    try:
        # 连接MODBUS TCP从机
        master = modbus_tcp.TcpMaster(host="192.168.1.88")
        master.set_timeout(5.0)
        logger.info("connected")
        # 读保持寄存器4500
        location = 0
        file = open(writename, 'a')
        file.writelines('时间' + ','  + '架号' + ',' + '趟数' +',' + '起始位置' +',' + '中止位置' + '\n')
        file.close()
        while True:
            start=datetime.datetime.now()
            demo1 = master.execute(1, cst.READ_HOLDING_REGISTERS, 5100, 60)
            if pre!=demo1:
                for i in range(15):
                    if i<5 :
                        encoderValue[i] = int4Lint(demo1[0+4*i: 4+4 * i])
                    else:
                        encoderValue[i] = int4Real(demo1[0 + 4 * i: 4 + 4 * i])

            if k>5000:
                file = open(writename, 'a')
                file.writelines('时间' + ',' + '架号' + ',' + '趟数' + ',' + '起始位置' + ',' + '中止位置' + '\n')
                file.close()
                file_path=os.getcwd()
                file_c=os.listdir(file_path)
                writename=str(len(file_c)+1)+'-111.txt'
                k=0
            if (demo1!=pre):
                for i in range(5):
                    if encoderValue[i]!=pre[i]:
                        k=i
                        text_save(writename, encoderValue,k)
                        print(encoderValue)
            end = datetime.datetime.now()
            #print(end - start)
            pre = [x for x in encoderValue]
    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
        input('按任意键退出')
