import os
while True:
    port=input('请输入端口号:')
    port=57978
    result = os.popen('netstat -aon|findstr "{0}"'.format(port))
    result2=os.popen('NETSTAT -a')
    print(result.read())
    print(result2)
