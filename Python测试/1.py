import wave
import os
import numpy as np
from pydub import AudioSegment
import matplotlib as plt

from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
from matplotlib import style
t = np.linspace(0, np.pi * 2, 100)
s = np.linspace(0, np.pi, 100)
t, s = np.meshgrid(t, s)
x = np.cos(t) * np.sin(s)
y = np.sin(t) * np.sin(s)
z = np.cos(s)
ax = plot.subplot(111, projection='3d')
ax.plot_wireframe(x, y, z)
plot.show()



