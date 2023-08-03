import numpy
import numpy as np


def complex_multiply( a,  b):
    real = a.real * b.real - a.imag * b.imag
    imag = a.real * b.imag + a.imag * b.real
    return real+imag*1j
def fft_recursive(N,  x,  X):

    if (N == 1):  # 递归结束条件，N为1时，X[0] = x[0]
        X[0] = x[0]
        return
    # 分治计算DFT，得到偶数、奇数下标序列对应的DFT值
    xe = np.empty(N / 2)
    x0 = np.empty(N / 2)
    Xe = np.empty(N / 2)
    Xe = np.empty(N / 2)

    for k in range(N/2):
        xe[k] = x[2*k]
        xo[k] = x[2*k+1]

    fft_recursive(N/2, xe, Xe)
    fft_recursive(N/2, xo, Xo)

    # 计算X[k]，其中X[k+N/2]=W_N^k*Xo[k]
    Wn=0+0j
    for k in range(N/2):
        Wn.real = np.cos(2 * np.pi * k / N)
        Wn.imag = -np.sin(2 * np.pi * k / N)
        t = complex_multiply(Wn, Xo[k])
        X[k] = complex_add(Xe[k], t)
        X[k+N/2] = complex_sub(Xe[k], t)



# 快速傅立叶变换
def fft( n, x,  y):

    a=[]
    b=[]

    # 将数据复制到复数结构体中
    for i in range(n):
        a.append(x[i]+y[i]*1j)

    # 调用递归函数计算FFT
    fft_recursive(n, a, b)

    # 将结果复制回来
    for i in range(n):
        x[i] = b[i].real
        y[i] = b[i].imag

    print(x)
    print(y)

if __name__ == "__main__":
    a=[1,2,3,4,5,4,3,2,1,0]
    fft(10,a,a)