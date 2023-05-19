# ChartMainWin.py
import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import QtCharts, QtGui
from PyQt6.QtCore import Qt,QPointF

from pythonChart import Ui_pythonChart


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗口

        self.__ui = Ui_pythonChart()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面
        self.series1 = QtCharts.QLineSeries()
        self.series2 = QtCharts.QLineSeries()
        self.data_axisX = QtCharts.QValueAxis()
        self.value_axisY = QtCharts.QValueAxis()
        self.minX = 0
        self.maxX = 100
        self.minY = 0
        self.maxY = 100
        self.lab1 = ''
        self.lab2 = ''
        self.create_area_chart()

        self.setWindowTitle("Python图表制作器")

    def on_pushButton_setX_clicked(self):
        self.minX = self.__ui.doubleSpinBox_minX.value()
        self.maxX = self.__ui.doubleSpinBox_maxX.value()
        # 设置坐标轴显示范围
        self.data_axisX.setMin(self.minX)
        self.data_axisX.setMax(self.maxX)

    def on_pushButton_setY_clicked(self):
        self.minY = self.__ui.doubleSpinBox_minY.value()
        self.maxY = self.__ui.doubleSpinBox_maxY.value()
        
        self.value_axisY.setMin(self.minY)
        self.value_axisY.setMax(self.maxY)

    def on_pushButton_setSeries1_pressed(self):
        self.series1.append(self.__ui.doubleSpinBox_series1X.value(
        ), self.__ui.doubleSpinBox_series1Y.value())
        self.lab1 += '('+str(self.__ui.doubleSpinBox_series1X.value()) + \
            ','+str(self.__ui.doubleSpinBox_series1Y.value())+')'+"\n"
        self.__ui.label_series1.setText(self.lab1)

    def on_pushButton_setSeries2_pressed(self):
        self.series2.append(self.__ui.doubleSpinBox_series2X.value(
        ), self.__ui.doubleSpinBox_series2Y.value())
        self.lab2 += '('+str(self.__ui.doubleSpinBox_series2X.value()) + \
            ','+str(self.__ui.doubleSpinBox_series2Y.value())+')'+"\n"
        self.__ui.label_series2.setText(self.lab2)

    def on_pushButton_clear_clicked(self):
        self.__ui.doubleSpinBox_minX.setValue(0)
        self.__ui.doubleSpinBox_maxX.setValue(0)
        self.__ui.doubleSpinBox_minY.setValue(0)
        self.__ui.doubleSpinBox_maxY.setValue(0)
        self.__ui.doubleSpinBox_series1X.setValue(0)
        self.__ui.doubleSpinBox_series2X.setValue(0)
        self.__ui.doubleSpinBox_series1Y.setValue(0)
        self.__ui.doubleSpinBox_series2Y.setValue(0)
        self.__ui.label_series1.setText('')
        self.__ui.label_series2.setText('')
        self.minX = 0
        self.maxX = 100
        self.minY = 0
        self.maxY = 100
        self.lab1 = ''
        self.lab2 = ''
        self.series1.clear()
        self.series2.clear()
        self.data_axisX.setMin(self.minX)
        self.data_axisX.setMax(self.maxX)
        self.value_axisY.setMin(self.minY)
        self.value_axisY.setMax(self.maxY)

    def create_area_chart(self):
        self.chart = QtCharts.QChart()
        self.chart.addSeries(self.series1)
        self.chart.addSeries(self.series2)
        self.chart.legend().hide()

        # 把坐标轴添加到chart中
        self.chart.addAxis(self.data_axisX, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.value_axisY, Qt.AlignmentFlag.AlignLeft)

        # 把曲线关联到坐标轴
        self.series1.attachAxis(self.data_axisX)
        self.series1.attachAxis(self.value_axisY)
        self.series2.attachAxis(self.data_axisX)
        self.series2.attachAxis(self.value_axisY)
        self.series = QtCharts.QAreaSeries(self.series1,self.series2)
        
        self.chart.addSeries(self.series)
        self.series.attachAxis(self.data_axisX)
        self.series.attachAxis(self.value_axisY)
        self.pen = QtGui.QPen(0x059605)
        self.pen.setWidth(3)
        self.series.setPen(self.pen)
        # self.series1.setPen(self.pen)
        # self.pen2 = QtGui.QPen(Qt.GlobalColor.blue)
        # self.pen2.setWidth(16)
        # self.series2.setPen(self.pen2)
        self.gradient = QtGui.QLinearGradient(QPointF(0, 0), QPointF(0, 1))
        self.gradient.setColorAt(0.0, 0x3cc63c)
        self.gradient.setColorAt(1.0, 0x26f626)
        self.gradient.setCoordinateMode(QtGui.QGradient.CoordinateMode.ObjectBoundingMode)
        self.series.setBrush(self.gradient)

        self.__ui.graphicsView.setChart(self.chart)
        self.__ui.graphicsView.setRenderHint(QtGui.QPainter.RenderHint.Antialiasing)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建App，用QApplication类
    myWidget = QmyWidget()
    myWidget.show()
    sys.exit(app.exec())
