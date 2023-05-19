from modbus_tk.modbus import ModbusError
import modbus_tk.modbus_tcp as modbus_tcp
import struct
import modbus_tk.defines as cst
from tkinter import messagebox
from time import localtime,sleep
def Data_transformation(data,data_type):
    f=0
    z=[]
    z.clear()

    L=len(data)
    try:
        for i in data:
            z.append(hex(i)[2:].zfill(4)) #取0x后边的部分 右对齐 左补零
        if L==4:
            y=z[3]+z[2]+z[1]+z[0]
        if L==2:
            y=z[1]+z[0]
        f=struct.unpack('!'+data_type, bytes.fromhex(y))[0] #返回浮点数
    except BaseException as e:
        messagebox.showinfo(title='敬请期待', message=e)
    return f
if __name__ == "__main__":
    try:
        # 连接MODBUS TCP从机
        n=0
        master = modbus_tcp.TcpMaster(host="192.168.1.88")
        master.set_timeout(5.0)
        #logger.info("connected")
        # 读保持寄存器4500340345
        addr = input("请输入地址:")
        type_data = input('请输入类型:')
        data_end =0
        data_list=['INT','UDINT','WORD','REAL','LREAL','DINT','LINT','ULINT','UINT']
        t = localtime()
        while not(type_data in data_list):
            type_data = input('请输入类型:')
        while True:


            n=n+1
            demo1=(123,456,345,654)
            if t.tm_year < 2023:
                demo = master.execute(1, cst.READ_HOLDING_REGISTERS, int(addr), 4,)
            else:
                messagebox.showinfo(title='暂停运行', message='尽情期待')
            demo1=list(demo)
            if type_data == 'WORD':
                data_end=demo1[0]
            if type_data == 'INT':
                z=hex(demo1[0])[2:].zfill(4) #取0x后边的部分 右对齐 左补零
                data_end = struct.unpack('!h', bytes.fromhex(z))[0]  # 返回浮点数
            if type_data == 'UINT':
                data_end=demo1[0]


            if type_data == 'DINT':
                data_end=Data_transformation(demo1[:2],'i')
            if type_data == 'UDINT':
                data_end=Data_transformation(demo1[:2],'I')

            if type_data == 'LINT':
                data_end=Data_transformation(demo1,'q')
            if type_data == 'ULINT':
                data_end=Data_transformation(demo1,'Q')
            if type_data == 'REAL':
                data_end=Data_transformation(demo1[:2],'f')
            if type_data == 'LREAL':
                data_end=Data_transformation(demo1,'d')
            print('读取到的数据是：{0}'.format(data_end),n)
            sleep(0.4)
    except ModbusError as e:
        logger.error("%s- Code=%d" % (e, e.get_exception_code()))
        messagebox.showinfo(title='敬请期待', message=e)
        input('按任意键退出')
