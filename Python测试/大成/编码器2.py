import time

import modbus_tk
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
import PyInstaller
import struct
logger = modbus_tk.utils.create_logger("console")
writename = '111.txt'
import datetime
def int2float(a,b):
    f=0
    try:
        z0=hex(a)[2:].zfill(4) #取0x后边的部分 右对齐 左补零
        z1=hex(b)[2:].zfill(4) #取0x后边的部分 右对齐 左补零
        z=z1+z0 #高字节在前 低字节在后
        #z=z0+z1 #低字节在前 高字节在后
        #print (z)
        f=struct.unpack('!f', bytes.fromhex(z))[0] #返回浮点数
    except BaseException as e:
        print(e)
    return f
def text_save(filename,speed,data,data2):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    now_time = datetime.datetime.now()
    da_str=str(data)
    da2_str=str(data2)
    file.writelines(str(now_time)+','+str(speed)+','+da_str+','+da2_str+'\n')

    file.close()

if __name__ == "__main__":
    try:
        # 连接MODBUS TCP从机
        master = modbus_tcp.TcpMaster(host="192.168.1.88")
        master.set_timeout(5.0)
        logger.info("connected")
        # 读保持寄存器4500
        location = 0
        while True:
            start=datetime.datetime.now()
            demo1 = master.execute(1, cst.READ_HOLDING_REGISTERS, 5000, 10)
            print(demo1)
            pre=location

            location=int2float(demo1[2],demo1[3])



            if (location!=pre):
                text_save(writename, demo1[0],demo1[1], location)
                print(location)
            end = datetime.datetime.now()
            print(end - start)

    except modbus_tk.modbus.ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
        input('按任意键退出')
