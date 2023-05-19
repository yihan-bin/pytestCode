import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

plt.rcParams['figure.figsize'] = [12, 12]
plt.rcParams.update({'font.size': 18})

dt = 0.001
n = 64
l = 30
dx = l / n
x = np.arange(-l / 2, l / 2, dx, dtype='complex_')
f = np.cos(x) * np.exp(-np.power(x, 2) / 25)
df = -(np.sin(x) * np.exp(-np.power(x, 2) / 25) + (2 / 25) * x * f)

dfFD = np.zeros(len(df), dtype='complex_')
for kappa in range(len(df) - 1):
    dfFD[kappa] = (f[kappa + 1] - f[kappa]) / dx

dfFD[-1] = dfFD[-2]

fhat = np.fft.fft(f)
kappa = (2 * np.pi / l) * np.arange(-n / 2, n / 2)
kappa = np.fft.fftshift(kappa)
dfhat = kappa * fhat * (1j)
dfFFT = np.real(np.fft.ifft(dfhat))

plt.plot(x, df.real, color='k', linewidth=1.5,label='True Derivative')
plt.plot(x, dfFD.real,'--', color='b', linewidth=1.5,label='Finite Diff')
plt.plot(x, dfFFT.real, '--',color='c', linewidth=1.5,label='FFT Derivative')
plt.legend()
plt.show()