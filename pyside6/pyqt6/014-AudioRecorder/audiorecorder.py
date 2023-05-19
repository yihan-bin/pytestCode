# Form implementation generated from reading ui file 'audiorecorder.ui'
#
# Created by: PyQt6 UI code generator 6.2.3
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_AudioRecorder(object):
    def setupUi(self, AudioRecorder):
        AudioRecorder.setObjectName("AudioRecorder")
        AudioRecorder.resize(546, 471)
        self.centralwidget = QtWidgets.QWidget(AudioRecorder)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.recordButton = QtWidgets.QPushButton(self.centralwidget)
        self.recordButton.setObjectName("recordButton")
        self.gridLayout_3.addWidget(self.recordButton, 2, 1, 1, 1)
        self.outputButton = QtWidgets.QPushButton(self.centralwidget)
        self.outputButton.setObjectName("outputButton")
        self.gridLayout_3.addWidget(self.outputButton, 2, 0, 1, 1)
        self.pauseButton = QtWidgets.QPushButton(self.centralwidget)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout_3.addWidget(self.pauseButton, 2, 2, 1, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 3, 0, 1, 1)
        self.audioDeviceBox = QtWidgets.QComboBox(self.centralwidget)
        self.audioDeviceBox.setObjectName("audioDeviceBox")
        self.gridLayout_2.addWidget(self.audioDeviceBox, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 2, 0, 1, 1)
        self.containerBox = QtWidgets.QComboBox(self.centralwidget)
        self.containerBox.setObjectName("containerBox")
        self.gridLayout_2.addWidget(self.containerBox, 2, 1, 1, 1)
        self.audioCodecBox = QtWidgets.QComboBox(self.centralwidget)
        self.audioCodecBox.setObjectName("audioCodecBox")
        self.gridLayout_2.addWidget(self.audioCodecBox, 1, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 4, 0, 1, 1)
        self.channelsBox = QtWidgets.QComboBox(self.centralwidget)
        self.channelsBox.setObjectName("channelsBox")
        self.gridLayout_2.addWidget(self.channelsBox, 4, 1, 1, 1)
        self.sampleRateBox = QtWidgets.QSpinBox(self.centralwidget)
        self.sampleRateBox.setObjectName("sampleRateBox")
        self.gridLayout_2.addWidget(self.sampleRateBox, 3, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 3)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.constantQualityRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.constantQualityRadioButton.setChecked(True)
        self.constantQualityRadioButton.setObjectName("constantQualityRadioButton")
        self.gridLayout.addWidget(self.constantQualityRadioButton, 0, 0, 1, 2)
        self.qualitySlider = QtWidgets.QSlider(self.groupBox)
        self.qualitySlider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.qualitySlider.setObjectName("qualitySlider")
        self.gridLayout.addWidget(self.qualitySlider, 1, 1, 1, 1)
        self.constantBitrateRadioButton = QtWidgets.QRadioButton(self.groupBox)
        self.constantBitrateRadioButton.setObjectName("constantBitrateRadioButton")
        self.gridLayout.addWidget(self.constantBitrateRadioButton, 2, 0, 1, 2)
        self.bitrateBox = QtWidgets.QComboBox(self.groupBox)
        self.bitrateBox.setEnabled(False)
        self.bitrateBox.setObjectName("bitrateBox")
        self.gridLayout.addWidget(self.bitrateBox, 3, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 1, 0, 1, 3)
        AudioRecorder.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AudioRecorder)
        self.statusbar.setObjectName("statusbar")
        AudioRecorder.setStatusBar(self.statusbar)

        self.retranslateUi(AudioRecorder)
        self.constantQualityRadioButton.toggled['bool'].connect(self.qualitySlider.setEnabled) # type: ignore
        self.constantBitrateRadioButton.toggled['bool'].connect(self.bitrateBox.setEnabled) # type: ignore
        self.outputButton.clicked.connect(AudioRecorder.setOutputLocation) # type: ignore
        self.recordButton.clicked.connect(AudioRecorder.toggleRecord) # type: ignore
        self.pauseButton.clicked.connect(AudioRecorder.togglePause) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(AudioRecorder)

    def retranslateUi(self, AudioRecorder):
        _translate = QtCore.QCoreApplication.translate
        AudioRecorder.setWindowTitle(_translate("AudioRecorder", "MainWindow"))
        self.recordButton.setText(_translate("AudioRecorder", "Record"))
        self.outputButton.setText(_translate("AudioRecorder", "Output..."))
        self.pauseButton.setText(_translate("AudioRecorder", "Pause"))
        self.label_4.setText(_translate("AudioRecorder", "Sample rate:"))
        self.label_2.setText(_translate("AudioRecorder", "Audio Codec:"))
        self.label.setText(_translate("AudioRecorder", "Input Device:"))
        self.label_3.setText(_translate("AudioRecorder", "File Container:"))
        self.label_5.setText(_translate("AudioRecorder", "Channels:"))
        self.groupBox.setTitle(_translate("AudioRecorder", "Encoding Mode:"))
        self.constantQualityRadioButton.setText(_translate("AudioRecorder", "Constant Quality:"))
        self.constantBitrateRadioButton.setText(_translate("AudioRecorder", "Constant Bitrate:"))