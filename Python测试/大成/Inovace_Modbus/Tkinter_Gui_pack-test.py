from tkinter import Tk
from tkinter import Label
from tkinter import Button
from tkinter import StringVar
from tkinter import Frame
from time import localtime
from tkinter import messagebox

import Mobbus_Com as mod
DI_DO=[Label]*7
Machin_num=1
Err_code1=0x952952
Err_code2=0x950950
data=[65531,12,13,14,15,16,17,12,12,1,2,3,4,5,7,8,5]
bit=[1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192,16384,32768]
data_pre=[0,0,0,0,0,0,0,0,0,0,0]
class DI_Lable():
    def __init__(self,DIn,root,DI_DO_Num=6):
        self.DI=[]
        fm = []
        for i in range(DI_DO_Num):
            self.DI_tem1 = [Label] * 16
            self.DI.append(self.DI_tem1)
            fm_tem = Frame(root)
            fm.append(fm_tem)
        for x in range(DI_DO_Num):

            if x==DI_DO_Num-1:
                Label(fm[x], text='第 {0} 组D0信号'.format(x+1) ,height =1,width=10, justify='left').pack(padx=3,pady=0,anchor='w')
            else:
                Label(fm[x], text='第 {0} 组DI信号'.format(x+1) , height=1,width=10, justify='left').pack(padx=3,pady=0,anchor='w')
            for i in range(16):
                if x == DI_DO_Num - 1:
                    self.DI[x][i] = Label(fm[x], text="DO{0}".format(i), background='gray', foreground='blue',height=1, width=3, justify='left',font=('Arial', 8))
                    self.DI[x][i].pack(side='left',padx=3,pady=0)
                else:
                    self.DI[x][i] = Label(fm[x], text="DI{0}".format(i), background='gray', foreground='blue', height=1, width=3, justify='left',font=('Arial', 8))
                    self.DI[x][i].pack(side='left', padx=3, pady=0)
            fm[x].pack()


    def Refreshe(self,para):

        global bit,data_pre
        if data_pre==para:
            pass
        else:
            for i in range(16):
                if bit[i]&para[0]>0:
                    self.DI[0][i].config(background='Chartreuse')
                else:
                    self.DI[0][i].config(background='gray')
                if bit[i]&para[1]>0:
                    self.DI[1][i].config(background='Chartreuse')
                else:
                    self.DI[1][i].config(background='gray')
                if bit[i]&para[2]>0:
                    self.DI[2][i].config(background='Chartreuse')
                else:
                    self.DI[2][i].config(background='gray')
                if bit[i]&para[3]>0:
                    self.DI[3][i].config(background='Chartreuse')
                else:
                    self.DI[3][i].config(background='gray')
                if bit[i]&para[4]>0:
                    self.DI[4][i].config(background='Chartreuse')
                else:
                    self.DI[4][i].config(background='gray')
                if bit[i] & para[5] > 0:
                    self.DI[5][i].config(background='Chartreuse')
                else:
                    self.DI[5][i].config(background='gray')
        data_pre = para

def Refresh_DI_DO(data):
    t=localtime()
    if t.tm_year<2023:
        DI_1.Refreshe(data)
    else:
        messagebox.showinfo(title='暂停运行', message='尽情期待')








root=Tk()
root.resizable(0,0)
root.title('Inovance_PLC_IO_Read_V2.2')
root.iconbitmap('ino.ico')
DI_1=DI_Lable(1,root)



def Change_Num(n):
    global Machin_num
    Machin_num=n
    text.set("当前是 {0} 架信号".format(Machin_num))


def datachange():
    global Machin_num
    tup_data= Creat_Com.read_data(addr=4890+20*Machin_num,data_len=11)
    global Err_code1, Err_code2,data
    Refresh_DI_DO(tup_data)
    Err_code1 = (tup_data[8] << 16)+(tup_data[7])
    Err_code2 = (tup_data[10] << 16) + (tup_data[9])
    text1_errCode.set("伺服一报警代码{:#x}".format(Err_code1))
    text2_errCode.set("伺服一报警代码{:#x}".format(Err_code2))
    root.after(50, datachange)



text = StringVar()
text.set("当前是 {0} 架信号".format(Machin_num))
Num_Show = Label(root,textvariable=text, font=("微软雅黑", 16, "italic"),background='gray', foreground='blue', justify='left', padx=5)
Num_Show.pack( padx=5, pady=5)


#报警代码显示
text1_errCode = StringVar()
text1_errCode.set("伺服一报警代码{:#x}".format(Err_code1))
text2_errCode = StringVar()
text2_errCode.set("伺服二报警代码{:#x}".format(Err_code2))
#定义报警显示控件
errcode_Fm=Frame(root)
machine_errCode1 = Label(errcode_Fm,textvariable=text1_errCode, background='AntiqueWhite', foreground='blue', justify='left', padx=5)
machine_errCode1.pack( padx=20, pady=10)
machine_errCode2 = Label(errcode_Fm, textvariable=text2_errCode,background='AntiqueWhite', foreground='blue', justify='left', padx=5)
machine_errCode2.pack( padx=20, pady=10)
errcode_Fm.pack(anchor='center')
#定义按键控件和显示
but_Frm=Frame(root)
A = Button(but_Frm, text="一架", command=lambda: Change_Num(1),font=("微软雅黑",15))
A.pack(side='left',padx=20, pady=10)
B = Button(but_Frm, text="二架", command=lambda: Change_Num(2),font=("微软雅黑",15))
B.pack(side='left',padx=20, pady=10)
C = Button(but_Frm, text="三架", command=lambda: Change_Num(3),font=("微软雅黑",15))
C.pack(side='left',padx=20, pady=10)
D = Button(but_Frm, text="四架", command=lambda: Change_Num(4),font=("微软雅黑",15))
D.pack(side='left',padx=20, pady=10)
E = Button(but_Frm, text="五架", command=lambda: Change_Num(5),font=("微软雅黑",15))
E.pack(side='left',padx=20, pady=10)
but_Frm.pack(anchor='center')







Refresh_DI_DO(data)
#root.after(1000,Refresh_DI_DO)
#root.update()
Creat_Com = mod.Modbus_Com()

Refresh_DI_DO(data)



datachange()
root.mainloop()#进入消息循环

#ex = tk.Label(root, text=Creat_Com.e, background='gray', foreground='blue', justify='left', padx=5)
#ex.grid(row=7, column=0, padx=5, pady=5)

