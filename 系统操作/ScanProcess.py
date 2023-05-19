#!/usr/bin/env python
# -*- coding: UTF-8 -*-
'''
@Project ：tank01.py 
@File    ：ScanProcess.py
@IDE     ：PyCharm 
@Author  ：zw的摸鱼时刻
@Date    ：2023/1/11 13:52 
'''

import os
import sys
import time
import psutil

# reload(sys)
# sys.setdefaultencoding('utf-8')
#############读取程序采集时间间隔（以分为单位）和采集次数（0为一直采集）
# with open("Set.ini", 'rb') as f:
#     set_content = f.read()
#
# interval = int(set_content.split(',')[0])
# num = int(set_content.split(',')[1])
interval = 5
num = 1

def help():
    print(u'用法： python monitor_port.py [-s | -h]')

    print(u'没有参数   读取配置文件，直接运行。')
    print(u'    -s 设置配置文件，包括扫描间隔和扫描次数。')
    print(u'    -h         显示帮助。')

    sys.exit(0)


def setting():
    global interval
    global num

    while True:
        set_interval = raw_input(unicode(">>> 请输入程序扫描间隔[min]:", 'utf-8').encode('gbk'))
        try:
            interval = int(set_interval)
        except Exception as e:
            print(u'输入有误，请输入数字！！！')
        else:
            break
    print(interval)

    while True:
        set_num = raw_input(unicode(">>> 请输入程序扫描次数[0为一直执行]:", 'utf-8').encode('gbk'))
        try:
            num = int(set_num)
        except Exception as e:
            print(u'输入有误，请输入数字！！！')
        else:
            break
    print(num)

    # with open("Set.ini", 'wb') as f:
    #     set_content = f.write(str(interval) + ',' + str(num))

    scanning_process()


def scanning_process():
    global interval
    global num
    i = 1
    if num > 0:
        num = num + 1

    print(u'开始扫描...')
    format1 = '{:<8}\t{:<40}\t{}'
    # format1 = '{:<8}\t{:<40}\t{}'
    # x = bytes(format1.format(r'PID', r'进程名', r'工作目录的绝对路径'), encoding='utf-8')
    # print(type(x))
    # with open("data/PID监测1.txt", 'ab') as f:
    #     f.write(bytes(format1.format(r'PID', r'进程名', r'工作目录的绝对路径') + os.linesep * 2, encoding='utf-8'))
    #     f.close()
    #





    with open("data/PID监测.txt", 'a') as f:
        while bool(i - num):
            p, now_time = psutil.pids(), time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
            f.writelines(format1.format(r'PID', r'进程名', r'工作目录的绝对路径') + os.linesep * 2)
            for po in p:
                try:
                    p_bin = psutil.Process(po).exe()
                except Exception as e:
                    p_bin = u"未找到该进程工作目录的绝对路径"
                finally:
                    # print po,str(psutil.Process(po)).split("'")[1],p_bin
                    f.write(format1.format(po, str(psutil.Process(po)).split("'")[1], p_bin) + os.linesep)

            f.write(os.linesep + now_time + os.linesep)
            f.write("-" * 126 + os.linesep * 2)
            f.flush()
            i = i + 1
            if num != 2:
                time.sleep(60 * interval)

    f.close()
    print(u'扫描结束...')


def main():
    if len(sys.argv) > 2:
        print(u'运行错误，请查看帮助！')
        print('Example：\tpython monitor_port.py -h')
        sys.exit(0)
    elif len(sys.argv) == 2:
        if sys.argv[1][-1] == 'h':
            help()
        elif sys.argv[1][-1] == 's':
            setting()
        else:
            print(u'运行错误，请查看帮助！')
            print('Example：\tpython monitor_port.py -h')
            sys.exit(0)
    else:
        scanning_process()


if __name__ == '__main__':
    main()
