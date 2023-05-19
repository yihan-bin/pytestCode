#helloMainWin.py
import sys

from PyQt6.QtWidgets import  QWidget, QApplication
from numpy import var

from calculateWin import Ui_Calculate

class QmyWidget(QWidget): 
   def __init__(self, parent=None):
      super().__init__(parent)   #调用父类构造函数，创建QWidget窗口
      self.label_text=''
      self.edit_text=''
      self.num1=''
      self.num2=''
      self.opt=''
      self.result=''
      self.__ui=Ui_Calculate()   #创建UI对象
      self.__ui.setupUi(self)    #构造UI界面
      self.__ui.lineEdit_op.setText("0")

   def on_pushButton_0_pressed(self):
      self.label_text+='0'
      
      if(self.opt==''):
          self.num1+='0'
          self.edit_text=self.num1
      else:
          self.num2+='0'
          self.edit_text=self.num2

      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_1_pressed(self):
      self.label_text+='1'
      
      if(self.opt==''):
          self.num1+='1'
          self.edit_text=self.num1
      else:
          self.num2+='1'
          self.edit_text=self.num2

      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_2_pressed(self):
      self.label_text+='2'
      if(self.opt==''):
          self.num1+='2'
          self.edit_text=self.num1
      else:
          self.num2+='2'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_3_pressed(self):
      self.label_text+='3'
      if(self.opt==''):
          self.num1+='3'
          self.edit_text=self.num1
      else:
          self.num2+='3'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_4_pressed(self):
      self.label_text+='4'
      if(self.opt==''):
          self.num1+='4'
          self.edit_text=self.num1
      else:
          self.num2+='4'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_5_pressed(self):
      self.label_text+='5'
      if(self.opt==''):
          self.num1+='5'
          self.edit_text=self.num1
      else:
          self.num2+='5'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_6_pressed(self):
      self.label_text+='6'
      if(self.opt==''):
          self.num1+='6'
          self.edit_text=self.num1
      else:
          self.num2+='6'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_7_pressed(self):
      self.label_text+='7'
      if(self.opt==''):
          self.num1+='7'
          self.edit_text=self.num1
      else:
          self.num2+='7'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_8_pressed(self):
      self.label_text+='8'
      if(self.opt==''):
          self.num1+='8'
          self.edit_text=self.num1
      else:
          self.num2+='8'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_9_pressed(self):
      self.label_text+='9'
      if(self.opt==''):
          self.num1+='9'
          self.edit_text=self.num1
      else:
          self.num2+='9'
          self.edit_text=self.num2
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)

   def on_pushButton_pl_pressed(self):
      if(self.num1=='' or self.opt!=''):
          pass
      else:
        self.label_text+='+'
        self.opt='+'
        self.__ui.label_show.setText(self.label_text)

   def on_pushButton_mn_pressed(self):
      if(self.num1=='' or self.opt!=''):
          pass
      else:
        self.label_text+='-'
        self.opt='-'
        self.__ui.label_show.setText(self.label_text)

   def on_pushButton_ml_pressed(self):
      if(self.num1=='' or self.opt!=''):
          pass
      else:
        self.label_text+='x'
        self.opt='x'
        self.__ui.label_show.setText(self.label_text)

   def on_pushButton_md_2_pressed(self):
      if(self.num1=='' or self.opt!=''):
          pass
      else:
        self.label_text+='%'
        self.opt='%'
        self.__ui.label_show.setText(self.label_text)

   def on_pushButton_eq_pressed(self):
      if(self.opt=='+'):
        self.result=str(int(self.num1)+int(self.num2))
      elif(self.opt=='-'):
          self.result=str(int(self.num1)-int(self.num2))
      elif(self.opt=='x'):
          self.result=str(int(self.num1)*int(self.num2))
      elif(self.opt=='%'):
          self.result=str(int(self.num1)/int(self.num2))

      self.label_text=self.label_text+'='+self.result
      self.edit_text = self.result
      self.__ui.lineEdit_op.setText(self.edit_text)
      self.__ui.label_show.setText(self.label_text)
      self.label_text=''
      self.edit_text=''
      self.num1=''
      self.num2=''
      self.opt=''
      self.result=''

   def on_pushButton_ce_clicked(self):
      self.__ui.lineEdit_op.clear()
      self.__ui.label_show.clear()
      self.label_text=''
      self.edit_text=''
      self.num1=''
      self.num2=''
      self.opt=''
      self.result=''

   def on_pushButton_c_pressed(self):
      self.__ui.lineEdit_op.clear()
      self.__ui.label_show.clear()
      self.label_text=''
      self.edit_text=''
      self.num1=''
      self.num2=''
      self.opt=''
      self.result=''

        
    
if  __name__ == "__main__":
   app = QApplication(sys.argv)   #创建App，用QApplication类
   myWidget=QmyWidget()
   myWidget.show()
   sys.exit(app.exec()) 