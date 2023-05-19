#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：csdn博客.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/1/18 13:52 
'''
import wave

import numpy as np
import pyaudio
import matplotlib.pyplot as plt
import librosa
import librosa.display

#打开WAV文档，文件路径根据需要做修改
wf = wave.open("../data/124.wav", "rb")
#创建PyAudio对象
p = pyaudio.PyAudio()
stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
channels=wf.getnchannels(),
rate=wf.getframerate(),
output=True)
channel=wf.getnchannels()
print(channel)
nframes = wf.getnframes()
framerate = wf.getframerate()
print(nframes,framerate)
wf.close()
x, sr = librosa.load("../data/124.wav", sr=framerate)
print(x.shape, sr)

#原始波形显示
plt.figure(figsize=(14, 5))
librosa.display.waveshow(x, sr=sr)
#快速傅里叶变化频谱图
librosa.__version__
X = librosa.stft(x)
Xdb = librosa.amplitude_to_db(abs(X))   # 把幅度转成分贝格式
plt.figure(figsize=(14, 5))
librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='hz')
plt.colorbar()


n0 = 9000
n1 = 9100
plt.figure(figsize=(14, 5))
plt.plot(x[n0:n1])
plt.grid()










