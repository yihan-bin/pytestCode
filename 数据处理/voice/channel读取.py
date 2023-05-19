#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：channel读取.py
@IDE     ：PyCharm 
@Author  ：zwProject
@Date    ：2023/2/10 10:57 
'''
import wave


import pyaudio


#打开WAV文档，文件路径根据需要做修改
wf = wave.open("../data/124.wav", "r")
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