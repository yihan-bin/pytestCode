import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#df = pd.read_excel("exportdata/4.csv")
list1 = np.genfromtxt(open("exportdata/4.csv", "rb"), delimiter=",", encoding='GBK')
#height,width = df.shape
#print(height,width,type(df))
average=np.mean(list1)
list_c=list1-[average]*len(list1)
fft_y=np.fft.fft(list_c)

fft_iy=np.fft.ifft(fft_y)
real=fft_y.real
imag=fft_y.imag
for i in range(len(fft_y)):
    if i>50 and i<350:
        fft_y[i].real=0
fft_ty=np.fft.ifft(fft_y)
fft_v=np.abs(fft_y)
plt.figure()
plt.plot(list1)
# plt.figure()
# plt.plot(fft_v)
# plt.figure()
# plt.plot(real)
# plt.figure()
# plt.plot(imag)
plt.figure()
plt.plot(fft_ty)
plt.show()