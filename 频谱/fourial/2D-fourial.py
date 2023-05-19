import numpy as np
import matplotlib.pyplot as plt
from matplotlib.cm import get_cmap
from PIL import Image


def init_data():
    pass


def dft_2D(f, x, y):
    fourial_y = np.zeros((y, x), dtype='complex')
    for i1 in range(y):
        for i2 in range(x):
            for i3 in range(y):
                for i4 in range(x):
                    w = 2 * np.pi * ((i2 * i4) / x + (i1 * i3) / y)

                    fourial_y[i1][i2] += np.cos(w) * f[i3][i4].real
                    #fourial_y[i1][i2].imag += np.sin(w) * f[i3][i4].imag

    return fourial_y


def idft_2D(f, x, y):
    ifourial_y = np.zeros((y, x), dtype='complex')
    for i1 in range(y):
        for i2 in range(x):
            for i3 in range(y):
                for i4 in range(x):
                    w = 2 * np.pi * ((i2 * i4) / x + i1 * i3 / y)
                    ifourial_y[i1][i2] += np.cos(w) * f[i3][i4].real - np.sin(w) * f[i3][i4].imag
                    #ifourial_y[i1][i2].imag += np.cos(w) * f[i3][i4].imag - np.sin(w) * f[i3][i4].real
            ifourial_y[i1][i2] /= (x * y)
            #ifourial_y[i1][i2].imag /= (x * y)
    return ifourial_y

if __name__ == "__main__":
    image = Image.open('data/1.bmp')
    image_array = np.array(image)
    image_shape = image_array.shape
    print(image_shape[0])
    y = np.zeros((image_shape[0], image_shape[1]), dtype='complex')
    for i in range(image_shape[0]):
        for k in range(image_shape[1]):
            y[i][k] = image_array[i][k][0] * 0.2990 + image_array[i][k][1] * 0.5870 + image_array[i][k][2] * 0.1140

    dft_y = dft_2D(y, image_shape[0], image_shape[1])
    idft_y = idft_2D(dft_y, image_shape[0], image_shape[1])
    b_y=dft_y-idft_y
    print(b_y)