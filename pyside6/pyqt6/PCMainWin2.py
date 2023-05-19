# PCMainWin2.py
import sys

from PyQt6.QtWidgets import QWidget, QApplication, QLabel
from PyQt6 import QtCharts
from PyQt6.QtCore import Qt,QStringListModel
from matplotlib.style import use

from PCMonitor2 import Ui_Form
import psutil
from PyQt6.QtCore import QTimer, QDateTime


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗口

        self.__ui = Ui_Form()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面
        self.create_chart_cpu()
        self.set_timer_cpu()

        self.create_chart_mem()
        self.set_timer_mem()

        self.create_chart_disk()

        self.setWindowTitle("PC电脑系统监控")

    def create_chart_cpu(self):
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
        self.__ui.pcChartView_cpu.setChart(self.chart)
        cpucore = psutil.cpu_count(logical=False)
        cpulogical = psutil.cpu_count(logical=True) 
        cpufreq = psutil.cpu_freq()
        self.__ui.label_cpu_core_2.setText(str(cpucore))
        self.__ui.label_cpu_logical.setText(str(cpulogical))
        self.__ui.label_cpu_freq_2.setText(str(cpufreq.current/100)+'GHz')

    def set_timer_cpu(self):
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
        self.__ui.label_cpu_percent_2.setText(str(cpuload)+'%')
    
    def create_chart_mem(self):
        self.chart_mem = QtCharts.QChart()
        self.series_mem = QtCharts.QLineSeries()
        self.chart_mem.addSeries(self.series_mem)
        self.chart_mem.legend().hide()

        # 设置坐标轴显示范围
        self.data_axisX_mem = QtCharts.QDateTimeAxis()
        self.value_axisY_mem = QtCharts.QValueAxis()
        self.limitminute_mem = 1  # 设置显示多少分钟内的活动
        self.maxspeed_mem = 100  # 预设y轴最大值
        #Returns a QDateTime object containing a datetime s seconds later than the datetime of this object (or earlier if s is negative).
        self.data_axisX_mem.setMin(QDateTime.currentDateTime().addSecs(-self.limitminute_mem*60))
        self.data_axisX_mem.setMax(QDateTime.currentDateTime().addSecs(0))
        self.value_axisY_mem.setMin(0)
        self.value_axisY_mem.setMax(self.maxspeed_mem)
        self.data_axisX_mem.setFormat("hh:mm:ss")
        # 把坐标轴添加到chart中
        self.chart_mem.addAxis(self.data_axisX_mem, Qt.AlignmentFlag.AlignBottom)
        self.chart_mem.addAxis(self.value_axisY_mem, Qt.AlignmentFlag.AlignLeft)

        # 把曲线关联到坐标轴
        self.series_mem.attachAxis(self.data_axisX_mem)
        self.series_mem.attachAxis(self.value_axisY_mem)
        self.__ui.pcChartView_mem.setChart(self.chart_mem)

    def set_timer_mem(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.memLoad)
        self.timer.start(200)  # 每隔200毫秒出一个点

    def memLoad(self):
        current_time = QDateTime.currentDateTime()
        self.data_axisX_mem.setMin(current_time.addSecs(-self.limitminute_mem*60))
        self.data_axisX_mem.setMax(current_time.addSecs(0))
        meminfo = psutil.virtual_memory()
        self.series_mem.append(current_time.toMSecsSinceEpoch(), meminfo.percent)
        if self.series_mem.at(0):
            #Returns the datetime as the number of milliseconds that have passed since 1970-01-01T00:00:00.000, Coordinated Universal Time (UTC).
            if self.series_mem.at(0).x()<current_time.addSecs(-self.limitminute_mem * 60).toMSecsSinceEpoch():
                self.series_mem.remove(0)
        self.__ui.label_mem_percent.setText(str(meminfo.percent)+'%')
        self.__ui.label_mem_total.setText(bytes2human(meminfo.total))
        self.__ui.label_mem_available.setText(bytes2human(meminfo.available))
        self.__ui.label_mem_used.setText(bytes2human(meminfo.used))

    def create_chart_disk(self):
        self.set0 = QtCharts.QBarSet('used')
        self.set1 = QtCharts.QBarSet('free')
        self.series_disk = QtCharts.QPercentBarSeries()
        
        self.chart_disk = QtCharts.QChart()
        self.chart_disk.addSeries(self.series_disk)
        self.chart_disk.legend().hide()
        self.chart_disk.setTitle("磁盘使用情况")
        #访问枚举类型：类+枚举名+枚举变量
        self.chart_disk.setAnimationOptions(QtCharts.QChart.AnimationOption.SeriesAnimations)

        self.categories = QStringListModel()
        mydisk = psutil.disk_partitions()
        disk_list = []
        diskstr = ''
        for dk in mydisk:
            disk_list.append(dk.device[0]+'盘')
            usage = psutil.disk_usage(dk.device)
            self.set0.append(usage.used)
            self.set1.append(usage.free)
            self.lab_disk = QLabel(self.__ui.frame_disk)
            #diskstr = dk.device[0]+'盘:'+'容量'+bytes2human(usage.total)
            diskstr = diskstr+dk.device[0]+'盘:'+'总容量'+bytes2human(usage.total)+' 已用'+bytes2human(usage.used)\
                +' 未用'+bytes2human(usage.free)+' 占比'+str(usage.percent)+'%'+'\n'
            self.lab_disk.setText(diskstr)
        
        self.series_disk.append(self.set0)
        self.series_disk.append(self.set1)

        self.categories.setStringList(disk_list)
        self.axisX_disk = QtCharts.QBarCategoryAxis()
        self.axisX_disk.append(disk_list)
        self.axisY_disk = QtCharts.QValueAxis()

        # 把坐标轴添加到chart中
        self.chart_disk.addAxis(self.axisX_disk, Qt.AlignmentFlag.AlignBottom)
        self.chart_disk.addAxis(self.axisY_disk, Qt.AlignmentFlag.AlignLeft)

        # 把曲线关联到坐标轴
        self.series_disk.attachAxis(self.axisX_disk)
        self.series_disk.attachAxis(self.axisY_disk)

        self.__ui.pcChartView_disk.setChart(self.chart_disk)
        

def bytes2human(n):
    symbols = ('K','M','G','T','P','E','Z','Y')
    prefix = {}
    for i,s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10
    for s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' % (value,s)
    return '%sB' % n


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        ui = ui_login.Ui_Form()  # 实例化UI对象
        ui.setupUi(self)  # 初始化

    @QtCore.Slot()  # 槽函数用它装饰
    def login(self):  # 在Qt Designer中为登录按钮命名的槽函数；
        print("你点击了登录")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec())