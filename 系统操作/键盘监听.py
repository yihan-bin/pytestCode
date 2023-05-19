import keyboard

t=[]
def callback(x):
    if x.event_type == 'down':
        print(x)
        if x.name=='space':
            t.append(x.name)
            print(t)

        if x.name.isdigit():
            print(int(x.name))

keyboard.hook(callback)
# 按下任何按键时，都会调用callback，其中一定会传一个值，就是键盘事件
keyboard.wait('1','2')