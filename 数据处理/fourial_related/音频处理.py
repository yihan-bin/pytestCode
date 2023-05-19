

import librosa

import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft , ifft
import matplotlib.pylab as mpl
import re
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
filename ='G:\来自余老板的资料\Python测试\数据处理\数据\周笔畅-最美的期待.WAV'
y,sr=librosa.load(filename,sr=None)
print(sr)
print(y)
print(len(y))
temp,beats=librosa.beat.beat_track(y=y,sr=sr)

y_beats=librosa.clicks(frames=beats,sr=sr)

# plt.figure(figsize = ( 12 ,  8 ))
# D  =  librosa.amplitude_to_db(librosa.stft(y), ref = np. max )
# plt.subplot( 4 ,  2 ,  1 )
# librosa.display.specshow(D, y_axis = 'linear' )
# plt.colorbar( format = '%+2.0f dB' )
# plt.title( 'Linear-frequency power spectrogram' )
i=len(y)
x=np.linspace(0,1,i)


############################################################################
plt.figure()
plt.plot(x,y)
plt.title('原始波形图')
plt.figure()
plt.plot(x[0:50],y[0:50])
plt.title('前50组样本')
plt.show()
fft_y=fft(y)
# print(len(fft_y))
# print(fft_y[0:50])
N=1400
x=np.arange(i)
abs_y=np.abs(fft_y)
angle_y=np.angle(fft_y)
plt.figure()
plt.plot(x,abs_y)
plt.title('双边振幅频谱')
plt.figure()
plt.plot(x,angle_y)
plt.title('双边相位谱')
plt.show()