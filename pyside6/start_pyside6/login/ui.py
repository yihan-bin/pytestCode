
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTextEdit, QWidget)
#import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(30, 10, 211, 251))
        self.widget.setStyleSheet(u"border-image:url(../image/OI.jpg);\n"
"border-top-left-radius:30px;\n"
"border-bottom-left-radius:30px;")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(240, 10, 271, 251))
        self.widget_2.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"")
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(20, -10, 221, 61))
        self.widget_3.setStyleSheet(u"QPushButton[\n"
"	border:none;\n"
"]\n"
"QPushButton:hover[\n"
"	padding-bottom:5px;\n"
"]")
        self.pushButton = QPushButton(self.widget_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 30, 91, 28))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	padding-bottom:5px;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../image/OIP-C (5).jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton_2 = QPushButton(self.widget_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 30, 91, 28))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"}\n"
"QPushButton:hover{\n"
"	padding-bottom:5px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../image/OIP-C (7).jpg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.label = QLabel(self.widget_2)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 70, 91, 20))
        font = QFont()
        font.setFamilies([u"\u6977\u4f53"])
        font.setPointSize(14)
        self.label.setFont(font)
        self.textEdit = QTextEdit(self.widget_2)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(10, 90, 241, 41))
        self.textEdit.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"")
        self.textEdit_2 = QTextEdit(self.widget_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(10, 140, 241, 41))
        self.textEdit_2.setStyleSheet(u"border:none;\n"
"border-bottom:2px solid rgb(0,0,0);\n"
"")
        self.pushButton_3 = QPushButton(self.widget_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(10, 220, 91, 28))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"	border:2px solidrgb(0, 0, 0);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;\n"
"\n"
"}")
        self.pushButton_4 = QPushButton(self.widget_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(110, 220, 91, 28))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"	background-color:rgb(0, 0, 0);\n"
"	color:rgb(255, 255, 255);\n"
"	border:2px solidrgb(0, 0, 0);\n"
"	border-radius:5px;\n"
"}\n"
"QPushButton:pressed{\n"
"	padding-top:5px;\n"
"	padding-left:5px;\n"
"\n"
"}")
        self.checkBox = QCheckBox(self.widget_2)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(20, 190, 94, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.widget_2.raise_()
        self.widget.raise_()
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 26))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.pushButton_2.clicked.connect(MainWindow.close)
        self.pushButton.clicked.connect(MainWindow.showMinimized)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u6b22\u8fce\u767b\u5f55", None))
        self.textEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.textEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u5bc6\u7801", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u767b\u5f55", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u53d6\u6d88", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u8bb0\u4f4f", None))
    # retranslateUi

