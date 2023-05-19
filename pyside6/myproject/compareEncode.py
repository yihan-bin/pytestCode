#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：compareEncode.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/13 17:03 
'''
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiFsqxrc.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import sys
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
QMetaObject, QObject, QPoint, QRect, Slot,QSize, QTime, QUrl, Qt)
# from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
#     QFont, QFontDatabase, QGradient, QIcon,
#     QImage, QKeySequence, QLinearGradient, QPainter,
#     QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QListWidget,
QListWidgetItem, QPushButton, QSizePolicy, QWidget, QFileDialog, QTableWidget, QTableWidgetItem)
from pathlib import Path


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(582, 385)
        self.compareEnter = QPushButton(Form)
        self.compareEnter.setObjectName(u"compareEnter")
        self.compareEnter.setGeometry(QRect(20, 190, 75, 24))
        self.openFile = QPushButton(Form)
        self.openFile.setObjectName(u"openFile")
        self.openFile.setGeometry(QRect(20, 70, 75, 24))
        self.FilePath = QLabel(Form)
        self.FilePath.setObjectName(u"FilePath")
        self.FilePath.setGeometry(QRect(140, 50, 311, 31))
        self.FilePath.setFrameShape(QFrame.StyledPanel)
        self.FilePath.setFrameShadow(QFrame.Raised)
        self.FilePath.setLineWidth(1)
        self.FilePath.setMidLineWidth(1)
        self.tableWidget = QTableWidget(Form)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(150, 170, 356, 192))

        self.retranslateUi(Form)
        self.openFile.clicked.connect(Form.openFile)
        self.compareEnter.clicked.connect(Form.startCompare)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.compareEnter.setText(QCoreApplication.translate("Form", u"\u5bf9\u6bd4", None))
        self.openFile.setText(QCoreApplication.translate("Form", u"\u6253\u5f00\u6587\u4ef6", None))
        self.FilePath.setText(QCoreApplication.translate("Form", u"", None))
    # retranslateUi


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.centralWidget = QWidget()
        self.ui = Ui_Form()  # 实例化UI对象
        self.ui.setupUi(self)  # 初始化

    @Slot()  # 槽函数用它装饰
    def openFile(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        print("openFile")
        FILE = Path(__file__).resolve()
        ROOT = FILE.parents[0]  # YOLOv5 root directory
        filePath = QFileDialog.getOpenFileName(
            self.centralWidget,  # 父窗口对象
            "选择存储路径",  # 标题
            str(ROOT)  # 起始目录
        )
        self.FilePath = self.ui.FilePath
        self.strpath = filePath[0]
        self.FilePath.setText(self.strpath)

    @Slot()  # 槽函数用它装饰
    def startCompare(self):
        print('startCompare')
        filename = '../data/2.txt'
        self.tableWidget = self.ui.tableWidget
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)

        dq_type = 'eq', 'er', 'EQ', 'ER', 'Eq', 'Er', 'eR', 'eQ'
        f = open(filename, encoding='utf-8')
        context = f.read()
        boms = context.split('\t')
        encoding_extrat = []
        for i in range(len(boms)):
            if boms[i][:2] in dq_type:
                encoding_extrat.append([[boms[i]], [boms[i + 1]], [boms[i + 2]]])
        for i in range(10):
            a=''.join(encoding_extrat[i][0])
            b=''.join(encoding_extrat[i][1])
            c=''.join(encoding_extrat[i][2])
            item1 = QTableWidgetItem(a)
            item2 = QTableWidgetItem(b)
            item3 = QTableWidgetItem(c)
            self.tableWidget.setItem(i, 0, item1)
            self.tableWidget.setItem(i, 1, item2)
            self.tableWidget.setItem(i, 2, item3)

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())
