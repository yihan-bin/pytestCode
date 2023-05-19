import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

plt.rcParams['figure.figsize'] = [16, 12]
plt.rcParams.update({'font.size': 18})

dt = 0.001

t = np.arange(0, 1, dt)
f = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)
f_close = f
f = f + 2.5 * np.random.randn(len(t))

plt.plot(t, f, color='c', linewidth=1.5, label='Nosiy')
plt.plot(t, f_close, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()

n = len(t)
fhat = np.fft.fft(f, n)
PSD = fhat * np.conj(fhat) / n
freq = (1 / (dt * n))*np.arange(n)
L=np.arange(1,np.floor(n/2),dtype='int')


fig, axs = plt.subplots(2, 1)
plt.sca(axs[0])
plt.plot(t, f, color='c', linewidth=1.5, label='Nosiy')
plt.plot(t, f_close, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()


plt.sca(axs[1])
plt.plot(freq[L], PSD[L], color='c', linewidth=1.5, label='Nosiy')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()


indices=PSD>100
psdclean=PSD*indices
fhat=indices*fhat
ffilt=np.fft.ifft(fhat)



fig,axs=plt.subplots(3,1)

plt.sca(axs[0])
plt.plot(t, f, color='c', linewidth=1.5, label='Nosiy')
plt.plot(t, f_close, color='k', linewidth=2, label='Clean')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[1])
plt.plot(t, ffilt, color='c', linewidth=1.5, label='Nosiy')
plt.xlim(t[0], t[-1])
plt.legend()

plt.sca(axs[2])
plt.plot(freq[L], PSD[L], color='c', linewidth=1.5, label='Nosiy')
plt.plot(freq[L], psdclean[L], color='k', linewidth=1.5, label='Filtery')
plt.xlim(freq[L[0]], freq[L[-1]])
plt.legend()



plt.show()

# A0 = np.sum(f * np.ones_like(x)) * dx * 2 / L
# fFS = A0 / 2 * np.ones_like(f)
#
# fig, ax = plt.subplots()
# plt.plot(x, f, color='k', linewidth=2)
# fFs_plot, = plt.plot([], [], color='r', linewidth=2)
# all_fFs = np.zeros((len(fFS), 101))
# all_fFs[:, 0] = fFS
#
# for k in range(101):
#     Ak = np.sum(f * np.cos(np.pi * 2 * k * x / L)) * dx * 2 / L
#     Bk = np.sum(f * np.sin(np.pi * 2 * k * x / L)) * dx * 2 / L
#     fFS = fFS + Ak * np.cos(2 * k * np.pi * x / L) + Bk * np.sin(2 * k * np.pi * x / L)
#     all_fFs[:, k] = fFS
# print(len(all_fFs[:, k]))
#
#
# def init():
#     ax.set_xlim(x[0], x[-1])
#     ax.set_ylim(-0.2, 1.2)
#     return fFS
#
#
# def animate(lter):
#     fFs_plot.set_data(x, all_fFs[:, iter])
#     return fFs_plot


# anim = animation.FuncAnimation(fig, animate, init_func=init, frames=101, interval=50)
# anim.save('sin_x.gif')
# HTML(anim.to_jshtml())
