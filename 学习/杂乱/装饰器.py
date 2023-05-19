


def funout(func):
    print('装饰器1')
    def funin():
        print(f'I am {func.__name__} and {func.__name__} 2')
        func()
    return funin
def funout2(func):
    print('装饰器2')
    def funin():
        print('hellow')
        func()
    return funin

#双重装饰
@funout2
@funout  #  相当于funout(foo)//优先执行
def foo():
    print('foo正在运行')

def ffoo():
    print('正在执行FFoo')

#foo = funout(foo)
foo()
ffoo=funout(ffoo)
ffoo()