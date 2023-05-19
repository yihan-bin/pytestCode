from __future__ import print_function
import ctypes
import sys
import winreg as reg
import time
import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

a=is_admin()
print(a)
if is_admin() or True:
    # 将要运行的代码加到这里
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r'SOFTWARE\test\test', reserved=0, access=reg.KEY_READ)

else:
    if sys.version_info[0] == 3:
        print(sys.version_info)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:  # in python2.x
        # pass
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)


def test():
    key = reg.OpenKey(reg.HKEY_LOCAL_MACHINE, r"SOFTWARE\2345Pic\Capabilities")
    try:
        print("-----get subKeys-----")
        i = 0
        while True:  # 一直枚举，枚举完毕之后会抛出错误ERROR 259
            name = reg.EnumKey(key, i)
            i += 1
            print(name)
    except Exception as e:
        print(e)


    try:
        print('-----get subValues-----')
        i = 0
        while True:
            k, v, t = reg.EnumValue(key, i)
            i += 1
            print(k, v, t)
    except Exception as e:
        print(e)
    reg.CloseKey(key)
if __name__=='__main__':
    test()