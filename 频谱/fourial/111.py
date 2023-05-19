# 动态画出sin函数曲线
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
a=np.array([1,2,3,4,5])
b=np.array([4,5,3,2,])
c=a+b
print(c)
# 生成子图，相当于fig = plt.figure(),ax = fig.add_subplot(),其中ax的函数参数表示把当前画布进行分割，
fig, ax = plt.subplots()
xdata, ydata = [], []
ln, = ax.plot([], [], 'r-', animated=False)
def init():
    ax.set_xlim(0, 2 * np.pi)
    ax.set_ylim(-1, 1)
    # 返回曲线
    return ln,
def update(frame):
    # 将每次传过来的n追加到xdata中
    xdata.append(frame)
    ydata.append(np.sin(frame))
    # 重新设置曲线的值
    ln.set_data(xdata, ydata)
    return ln,

ani = FuncAnimation(fig=fig, func=update, frames=np.linspace(0, 2 * np.pi, 128),
                    init_func=init, blit=True)
plt.show()
ani.save('sin_test1.gif', writer='imagemagick', fps=100)
