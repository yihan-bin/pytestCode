# 深度神经网络的代码：
from numpy import random, dot, exp, array


# 正向推导：根据输入和权重，算出结果
def fp(input):
    l1 = 1 / (1 + exp(-dot(input, w0)))
    l2 = 1 / (1 + exp(-dot(l1, w1)))
    return l1, l2


# 反向转播：用计算结果和实际结果的误差，反向推算权重的调整量
def bp(l1, l2, y):
    # 看看我们计算出来的和实际发生的有多大误差
    error = y - l2
    slope = l2 * (1 - l2)
    l1_delta = error * slope

    l0_slope = l1 * (1 - l1)
    l0_error = l1_delta.dot(w1.T)

    l0_delta = l0_slope * l0_error

    # 计算增量
    return l0_delta, l1_delta


# 准备数据: X是输入参数, y是正确结果
X = array([[0, 0, 1], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
y = array([[0, 1, 1, 0]]).T

# 设置随机的权重，随机值*2再减1是为了让随机值在-1和1之间
random.seed(1)
w0 = random.random((3, 10)) * 2 - 1
w1 = random.random((10, 1)) * 2 - 1
print( w0 , '/t', w1)
for it in range(10000):
    # 正向推导
    l0 = X
    l1, l2 = fp(l0)

    # 反向传播
    l0_delta, l1_delta = bp(l1, l2, y)

    # 更新权重
    w1 = w1 + dot(l1.T, l1_delta)
    w0 = w0 + dot(l0.T, l0_delta)

print(fp([[1, 0, 1]])[1])