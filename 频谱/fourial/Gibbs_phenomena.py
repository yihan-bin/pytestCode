import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation, rc
from IPython.display import HTML

plt.rcParams['figure.figsize'] = [8, 8]
plt.rcParams.update({'font.size': 18})
plt.rcParams['animation.html'] = 'jshtml'

dx = 0.01
L = 10
x = L * np.arange(0, L + dx, dx)
n = len(x)
nquart = int(np.floor(n / 4))

f = np.zeros_like(x)
f[nquart:3 * nquart] = 1

A0 = np.sum(f * np.ones_like(x)) * dx * 2 / L
fFS = A0 / 2 * np.ones_like(f)

fig, ax = plt.subplots()
ax.plot(x, f, color='k', linewidth=2)
fFs_plot, = ax.plot([], [], color='r', linewidth=2)
all_fFs = np.zeros((len(fFS), 101))
all_fFs[:, 0] = fFS

for k in range(1,101):
    Ak = np.sum(f * np.cos(np.pi * 2 * k * x / L)) * dx * 2 / L
    Bk = np.sum(f * np.sin(np.pi * 2 * k * x / L)) * dx * 2 / L
    tem = Ak * np.cos(2 * k * np.pi * x / L) + Bk * np.sin(2 * k * np.pi * x / L)
    temp_1 = tem + fFS
    all_fFs[:, k] = tem
print(all_fFs[:, k])

def init():
    ax.set_xlim(x[0], x[-1])
    ax.set_ylim(-0.2, 1.2)
    return fFS


def animate(lter):
    print(x)
    fFs_plot.set_data(x, all_fFs[:, iter])
    return fFs_plot


anim = animation.FuncAnimation(fig=fig, func=animate, init_func=init, frames=np.random.randint(0,101), interval=1000)
plt.show()
ani.save('1111.gif', writer='imagemagick', fps=100)
#anim.save('sin_x.gif')
#HTML(anim.to_jshtml())
