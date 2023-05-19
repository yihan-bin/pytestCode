import time


def writelog(func):
    print('访问了方法名：',func.__name__,'\t时间：',time.asctime())

def funout(func):
    def funin(x,y):#调用带参数的函数时，要加上参数
        writelog(func)
        return func(x,y)
    return funin


@funout
def sum(a,b):
    return a+b

result= sum(10,20)
print('两数之和',result)

def funout2(func):
    def funin(x,y,z):#调用带参数的函数时，要加上参数,只支持三个参数，不通用
        writelog(func)
        return func(x,y,z)
    return funin
@funout2
def add(x,y,z):
    return x+y+z
result1= add(10,20,30)
print('两数之和',result1)




#通用参数装饰器
def funouy3(funv):
    def funin(*args):
        writelog(funv)
        return funv(*args)
    return funin



#通用参数装饰器
def funouy4(funv):
    def funin(*args,**kwargs):
        writelog(funv)
        return funv(*args,**kwargs)
    return funin



@funouy3
def sum2(a,b):
    return a+b
@funouy3
def add2(a,b,c):
    return a+b+c

result2 = sum2(1,2)
result3 = add2(1,2,3)
print('两数之和',result2)
print('三数之和',result3)