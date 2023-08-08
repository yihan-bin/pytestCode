# file: combobox.py
#!/usr/bin/python

"""
ZetCode PyQt6 tutorial

This example shows how to use
a QComboBox widget.

Author: Jan Bodnar
Website: zetcode.com
"""

import sys
import re
import time
from threading import Thread
from PyQt6.QtWidgets import (QWidget, QLabel,
        QComboBox, QApplication,QLineEdit,QTextEdit,QPushButton)
from socket import socket,SHUT_RDWR
from PyQt6.QtCore import QThread,pyqtSignal
from struct import pack,unpack
FunctionCode=0x00
readData=[]
class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.lbl = QLabel('1', self)
        self.lbl.move(250, 30)
        self.Flbl = QLabel('功能', self)
        self.Flbl.move(20,50)
        self.Albl = QLabel('站号', self)
        self.Albl.move(20,20)
        self.Albl = QLabel('地址', self)
        self.Albl.move(20,80)
        self.Albl = QLabel('数量', self)
        self.Albl.move(20,110)

        Fcombo = QComboBox(self)
        Fcombo.addItem('0x读取线圈')
        Fcombo.addItem('1x读取输入状态')
        Fcombo.addItem('4x读保持寄存器')
        Fcombo.addItem('3x读输入寄存器')
        Fcombo.move(50, 50)
        Fcombo.textActivated[str].connect(self.onActivated)


        self.QtextOutput=QTextEdit(self)
        self.QtextOutput.setGeometry(20,20,450,300)
        self.QtextOutput.move(40,140)


        self.btn1 = QPushButton("清空文本框", self)
        self.btn1.move(280, 50)
        self.btn2 = QPushButton("开始读取", self)
        self.btn2.move(400, 50)
        self.btn3 = QPushButton("停止读取", self)
        self.btn3.move(400, 80)
        self.btn1.clicked.connect(self.buttonClick1)
        self.btn2.clicked.connect(self.buttonClick2)
        self.btn3.clicked.connect(self.buttonClick3)



        self.node = QLineEdit(self)
        self.node.setText('9')
        self.node.move(50, 20)
        self.addrInput = QLineEdit(self)
        self.addrInput.setText('1000')
        self.addrInput.move(50, 80)
        self.NumInput = QLineEdit(self)
        self.NumInput.setText('4')
        self.NumInput.move(50, 110)
        self.setGeometry(300, 300, 500, 450)
        self.setWindowTitle('QComboBox')
        self.show()


    def onActivated(self, text):


        FunctionCode=re.findall(r"\d+\.?\d*",text)
        self.lbl.setText(FunctionCode[0])
        self.lbl.adjustSize()

    def buttonClick1(self):
        self.QtextOutput.clear()

    def buttonClick2(self):
        data=[]
        data.append(self.node.text())
        data.append(self.lbl.text())
        data.append(self.addrInput.text())
        data.append(self.NumInput.text())
        # print(data)
        self.btn2.setEnabled(False)

        self.QtextOutput.clear()

        self.testThread = MyThread()
        self.testThread.setDaemon(True)  # 设为保护线程，主进程结束会关闭线程

        self.testThread.setParm(data)
        self.testThread.start()  # 开始线程
        #self.testThread.join()


    def buttonClick3(self):
        self.QtextOutput.clear()
        self.testThread.setFlag(False)      #修改线程运行状态
        self.btn2.setEnabled(True)
        del self.testThread

class ConServe(socket):
    def __init__(self):
        super().__init__()
        self.sk=socket()
    def connectServe(self,ip,port):
        self.sk.connect((ip,port))
    def sendData(self,data):
        self.sk.send(data)
        # self.sk.setblocking(False)
    def recData(self):
        return self.sk.recv(1024)
    def closeCon(self):

        # self.sk.shutdown(SHUT_RDWR)
        self.sk.close()
        time.sleep(0.2)




class MyThread(Thread):
    def __init__(self):
        super().__init__()
        self.Flag = True  # 停止标志位
        # 自行添加参数
        self.sk=ConServe()
        self.sk.connectServe('192.168.250.16',8008)

    def run(self):
        while (True):
            if (not self.Flag):
                self.sk.closeCon()
                break
            else:
                global readData
                time.sleep(2)
                print(self.sendData)
                self.sk.sendData(self.sendData)
                recData=self.sk.recData()
                recLen=len(recData)
                if recLen>6:
                    print(recData)
                    print("总共接收到的数据：{0}".format(recLen))
                    recCrc16=pack('>H',ModbusCrc16(recData[:recLen-2]))

                    readData.clear()
                    # print(recCrc16)

                    # print(len(recData[1:3]))
                    datalen=int(unpack('<b', recData[2:3])[0]/2)
                    print("接受到的数据长度是：{0}".format(datalen))
                    if datalen>0 and datalen%2==0:
                        for i in range(datalen):
                            readData.append(unpack('>h',recData[i*2+3:i*2+5])[0])
                        print(readData)
                    #print(hex(recData[recLen-2:]))
                    print('*'*50)


    def setFlag(self, parm):  # 外部停止线程的操作函数
        self.Flag = parm  # boolean

    def setParm(self, parm):  # 外部修改内部信息函数
        print(parm)
        self.sendData=pack('<b', int(parm[0]))
        self.sendData += pack('<b', int(parm[1]))
        self.sendData += pack('>h', int(parm[2]))
        self.sendData += pack('>h', int(parm[3]))
        self.sendData +=pack('>H',ModbusCrc16(self.sendData))
        for data in self.sendData:
            print(data)

    def __del__(self):
        self.sk.closeCon()

    def getParm(self):  # 外部获得内部信息函数
        return self.Parm


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())

def ModbusCrc16(strData):
    # datas=list(strData)
    crc16=0xFFFF
    poly=0xA001
    for data in strData:
        a=int(hex(data),16)
        crc16=a^crc16
        for i in range(8):
            if 1&(crc16)==1:
                crc16=crc16>>1
                crc16=crc16^poly
            else:
                crc16=crc16>>1
    crc17=crc16
    crc16=hex(int(crc16))
    crc16=crc16[2:].upper()
    length=len(crc16)
    high=crc16[0:length-2].zfill(2)
    high=str(high)
    low=crc16[length-2:length].zfill(2)
    low=str(low)
    print("校验码地位"+low.upper())
    print("校验码高位",high.upper())
    return crc17


if __name__ == '__main__':
    main()