
import numpy as np
from scipy.io import wavfile
import wave
import matplotlib.pyplot as plt
import librosa.display
"""读取多通道波形并绘制波形图"""

path = 'E:\Spleeter\\out000.mp3'

plt.figure()
# # 音乐文件载入
# audio_path = 'E:\Spleeter\\out005.mp3'
# music, sr = librosa.load(audio_path)
#
# # 宽高比为14:5的图
#
# librosa.display.waveplot(music, sr=sr)
# plt.subplot(4, 1, 1)

# 音乐文件载入
audio_path = 'E:\Spleeter\out016\\vocals.wav'
audio_path = 'noise_1k.wav'
music, sr = librosa.load(audio_path)

# 宽高比为14:5的图

librosa.display.waveplot(music, sr=sr)
# plt.grid()
#
#
#
# plt.subplot(4, 1, 2)
#
# # 音乐文件载入
# audio_path = 'E:\Spleeter\\out015.mp3'
# music, sr = librosa.load(audio_path)
#
# # 宽高比为14:5的图
#
# librosa.display.waveplot(music, sr=sr)
# plt.grid()
#
#
# plt.subplot(4, 1, 3)
#
# # 音乐文件载入
# audio_path = 'E:\Spleeter\\out016.mp3'
# music, sr = librosa.load(audio_path)
#
# # 宽高比为14:5的图
#
# librosa.display.waveplot(music, sr=sr)
# plt.grid()
#
#
#
#
#
# plt.subplot(4, 1, 4)
#
# # 音乐文件载入
# audio_path = 'E:\Spleeter\\out017.mp3'
# music, sr = librosa.load(audio_path)
#
# # 宽高比为14:5的图
#
# librosa.display.waveplot(music, sr=sr)
# plt.grid()




plt.figure()
# 提取音频频谱
spectrogram = librosa.stft(music)

# 将频谱转换为分贝尺度
spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))

# 可视化频谱
librosa.display.specshow(spectrogram_db, sr=sr, x_axis='time', y_axis='log')

# 提取音调
pitch, mag = librosa.piptrack(y=music, sr=sr)

x=np.argmax(mag)
# 获取基本频率
# fundamental_frequency = pitch[np.argmax(mag)]

print(f'基本频率：{x} Hz')


################################################################################################
audio_path = 'vocals.wav'
music, sr = librosa.load(audio_path)
plt.figure()
# 提取音频频谱
spectrogram = librosa.stft(music)

# 将频谱转换为分贝尺度
spectrogram_db = librosa.amplitude_to_db(abs(spectrogram))

# 可视化频谱
librosa.display.specshow(spectrogram_db, sr=sr, x_axis='time', y_axis='log')

# 提取音调
pitch, mag = librosa.piptrack(y=music, sr=sr)

x=np.argmax(mag)
# 获取基本频率
# fundamental_frequency = pitch[np.argmax(mag)]

print(f'基本频率：{x} Hz')



# 显示图
plt.show()