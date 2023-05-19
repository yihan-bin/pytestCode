from numpy import dot, exp, array, random


def fp(input):
    l1 = 1 / (1 + exp(-dot(input, w0)))
    l2 = 1 / (1 + exp(-dot(l1, w1)))
    return l1, l2


def bp(l1, l2, y):
    error = y - l2
    slope = l2 * (1 - l2)
    l1_delta = error * slope

    l0_slope = l1 * (1 - l1)
    l0_error = l1_delta.dot(w1.T)

    l0_delta = l0_slope*l0_error
    return l0_delta, l1_delta


x = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = array([[0, 1, 1, 0]]).T

random.seed(1)
w0 = random.random((3, 10)) * 2 - 1
w1 = random.random((10, 1)) * 2 - 1

for i in range(100):
    l0 = x
    l1, l2 = fp(l0)
    l0_delta, l1_delta = bp(l1, l2, y)
    w1 = w1 + dot(l1.T, l1_delta)
    w0 = w0 + dot(l0.T, l0_delta)
print(fp([[1, 0, 1]])[0])
