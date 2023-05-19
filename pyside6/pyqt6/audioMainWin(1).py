# audioMainWin.py
import sys
from PyQt6.QtWidgets import QWidget, QApplication
from PyQt6 import QtCharts
from PyQt6.QtCore import Qt, QPointF
from audio_Form import Ui_audio_Form
from PyQt6.QtMultimedia import QMediaDevices, QAudioInput, QAudioFormat, QAudioSource


class QmyWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)  # 调用父类构造函数，创建QWidget窗口
        self.__ui = Ui_audio_Form()  # 创建UI对象
        self.__ui.setupUi(self)  # 构造UI界面
        self.sampleCount = 2000
        self.ioDevice = None
        self.create_audio_chart()
        self.setWindowTitle("Python图表制作器")
        self.m_buffer = []

    def create_audio_chart(self):
        self.chart_audio = QtCharts.QChart()
        self.series_audio = QtCharts.QLineSeries()
        self.chart_audio.addSeries(self.series_audio)
        self.chart_audio.legend().hide()
        self.audio_axisX = QtCharts.QValueAxis()
        self.audio_axisX.setRange(0, self.sampleCount)
        self.audio_axisX.setLabelFormat("%g")
        self.audio_axisX.setTitleText("Samples")
        self.audio_axisY = QtCharts.QValueAxis()
        self.audio_axisY.setRange(-1, 1)
        self.audio_axisY.setTitleText("Audio level")
        # 把坐标轴添加到chart中
        self.chart_audio.addAxis(self.audio_axisX, Qt.AlignmentFlag.AlignBottom)
        self.chart_audio.addAxis(self.audio_axisY, Qt.AlignmentFlag.AlignLeft)
        self.series_audio.attachAxis(self.audio_axisX)
        self.series_audio.attachAxis(self.audio_axisY)
        # 创建一个音频输入设备实例
        self.inputDevice = QMediaDevices.defaultAudioInput()
        self.chart_audio.setTitle("Data from the microphone (" + self.inputDevice.description() + ')')
        # 创建一个输入通道
        #self.m_audioInput = QAudioInput(self.inputDevice)
        # 设置音频流参数信息
        self.formatAudio = QAudioFormat()
        self.formatAudio.setSampleRate(8000)
        self.formatAudio.setChannelCount(1)
        self.formatAudio.setSampleFormat(QAudioFormat.SampleFormat.UInt8)
        # 创建一个音频数据接口
        self.m_audioSource = QAudioSource(self.inputDevice, self.formatAudio)
        self.m_audioSource.setBufferSize(200)
        # 创建内建的IODevice实例
        self.ioDevice = self.m_audioSource.start()
        self.ioDevice.readyRead.connect(self.do_IO_readyRead)
        self.__ui.graphicsView.setChart(self.chart_audio)

    def do_IO_readyRead(self):
        # Returns the amount of audio data available to read in bytes.
        bytes = self.m_audioSource.bytesAvailable()
        # Reads at most maxSize bytes from the device, and returns the data read as a QByteArray.
        # 返回列表
        buffer = self.ioDevice.read(bytes)
        # 返回字节的数量
        maxSize = len(buffer)
        # 初始化序列数据
        if(self.m_buffer == []):
            for mm in range(2000):
                self.m_buffer.append(QPointF(mm, 0))
        # 移动曲线
        start = 0
        resolution = 4 
        availableSamples = int(maxSize / resolution)
        if (availableSamples < self.sampleCount):
            start = self.sampleCount - availableSamples
            for s in range(start):
                self.m_buffer[s].setY(self.m_buffer[s+availableSamples].y())

        # 添加新的点
        tmp = 0
        for ss in range(start,self.sampleCount):
            v=buffer[tmp]
            tmp +=resolution
            self.m_buffer[ss].setY((v-128)/128)
            
        self.series_audio.replace(self.m_buffer)


if __name__ == "__main__":
    app = QApplication(sys.argv)  # 创建App，用QApplication类
    myWidget = QmyWidget()
    myWidget.show()
    sys.exit(app.exec())
