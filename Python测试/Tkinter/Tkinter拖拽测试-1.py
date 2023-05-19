import tkinter
from tkinter.messagebox import showinfo
from tkinter import Label
import windnd

def drag_files(files):
    msg='\n'.join((item.decode('gbk') for item in files))
    #showinfo('你拖放的文件',msg)
    label = Label(tk, text=msg, font=('宋体', 5, 'bold italic'), bg="#7CCD7C",
                     # 设置标签内容区大小
                     width=30, height=5,
                     # 设置填充区距离、边框宽度和其样式（凹陷式）
                     padx=10, pady=15, borderwidth=10, relief="sunken")
    label.pack()

tk=tkinter.Tk()
windnd.hook_dropfiles(tk,func=drag_files)

tk.mainloop()





