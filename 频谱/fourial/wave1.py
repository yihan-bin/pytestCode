import wave

import numpy as np
import pyaudio
import numpy
import matplotlib.pyplot as pl

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
#读取完整的帧数据到str_data中，这是一个string类型的数据
str_data = wf.readframes(nframes*2)
wf.close()
#将波形数据转换为数组
# A new 1-D array initialized from raw binary or text data in a string.
wave_data = numpy.fromstring(str_data, dtype=numpy.short,count = -1)
# #将wave_data数组改为2列，行数自动匹配。在修改shape的属性时，需使得数组的总长度不变。
# wave_data.shape = -1,2
# #将数组转置
# wave_data = wave_data.T
#time 也是一个数组，与wave_data[0]或wave_data[1]配对形成系列点坐标
f=open("../data/124.wav",'rb')
data=f.read()
time = numpy.arange(0,nframes)*(1.0/framerate)
wave_data = np.reshape(wave_data,[nframes,channel])
#绘制波形图
pl.plot(time, wave_data)
# pl.subplot(212)
# pl.plot(time[1], wave_data[1], c="g")
pl.xlabel("time (seconds)")
pl.show()
#
# 采样点数，修改采样点数和起始位置进行不同位置和长度的音频波形分析
N=44100
start=0 #开始采样位置
df = framerate/(N-1) # 分辨率
x=df*N
freq = [df*n for n in range(0,N)] #N个元素
wave_data2=wave_data[start:start+N]
c=numpy.fft.fft(wave_data2)*2/N
#常规显示采样频率一半的频谱
d=int(len(c)/2)
#仅显示频率在4000以下的频谱
# while freq[d]>4000:
# d-=10
pl.plot(freq[:d-1],abs(c[:d-1]),'r')
pl.show()
