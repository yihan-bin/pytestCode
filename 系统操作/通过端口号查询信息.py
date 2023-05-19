from os import popen
while True:
    port=input('请输入端口号:')
    with popen('netstat -aon|findstr "{0}"'.format(port)) as res:
        res = res.read().split('\n')
    results = []
    for line in res:
        temp = [i for i in line.split(' ') if i != '']
        if len(temp) > 4:
            results.append({'pid': temp[4], 'address': temp[1], 'state': temp[3]})
    for result in results:
        print(result)
