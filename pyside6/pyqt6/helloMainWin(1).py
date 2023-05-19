#helloMainWin.py
import sys

from PyQt6.QtWidgets import  QWidget, QApplication

from helloWin import Ui_Form

class QmyWidget(QWidget): 
   def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建QWidget窗口

      self.__ui=Ui_Form()   #创建UI对象
      self.__ui.setupUi(self)    #构造UI界面
      self.Lab="Welcome to QmyWidget"
      self.__ui.label.setText(self.Lab)
        
    
if  __name__ == "__main__":
   app = QApplication(sys.argv)   #创建App，用QApplication类

   myWidget=QmyWidget()
   myWidget.show()
   sys.exit(app.exec()) 