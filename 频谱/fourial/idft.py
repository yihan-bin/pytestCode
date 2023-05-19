import numpy as np

def idft(x):
    N=len(x)
    X=[]
    for k in range(N):
        re=0
        im=0

        for n in range(N):
            if True:
                phi = (np.pi * 2 * k * n) / N
                re=re+x[n].real*np.cos(phi)-x[n].imag*np.sin(phi)
                im=im+x[n].real*np.sin(phi)+x[n].imag*np.cos(phi)
            # else:
            #
            #     phi = -(np.pi * 2 * k * (n)) / N
            #     re = re + x[n].real * np.cos(phi) - x[n].imag * np.sin(phi)
            #     im = im + x[n].real * np.sin(phi) + x[n].imag * np.cos(phi)

        re=-re
        im=-re

        freq=k
        amp=np.sqrt(re*re+im*im)
        print(amp)
        phase=np.arctan2(im,re)
        X.append(re+1j*im)
    return X