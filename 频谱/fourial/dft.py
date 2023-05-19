import numpy as np

def dft(x) -> object:
    N=len(x)
    X=[]
    for k in range(N):
        re=0
        im=0
        for n in range(N):
            phi=(np.pi*2*k*n)/N
            re+=x[n]*np.cos(phi)
            im+=x[n]*np.sin(phi)
        re=re/N
        im=im/N

        freq=k
        amp=np.sqrt(re*re+im*im)
        phase=np.arctan2(im,re)
        X.append(re+1j*im)
    return X