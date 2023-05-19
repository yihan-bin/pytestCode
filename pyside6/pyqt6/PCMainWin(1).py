# PCMainWin.py
import sys

from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import QtCharts
from PyQt6.QtCore import Qt

from PCMonitor import Ui_PCMonitor
import psutil
from PyQt6.QtCore import QTimer, QDateTime


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗口

        self.__ui = Ui_PCMonitor()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面
        self.create_chart()
        self.set_timer()
        self.setWindowTitle("PC电脑系统监控")

    def create_chart(self):
        self.chart = QtCharts.QChart()
        self.series = QtCharts.QLineSeries()
        self.chart.addSeries(self.series)
        self.chart.legend().hide()

        # 设置坐标轴显示范围
        self.data_axisX = QtCharts.QDateTimeAxis()
        self.value_axisY = QtCharts.QValueAxis()
        self.limitminute = 1  # 设置显示多少分钟内的活动
        self.maxspeed = 100  # 预设y轴最大值
        #Returns a QDateTime object containing a datetime s seconds later than the datetime of this object (or earlier if s is negative).
        self.data_axisX.setMin(QDateTime.currentDateTime().addSecs(-self.limitminute*60))
        self.data_axisX.setMax(QDateTime.currentDateTime().addSecs(0))
        self.value_axisY.setMin(0)
        self.value_axisY.setMax(self.maxspeed)
        self.data_axisX.setFormat("hh:mm:ss")
        # 把坐标轴添加到chart中
        self.chart.addAxis(self.data_axisX, Qt.AlignmentFlag.AlignBottom)
        self.chart.addAxis(self.value_axisY, Qt.AlignmentFlag.AlignLeft)

        # 把曲线关联到坐标轴
        self.series.attachAxis(self.data_axisX)
        self.series.attachAxis(self.value_axisY)
        self.__ui.pcChartView.setChart(self.chart)
        cpucore = psutil.cpu_count(logical=False)
        cpulogical = psutil.cpu_count(logical=True) 
        cpufreq = psutil.cpu_freq()
        self.__ui.label_cpu_core.setText(str(cpucore))
        self.__ui.label_cpu_logicalcore.setText(str(cpulogical))
        self.__ui.label_cpu_freq.setText(str(cpufreq.current/100)+'GHz')

    def set_timer(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.cpuLoad)
        self.timer.start(200)  # 每隔200毫秒出一个点

    def cpuLoad(self):
        current_time = QDateTime.currentDateTime()
        self.data_axisX.setMin(current_time.addSecs(-self.limitminute*60))
        self.data_axisX.setMax(current_time.addSecs(0))
        cpuload = psutil.cpu_percent()
        self.series.append(current_time.toMSecsSinceEpoch(), cpuload)
        if self.series.at(0):
            #Returns the datetime as the number of milliseconds that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (UTC).
            if self.series.at(0).x()<current_time.addSecs(-self.limitminute * 60).toMSecsSinceEpoch():
                self.series.remove(0)
        self.__ui.label_cpu_percent.setText(str(cpuload)+'%')
        


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建App，用QApplication类
    myWidget = QmyWidget()
    myWidget.show()
    sys.exit(app.exec())
