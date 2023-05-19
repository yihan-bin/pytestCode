import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
import matplotlib.cm as cm
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import axes3d

plt.rcParams['figure.figsize'] = [12, 12]
plt.rcParams.update({'font.size': 18})

a = 1
n = 1000
l = 100
dx = l / n
x = np.arange(-l / 2, l / 2, dx)

kappa = 2 * np.pi * np.fft.fftfreq(n, d=dx)

u0 = np.zeros_like(x)
u0[int((l / 2 - l / 10) / dx):int((l / 2 + l / 10) / dx)] = 1
u0hat = np.fft.fft(u0)
tem_re=u0hat.real
tem_im=u0hat.imag
u0hat_ri = np.concatenate((tem_re, tem_im))

dt = 0.1
t = np.arange(0, 10, dt)


def rhsHeat(uhat_ri, t, kappa, a):
    uhat = uhat_ri[:n] + (1j) * uhat_ri[n:]
    d_uhat = -a ** 2 * (np.power(kappa, 2)) * uhat
    d_uhat_ri = np.concatenate((d_uhat.real, d_uhat.imag)).astype('float64')
    return d_uhat_ri


uhat_ri = odeint(rhsHeat, u0hat_ri, t, args=(kappa, a))
uhat = uhat_ri[:, :n] + (1j) * uhat_ri[:, n:]
u = np.zeros_like(uhat)
for k in range(len(t)):
    u[k, :] = np.fft.ifft(uhat[k, :])

u = u.real

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
plt.set_cmap('jet_r')
u_plot = u[0:-1:10, :]

for j in range(u_plot.shape[0]):
    ys = j * np.ones(u_plot.shape[1])
    ax.plot(x, ys, u_plot[j, :], color=cm.jet(j * 20))

plt.figure()
plt.imshow(np.flipud(u), aspect=8)
plt.axis('off')
plt.set_cmap('jet_r')
plt.show()
