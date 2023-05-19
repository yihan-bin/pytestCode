from __future__ import print_function
import ctypes
import sys
import winreg
import time
import ctypes, sys


def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

a=is_admin()
print(a)
if is_admin():
    # 将要运行的代码加到这里
    key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\test\test', reserved=0, access=winreg.KEY_ALL_ACCESS)
    # print(key)
    winreg.CreateKey(key, 'puj')
    aa = winreg.QueryInfoKey(key)
    # winreg.QueryValue(aa,'2345Pic.cr3') #用一个字符串来检索一个键的值
    bb = winreg.QueryValueEx(key, '1')  # 检索与开放权限的注册表键相关联的指定值的数据类型和名称
    cc = winreg.QueryValueEx(key, '2')  # 检索与开放权限的注册表键相关联的指定值的数据类型和名称
    print(aa, bb, cc[0])
    winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, r'SOFTWARE\test\puj',reserved=0, access=winreg.KEY_WRITE)
    winreg.SetValue(key, '', winreg.REG_SZ, 'URL:nzblnk')
    winreg.SetValueEx(key, 'URL Protocol', 0, winreg.REG_SZ, '')
    time.sleep(20)
else:
    if sys.version_info[0] == 3:
        print(sys.version_info)
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, __file__, None, 1)
    else:  # in python2.x
        # pass
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
        ctypes.windll.shell32.ShellExecuteW(None, u"runas", unicode(sys.executable), unicode(__file__), None, 1)
