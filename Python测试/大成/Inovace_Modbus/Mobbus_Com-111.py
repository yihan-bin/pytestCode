import modbus_tk.modbus as mod
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
from tkinter import messagebox


class Modbus_Com:
    def __init__(self):
        # 连接MODBUS TCP从机
        while True:
            if self._con():
                print('连接成功')
                return 1
            else:
                print('连接失败')

    def _con(self):
        try:
            self.master = modbus_tcp.TcpMaster(host="192.168.1.88")
            self.master.set_timeout(5)
            # 读保持寄存器


        except mod.ModbusError as e:
            print('连接失败')
            messagebox.showinfo(title='敬请期待', message=e)
            return -1

    def read_data(self, addr, data_len):
        #        print(addr)
        data = self.master.execute(1, cst.READ_HOLDING_REGISTERS, addr, data_len)
        return data

    def write_data(self, addr, data_len):
        master.execute(1, cst.WRITE_MULTIPLE_REGISTERS, 370, output_value=[20, 21, 22, 23])


test = Modbus_Com()
test()
