# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerTRWAwZ.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QSizePolicy,
    QTabWidget, QWidget)
#import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1168, 917)
        MainWindow.setStyleSheet(u"font: \"\u5fae\u8f6f\u96c5\u9ed1\";")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(180, 120, 691, 551))
        self.tabWidget.setStyleSheet(u"\n"
"QTabWidget::pane{\n"
"min-width:70px;\n"
"min-height:25px;\n"
"border-top: 2px solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"\n"
"color: white;\n"
"\n"
"font:16px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"color: #4796f0;\n"
"\n"
"font:13px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 2px solid;\n"
"\n"
"border-color: #4796f0;\n"
"\n"
"}\n"
"blackground::rgb(38, 43, 75)")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2 = QTabWidget(self.tab_2)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(30, 20, 691, 551))
        self.tabWidget_2.setStyleSheet(u"\n"
"QTabWidget::pane{\n"
"min-width:70px;\n"
"min-height:25px;\n"
"border-top: 2px solid;\n"
"\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"\n"
"color: white;\n"
"\n"
"font:16px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"\n"
"\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"\n"
"min-width:70px;\n"
"\n"
"min-height:25px;\n"
"color: #4796f0;\n"
"\n"
"font:13px \"Microsoft YaHei\";\n"
"\n"
"border: 0px solid;\n"
"\n"
"border-bottom: 2px solid;\n"
"\n"
"border-color: #4796f0;\n"
"\n"
"}\n"
"blackground::rgb(38, 43, 75)")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.tabWidget_2.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.label_2 = QLabel(self.tab_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(250, 170, 69, 20))
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tabWidget.addTab(self.tab_2, "")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 70, 1031, 771))
        self.label.setPixmap(QPixmap(u"../image/background.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.tabWidget.raise_()

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Play", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), QCoreApplication.translate("MainWindow", u"Play", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"123", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"\u4ff1\u4e50\u90e8", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u4ff1\u4e50\u90e8", None))
        self.label.setText("")
    # retranslateUi

