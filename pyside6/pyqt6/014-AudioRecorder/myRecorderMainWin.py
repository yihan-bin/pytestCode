from ast import If, Pass
from PyQt6.QtWidgets import QMainWindow,QApplication,QFileDialog
from audiorecorder import Ui_AudioRecorder
import sys
from PyQt6.QtMultimedia import QMediaRecorder,QMediaCaptureSession,QAudioInput,QMediaDevices,\
    QMediaFormat,QImageCapture,QAudioDevice
from PyQt6.QtCore import Qt,pyqtSlot,QVariant,QUrl

class AudioRecorder(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_AudioRecorder()
        self.ui.setupUi(self)
        self.setWindowTitle("录音机")
        self.m_audioRecorder = QMediaRecorder(self)
        self.m_captureSession = QMediaCaptureSession()
        self.m_captureSession.setRecorder(self.m_audioRecorder)
        self.m_audioInput = QAudioInput(self)
        self.m_captureSession.setAudioInput(self.m_audioInput)
        self.m_outputLocationSet = False
        self.m_updatingFormats = False

        #audio devices
        default = QMediaDevices.defaultAudioInput()
        self.ui.audioDeviceBox.addItem("default",QVariant(default))
        devices = QMediaDevices.audioInputs()
        for device in devices:
            self.ui.audioDeviceBox.addItem(device.description(),QVariant(device))
        
        #audio codecs and container formats
        self.updateFormats()
        self.ui.audioCodecBox.currentIndexChanged.connect(self.updateFormats)
        self.ui.containerBox.currentIndexChanged.connect(self.updateFormats)

        #sample rate
        self.ui.sampleRateBox.setRange(self.m_captureSession.audioInput().device().minimumSampleRate(),\
            self.m_captureSession.audioInput().device().maximumSampleRate())
        qmax = max(self.m_captureSession.audioInput().device().minimumSampleRate(),\
            max(self.m_captureSession.audioInput().device().maximumSampleRate(),44100))
        self.ui.sampleRateBox.setValue(qmax)

        #channels
        self.ui.channelsBox.addItem("Default",QVariant(-1))
        self.ui.channelsBox.addItem("1",QVariant(1))
        self.ui.channelsBox.addItem("2",QVariant(2))
        self.ui.channelsBox.addItem("4",QVariant(4))

        #quality
        self.ui.qualitySlider.setRange(0,QImageCapture.Quality.VeryHighQuality.value)
        self.ui.qualitySlider.setValue(QImageCapture.Quality.NormalQuality.value)

        #bit rates:
        self.ui.bitrateBox.addItem("Default",QVariant(0))
        self.ui.bitrateBox.addItem("32000",QVariant(32000))
        self.ui.bitrateBox.addItem("64000",QVariant(64000))
        self.ui.bitrateBox.addItem("96000",QVariant(96000))
        self.ui.bitrateBox.addItem("128000",QVariant(128000))

        self.m_audioRecorder.durationChanged.connect(self.updateProgress)
        self.m_audioRecorder.recorderStateChanged.connect(self.onStateChanged)
        self.m_audioRecorder.errorChanged.connect(self.displayErrorMessage)
    
    def displayErrorMessage(self):
        self.ui.statusbar.showMessage(self.m_audioRecorder.errorString())

    def updateProgress(self,duration):
        if (self.m_audioRecorder.error() != QMediaRecorder.Error.NoError or duration < 2000):
            return True
        self.ui.statusbar.showMessage("Recorded "+str(duration/1000))

    def boxValue(self,box):
        idx = box.currentIndex()
        if (idx == -1):
            return QVariant()
        return QVariant(box.itemData(idx))

    def onStateChanged(self,state):
        statusMessage = ''
        if state == QMediaRecorder.RecorderState.RecordingState:
            statusMessage = "Recording to"+str(self.m_audioRecorder.actualLocation())
            self.ui.recordButton.setText("Stop")
            self.ui.pauseButton.setText("Pause")
        elif state == QMediaRecorder.RecorderState.PausedState:
            statusMessage = "Pause"
            self.ui.recordButton.setText("Stop")
            self.ui.pauseButton.setText("Resume")
        elif state == QMediaRecorder.RecorderState.StoppedState:
            statusMessage = "Stopped"
            self.ui.recordButton.setText("Record")
            self.ui.pauseButton.setText("Pause")
        if (self.m_audioRecorder.recorderState() != QMediaRecorder.RecorderState.StoppedState):
            self.ui.pauseButton.setEnabled(True)
        if (self.m_audioRecorder.error() == QMediaRecorder.Error.NoError):
            self.ui.statusbar.showMessage(statusMessage)

    def setOutputLocation(self):
        fileName = QFileDialog.getSaveFileName()
        self.m_audioRecorder.setOutputLocation(QUrl.fromLocalFile(fileName[0]))
        self.m_outputLocationSet = True

    def toggleRecord(self):
        if (self.m_audioRecorder.recorderState() == QMediaRecorder.RecorderState.StoppedState):
            self.m_captureSession.audioInput().setDevice(QAudioDevice(self.boxValue(self.ui.audioDeviceBox).value()))
            self.m_audioRecorder.setMediaFormat(self.selectedMediaFormat())
            self.m_audioRecorder.setAudioSampleRate(self.ui.sampleRateBox.value())
            self.m_audioRecorder.setAudioBitRate(int(self.boxValue(self.ui.bitrateBox).value()))
            self.m_audioRecorder.setAudioChannelCount(int(self.boxValue(self.ui.channelsBox).value()))
            self.m_audioRecorder.setQuality(QMediaRecorder.Quality(self.ui.qualitySlider.value()))
            if (self.ui.constantQualityRadioButton.isChecked()):
                encodermode = QMediaRecorder.EncodingMode.ConstantQualityEncoding
            else:
                encodermode = QMediaRecorder.EncodingMode.ConstantBitRateEncoding
            self.m_audioRecorder.setEncodingMode(encodermode)
            self.m_audioRecorder.record()
        else:
            self.m_audioRecorder.stop()
    
    def selectedMediaFormat(self):
        format = QMediaFormat()
        format.setFileFormat(self.boxValue(self.ui.containerBox).value())
        format.setAudioCodec(self.boxValue(self.ui.audioCodecBox).value())
        return format

    def togglePause(self):
        if (self.m_audioRecorder.recorderState() != QMediaRecorder.RecorderState.PausedState):
            self.m_audioRecorder.pause()
        else:
            self.m_audioRecorder.record()

    def updateFormats(self):
        if (self.m_updatingFormats):
            return True
        self.m_updatingFormats = True
        format = QMediaFormat()
        if (self.ui.containerBox.count()):
            format.setFileFormat(self.boxValue(self.ui.containerBox).value())
        if (self.ui.audioCodecBox.count()):
            format.setAudioCodec(self.boxValue(self.ui.audioCodecBox).value())
        
        currentIndex = 0
        self.ui.audioCodecBox.clear()
        default = QVariant(QMediaFormat.AudioCodec.Unspecified).value()
        self.ui.audioCodecBox.addItem("Default audio codec",default)
        for codec in format.supportedAudioCodecs(QMediaFormat.ConversionMode.Encode):
            if(codec == format.audioCodec()):
                currentIndex = self.ui.audioCodecBox.count()
            self.ui.audioCodecBox.addItem(QMediaFormat.audioCodecDescription(codec),QVariant(codec).value())
        self.ui.audioCodecBox.setCurrentIndex(currentIndex)

        currentIndex = 0
        self.ui.containerBox.clear()
        self.ui.containerBox.addItem("Default file format", QVariant(QMediaFormat.FileFormat.UnspecifiedFormat).value())
        for container in format.supportedFileFormats(QMediaFormat.ConversionMode.Encode):
            if(container.value < QMediaFormat.FileFormat.Mpeg4Audio.value):
                pass
            if(container == format.fileFormat()):
                currentIndex = self.ui.containerBox.count()
            self.ui.containerBox.addItem(QMediaFormat.fileFormatDescription(container),QVariant(container).value())
        self.ui.containerBox.setCurrentIndex(currentIndex)

        self.m_updatingFormats = False

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWidget = AudioRecorder()
    myWidget.show()
    sys.exit(app.exec())
