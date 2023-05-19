import modbus_tk.modbus as mod
import modbus_tk.defines as cst
import modbus_tk.modbus_tcp as modbus_tcp
from tkinter import messagebox
class Modbus_Com:
    def __init__(self):
        # 连接MODBUS TCP从机
        try:
            self.master = modbus_tcp.TcpMaster(host="192.168.1.88")
            self.master.set_timeout(5.0)
            # 读保持寄存器


        except mod.ModbusError as e:
            messagebox.showinfo(title='敬请期待', message=e)
    def read_data(self,addr,data_len):
#        print(addr)
        data = self.master.execute(1, cst.READ_HOLDING_REGISTERS, addr, data_len)
        return data
