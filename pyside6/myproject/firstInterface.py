#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：firstInterface.py
@IDE     ：PyCharm 
@Author  ：zw的摸鱼时刻
@Date    ：2023/1/13 15:55 
'''
import sys
from PySide6 import QtCore, QtWidgets, QtGui

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("点这里")

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.showMessage)

    @QtCore.Slot()
    def showMessage(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setText("Hello world")
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        ret = msgBox.exec()

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    app.setStyle(QtWidgets.QStyleFactory.create("Windows"))
    print(QtWidgets.QStyleFactory.keys())
    widget = MyWidget()
    widget.resize(300, 200)
    widget.show()

    sys.exit(app.exec())