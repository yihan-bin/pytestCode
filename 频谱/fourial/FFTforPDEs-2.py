import numpy as np
import matplotlib.pyplot as plt
import numpy.fft
from matplotlib import animation, rc
from IPython.display import HTML
import matplotlib.cm as cm
from scipy.integrate import odeint
from mpl_toolkits.mplot3d import axes3d

plt.rcParams['figure.figsize'] = [12, 12]
plt.rcParams.update({'font.size': 18})


nu=0.001
l=20
n=1000
dx=l/n
x=np.arange(-l/2,l/2,dx)

kappa=2*np.pi*np.fft.fftfreq(n,d=dx)

u0=1/np.cosh(x)


dt=0.025
t=np.arange(0,100*dt,dt)

def rhsBurgers(u,t,kappa,nu):
    uhat = np.fft.fft(u)
    d_uhat = (1j)*kappa*uhat
    dd_uhat=-np.power(kappa,2)*uhat
    d_u=np.fft.ifft(d_uhat)
    dd_u=np.fft.ifft(dd_uhat)
    du_dt=-u*d_u+nu*dd_u
    return du_dt.real

u = odeint(rhsBurgers, u0, t, args=(kappa, nu))





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
