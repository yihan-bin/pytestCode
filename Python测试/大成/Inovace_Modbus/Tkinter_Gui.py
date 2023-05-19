from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import StringVar


import Mobbus_Com as mod
DI_DO=[Label]*7
Machin_num=1
Err_code1=0x952952
Err_code2=0x950950
data=[65531,12,13,14,15,16,17,12,12,1,2,3,4,5]
class DI_Lable():
    def __init__(self,DIn,root,DI_DO_Status=False):
        self.DI = [Label]*16
        if DI_DO_Status:
            Label(root, text='第 {0} 组D0信号'.format(DIn) ,height =3,width=10, justify='left').grid(row=DIn,column=0,columnspan=1)
        else:
            Label(root, text='第 {0} 组DI信号'.format(DIn) , height=3,width=10, justify='left').grid(row=DIn,column=0,columnspan=1)
        for i in range(16):
            self.DI[i] = Label(root, text="DI{0}".format(i), background='gray', foreground='blue',height=1, width=3, justify='left')
            self.DI[i].grid(row=DIn, column=i+1, padx=10, pady=2,columnspan=1)


    def Refreshe(self,para):
        bit=1
        n=0
        for i in range(16):
            bit_n = bit << i
            if (para & bit_n)>0:
                self.DI[i].config(background='Chartreuse')
            else:
                self.DI[i].config(background='gray')
            n=n+1

def Refresh_DI_DO(data):
    DI_1.Refreshe(data[0])
    DI_2.Refreshe(data[1])
    DI_3.Refreshe(data[2])
    DI_4.Refreshe(data[3])
    DI_5.Refreshe(data[4])







root=Tk()
root.resizable(0,0)
root.title('Inovance_PLC_IO_Read_V1.2')
DI_1=DI_Lable(1,root)
DI_2=DI_Lable(2,root)
DI_3=DI_Lable(3,root)
DI_4=DI_Lable(4,root)
DI_5=DI_Lable(5,root)
DO_6=DI_Lable(6,root,True)


def Change_Num(n):
    global Machin_num
    Machin_num=n
    text.set("当前是 {0} 架信号".format(Machin_num))


def datachange():

    # tup_data= Creat_Com.read_data(addr=4899+11*n,data_len=11)
    # global Err_code1, Err_code2
    # Refresh_DI_DO(tup_data)
    # Err_code1 = (tup_data[8] << 16)+(tup_data[7])
    # Err_code2 = (tup_data[10] << 16) + (tup_data[9])
    # text1_errCode.set("伺服一报警代码{:#x}".format(Err_code1))
    # text2_errCode.set("伺服一报警代码{:#x}".format(Err_code2))
    root.after(200, datachange)


A = Button(root, text="一架", command=lambda: Change_Num(1),font=("微软雅黑",15))
A.grid(row=9, column=1, padx=20, pady=20)
B = Button(root, text="二架", command=lambda: Change_Num(2),font=("微软雅黑",15))
B.grid(row=9, column=2, padx=20, pady=20)
C = Button(root, text="三架", command=lambda: Change_Num(3),font=("微软雅黑",15))
C.grid(row=9, column=3, padx=20, pady=20)
D = Button(root, text="四架", command=lambda: Change_Num(4),font=("微软雅黑",15))
D.grid(row=9, column=4, padx=20, pady=20)
E = Button(root, text="五架", command=lambda: Change_Num(5),font=("微软雅黑",15))
E.grid(row=9, column=5, padx=20, pady=20)
#报警代码显示
text1_errCode = StringVar()
text1_errCode.set("伺服一报警代码{:#x}".format(Err_code1))
text2_errCode = StringVar()
text2_errCode.set("伺服二报警代码{:#x}".format(Err_code2))
machine_errCode1 = Label(root,textvariable=text1_errCode, background='AntiqueWhite', foreground='blue', justify='left', padx=5)
machine_errCode1.grid(row=8, column=4, padx=20, pady=20)
machine_errCode2 = Label(root, textvariable=text2_errCode,background='AntiqueWhite', foreground='blue', justify='left', padx=5)
machine_errCode2.grid(row=8, column=5, padx=20, pady=20)

text = StringVar()
text.set("当前是 {0} 架信号".format(Machin_num))
Num_Show = Label(root,textvariable=text, font=("微软雅黑", 16, "italic"),background='gray', foreground='blue', justify='left', padx=5)
Num_Show.grid(row=9, column=0, padx=5, pady=5)





Refresh_DI_DO(data)
#root.after(1000,Refresh_DI_DO)
#root.update()
Creat_Com = mod.Modbus_Com()

Refresh_DI_DO(data)


datachange()
root.mainloop()#进入消息循环

#ex = tk.Label(root, text=Creat_Com.e, background='gray', foreground='blue', justify='left', padx=5)
#ex.grid(row=7, column=0, padx=5, pady=5)

