import time
import sys
class Student():
    def __new__(cls, *args, **kwargs):
        obj = super(Student, self).__new__()
        print(f'__new__被调用的，cls的ID值为’.format{id(cls)}')
        obj = super().__new__(cls)
        print(f'__new__被调用的，cls的ID值为’.format{id(obj)}')
        return obj
    def __init__(self):
        pass
print(id(object))
print(id(Student))
print(time.strftime('%y-%m-%d',time.localtime(time.time())))
s='2021-07-04'
data=time.strptime(s, '%Y-%m-%d')
print(data)

p1=('zhangsan', '20')
s='jcjksnijvnjwdnk' \
  'jiovkjoidsjvwo' \
  'mkdvmokdwj' \
  'kowmfkc'
print(s)
# print(sys.argv[0])
# print(sys.argv[2])
imgsz=10
m=2
imgsz *= 2 if m == 1 else 1
print(imgsz)