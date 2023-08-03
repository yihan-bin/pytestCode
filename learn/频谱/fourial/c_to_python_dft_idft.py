from cmath import exp, pi
a=[]
print(len(a))



def log2n(n):
    k = 0
    while (n >> (k + 1)):
        k = k + 1
    return k

def fft(x, N :int , skip):
    X = [0]*N
    if N == 1:
        X[0] = x[0]
        return
    n2 = int(N / 2)
    even = [0]*n2
    odd = [0]*n2

    for i in range(n2):
        even[i] = x[2 * i]
        odd[i] = x[2 * i + 1]

    Even = [0]*n2
    Odd = [0]*n2
    Even=fft(even, int(N / 2), 2 * skip)
    Odd=fft(odd, int(N / 2), 2 * skip)

    for k in range(n2):
        t = exp(-1j * pi * k / N) * Odd[k]
        X[k] = Even[k] + t
        X[k + N / 2] = Even[k] - t
    return X

def ifft(self):
    pass


if __name__ == "__main__":

    x = [10, 4, 2, 4, 7, 6, 8, 7, 6, 5]
    N = len(x)
    min = 0
    max = 0
    for i in range(20):
        min = pow(2, i)
        max = pow(2, i + 1)
        if ((min < N) and (max >= N)):
            print(max)
            break

    p = []
    logN = int(log2n(N))

    for i in range(N):
        p.append(x[i])

    for i in range(N, max):
        p.append(0)

    X = fft(p, max, 1)

    print("FFT结果：\n")
    for i in range(n):
        print("%f + %fi\n", X[i].real, X[i].imag)

    Y = dft.fft()

    print("\nIFFT结果：\n")
    for i in range(n):
        print("%f + %fi\n", y[i].real, y[i].imag)
