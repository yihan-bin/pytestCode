import time


def writelog(func):
    try:
        file = open('../createData/write.txt', 'a', encoding='utf-8')
        file.write('访问：')
        file.write(func.__name__)

        file.write('\t')
        file.write('时间：')
        file.write(time.asctime())
        file.write('\n')

    except Exception as e:
        print(e.args)
    finally:
        file.close()


def fun1():
    writelog(fun1)
    print('功能1')

def fun2():
    writelog(fun2)
    print('功能2')
#不使用闭包实现修改
fun1()
fun2()

#不改变代码的情况下进行函数修改
def funcout(func):
    def funcin():
       func()
       print('调用',func.__name__,'结束')
    return funcin

fun1=funcout(fun1)
fun1()
fun2=funcout(fun2)
fun2()

import image