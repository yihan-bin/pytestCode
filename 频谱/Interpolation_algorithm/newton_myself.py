import numpy as np
import matplotlib.pyplot
from matplotlib import pyplot as plt


def difference_quotient(x, y):
    quotient = np.zeros((len(x), len(x)))
    i = 0
    order = len(y)
    while i < order:
        j = order - 1
        while j >= i:
            if i == 0:
                quotient[:, i] = y
            else:
                quotient[j][i] = (quotient[j][i - 1] - quotient[j - 1][i-1]) / (x[j]-x[j-i])
            j -= 1
        i += 1
    return quotient


if __name__ == '__main__':
    # x = [0.4, 0.55, 0.65, 0.80, 0.90, 1.05]
    # y = [0.41075, 0.57815, 0.69675, 0.88811, 1.02652, 1.25382]
    x = [1, 2, 3, 4, 5, 6]
    y = [1, 2, 4, 8, 16, 32]

    quotient_array = difference_quotient(x, y)
    print(quotient_array)
