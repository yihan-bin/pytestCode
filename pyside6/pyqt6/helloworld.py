import sys
from PyQt6 import QtWidgets,QtGui

if __name__ == '__main__':
    app =  QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QWidget()
    win.resize(560,500)
    win.setWindowTitle("hello world")
    win.setWindowIcon(QtGui.QIcon('cal.png'))
    lab = QtWidgets.QLabel(win)
    lab.setText("我的第一个程序。")
    size = lab.sizeHint()
    print(size.width(),size.height())
    lab.setGeometry(100,50,size.width(),size.height())
    # print(lab.text())
    # tmp =  win.windowTitle()
    # print(tmp)
    win.show()
    sys.exit(app.exec())