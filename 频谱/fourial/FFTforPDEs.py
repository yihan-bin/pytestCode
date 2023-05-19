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


c=2
l=20
n=1000
dx=l/n
x=np.arange(-l/2,l/2,dx)

kappa=2*np.pi*np.fft.fftfreq(n,d=dx)

u0=1/np.cosh(x)
u0hat=np.fft.fft(u0)


u0hat_ri=np.concatenate((u0hat.real,u0hat.imag))


dt=0.25
t=np.arange(0,100*dt,dt)

def rhsWave(uhat_ri,t,kappa,c):
    uhat = uhat_ri[:n] + (1j) * uhat_ri[n:]
    d_uhat = -c*(1j)*kappa*uhat
    d_uhat_ri = np.concatenate((d_uhat.real, d_uhat.imag)).astype('float64')
    return d_uhat_ri

uhat_ri = odeint(rhsWave, u0hat_ri, t, args=(kappa, c))
uhat = uhat_ri[:, :n] + (1j) * uhat_ri[:, n:]



def rhsWaveSpatial(u,t,kappa,c):
    uhat=numpy.fft.fft(u)
    d_uhat=(1j)*kappa*uhat
    d_u=np.fft.ifft(d_uhat).real
    du_dt=-c*d_u
    return du_dt


u=odeint(rhsWaveSpatial,u0,t,args=(kappa,c))
u=np.zeros_like(uhat)
zeros_like
for k in range(len(t)):
    u[k,:]=np.fft.ifft(uhat[k,:])


u=u.real



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
