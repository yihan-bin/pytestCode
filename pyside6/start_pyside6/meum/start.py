from ui import *
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6 import QtCore
from PySide6 import QtGui

class loginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)

        #隐藏窗口
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=loginWindow()
    sys.exit(app.exec_())