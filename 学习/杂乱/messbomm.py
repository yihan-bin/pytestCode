#from ctypes import windll
import time
from pymouse import PyMouse
from pynput import mouse
from pykeyboard import PyKeyboard
import keyboard
import pyautogui

m = PyMouse() ##鼠标实例
k = PyKeyboard() ##键盘实例

# width = windll.user32.GetSystemMetrics(0)
# height = windll.user32.GetSystemMetrics(1)

position=[]
timedelay=[]
lasttime=time.time()
def on_click(x, y, button, pressed):
    global lasttime
    if pressed:
        position.append(m.position())
        print(m.position())
        nowtime=time.time()
        timedelay.append(nowtime-lasttime)

        print(nowtime-lasttime)
        lasttime = time.time()

listener = mouse.Listener(
    on_click=on_click,)
listener.start()



print('第一次坐标width, height')
time.sleep(1)
(w,h)=m.position()
print(m.position())
## 横纵坐标的分辨率是针对整个电脑屏幕来说的，比如整个电脑的分辨率是1920x1080。输入位置的分辨率为665 【回车】 1000
#print('请输入需要控制位置的横纵分辨率')
time.sleep(3)

(w2,h2)=m.position()
print(m.position())
# pyperclip.copy('https://cn.bing.com/search?q=%E5%9B%BE%E7%89%87&qs=n&form=QBRE&sp=-1&pq=%E5%9B%BE%E7%89%87&sc=10-2&sk=&cvid=14CC3C91C9B242089816F210DF2263ED&ghsh=0&ghacc=0&ghpl='*10)
# pyperclip.copy('https://cn.bing.com/search?q=%E5%9B%BE%E7%89%87&qs=n&form=QBRE&sp=-1&pq=%E5%9B%BE%E7%89%87&sc=10-2&sk=&cvid=14CC3C91C9B242089816F210DF2263ED&ghsh=0&ghacc=0&ghpl='*10)
# pyperclip.copy('https://cn.bing.com/search?q=%E5%9B%BE%E7%89%87&qs=n&form=QBRE&sp=-1&pq=%E5%9B%BE%E7%89%87&sc=10-2&sk=&cvid=14CC3C91C9B242089816F210DF2263ED&ghsh=0&ghacc=0&ghpl='*10)
k=0
## 对固定位置的某个输入框重复输入某个字符串（不支持中文），并按回车发送。
try:
    while 1:
        if keyboard.is_pressed('space'):
            listener.stop()
            k=1
            timedelay.append(0.2)
        if k==1:
            i=0;
            for (w,h) in position:
                m.click(int(w), int(h))
                time.sleep(timedelay[i+1]+0.2)


            # m.click(int(w), int(h))
            # #k.type_string('xxx')
            # time.sleep(0.2)
            #
            # # 复制要发送的文字
            # pyautogui.hotkey("ctrl", "v")
            # #sys.stdout.flush()
            # time.sleep(1.5)
            # #k.tap_key(k.enter_key)
            # m.click(int(w2), int(h2))
            # time.sleep(0.2)
            # if keyboard.is_pressed('space'):
            #     break
except KeyboardInterrupt:
    print("捕获异常")