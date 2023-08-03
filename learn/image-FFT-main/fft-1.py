
import numpy as np
from numpy.fft import fft
import re

import pygame, math, os
from pygame.locals import *


def fftProcess(fileName):
    f = open(fileName,'r')
    content = f.readlines()
    pointList = []
    for data in content:
        pointAll = re.findall(r'-?\d+\.?\d*e?-?\d*?',data)
        if len(pointAll)%2:
            del(pointAll[-1])
        for i in range(0,len(pointAll)-2,2):
            #if i+8>=len(pointAll):break
            pointList.append((float(pointAll[i+1]),float(pointAll[i])))
            
    #sorted(pointList)
    y_matrix = np.array(pointList)
    
    y = [complex(p[0], p[1]) for p in pointList]
    
    print(y_matrix.shape)
    # plt.plot(y_matrix[:, 0],y_matrix[:, 1])
    # plt.show()
    with open("mm.txt", "w") as File:#把结果写入硬盘
        for dc in y:
            File.write("{0},{1}".format(dc.real,dc.imag))
            File.write("\n")
    y_len = len(y)
    yy = fft(y)
    Dou=[]
    PP = []
    MM=[]
    # for i in range(36):
    #     tem=np.tan(i*2*np.pi/36-np.pi)
    #     print(np.arctan(tem))
    #     print(i*2*np.pi/36-np.pi)
    for i, v in enumerate(yy[:y_len]):
        c = -2 * np.pi * i / y_len
        PP.append([-v.real / y_len, c, -np.pi / 2])
        PP.append([-v.imag / y_len, c, np.pi])
        tem=math.pow(v.real,2)+math.pow(v.imag,2)
        L=math.sqrt(tem)/y_len
        thel=np.arctan2(v.imag,v.real)
        #实部与虚部之间差了90度角，所以在这里进行区分，又由于向量之间的加减可以弥补平方在开根号，所以这里进行实部虚部分开计算，从而获得相加
        MM.append([L,c,thel])
    aa= -2 * np.pi * 7 / y_len
    bb = -2 * np.pi * 4 / y_len

    Dou.append([50, aa, thel])
    Dou.append([45, bb, 20*thel])
    PP.sort(key=lambda x: abs(x[0]), reverse=True)
    #MM.sort(key=lambda x: abs(x[0]), reverse=True)
    #排序主打一个排序不排序无所畏惧，但是不排序，信号的频率存在有小到大，导致画图难看
    return PP
        
# svgData("./images/132.txt")
        
def draw(fname):

    WINDOW_W = 600
    WINDOW_H = 600
    one_time = 5  # 时间流速（默认1）
    scale = 1  # 缩放（默认120）
    FPS = 600  # 帧率
    point_size = 2  # 点的大小
    start_xy = (WINDOW_W // 2 + 100, WINDOW_H // 2)  # 圆的位置

    # 波形图参数
    b_scale = 1  # 图形缩放
    b_color = (255, 10, 250)  # 图形颜色
    b_length = 10000  # 图形显示的长度
    PP = fftProcess(fname)

    fourier_list = PP[:]

    # 初始化pygame
    pygame.init()
    pygame.mixer.init()
    os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 70)
    # 创建一个窗口
    screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF, 32)
    pygame.display.set_caption("可视化")
    font = pygame.font.SysFont('simhei', 20)


    class Circle():
        x, y = 0, 0
        r = 0
        angle = 0
        angle_v = 0
        color = (0, 0, 0)
        father = None

        def __init__(self, r, angle_v, angle, color=None, father=None):
            self.r = r
            self.angle_v = angle_v
            self.angle = angle
            self.father = father
            if color is None:
                self.color = (250, 250, 250)
            else:
                self.color = color

        def set_xy(self, xy):
            self.x, self.y = xy

        def get_xy(self):
            return self.x, self.y

        def set_xy_by_angle(self):
            self.x = self.father.x + self.r * math.cos(self.angle) * scale
            self.y = self.father.y + self.r * math.sin(self.angle) * scale

        def run(self, step_time):
            if self.father is not None:
                self.angle += self.angle_v * step_time
                self.set_xy_by_angle()

        def draw(self, screen):
            color_an = tuple(map(lambda x: x // 3, self.color))
            # 画圆
            # print(color_an, int(round(self.x)), self.y)
            pygame.draw.circle(screen, self.color, (int(round(self.x)), int(round(self.y))), point_size)
            # 画轨道
            if self.father is not None:
                # print(color_an, self.father.x, self.father.y)
                pygame.draw.circle(screen, color_an, (int(round(self.father.x)), int(round(self.father.y))),
                                max(int(round(abs(self.r) * scale)), 1),
                                1)
                pygame.draw.line(screen, self.color, (self.father.x, self.father.y), (self.x, self.y),
                                1)


    class Boxin():
        xys = []

        def add_point(self, xy):
            self.xys.append(xy)
            if len(self.xys) > b_length:
                self.xys.pop(0)

        def draw(self, screen):
            # 画一个圆
            # pygame.draw.circle(screen, b_color, (b_xy[0], int(b_xy[1] + self.ys[-1] * scale)), point_size)
            bl = len(self.xys)
            for i in range(bl - 1):
                pygame.draw.line(screen, (255, 250, 0), self.xys[i], self.xys[i + 1], 1)


    # fourier_list = sorted(fourier_list, key=lambda x: abs(x[0]), reverse=True)
    super_circle = Circle(0, 0, 0, color=b_color)
    super_circle.set_xy(start_xy)
    circle_list = [super_circle]
    for i in range(len(fourier_list)):
        p = fourier_list[i]
        circle_list.append(Circle(p[0], p[1], p[2], color=b_color, father=circle_list[i]))

    bx = Boxin()
    clock = pygame.time.Clock()
    
    flag = False
    # 游戏主循环
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                flag = True
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    flag = True
                    pygame.quit()
                elif event.key == K_LEFT and one_time > 0.1:
                    one_time *= 0.9
                    one_time = max(one_time, 0.1)
                elif event.key == K_RIGHT and one_time < 10:
                    one_time *= 1.1
                elif (event.key == K_EQUALS or event.key == K_PLUS) and scale < 800:
                    scale *= 1.1
                elif event.key == K_MINUS and scale > 0.001:
                    scale *= 0.9
                    scale = max(scale, 0.001)
                else:
                    print(type(event.key), event.key)
        if flag:
            return 
        # 将背景图画上去
        screen.fill((0, 0, 0))
        # 运行
        for i, circle in enumerate(circle_list):
            circle.run(1)
            circle.draw(screen)

        last_circle = circle_list[-1]
        # 画波形
        bx.add_point((last_circle.x, last_circle.y))
        bx.draw(screen)

        pygame.display.update()
        time_passed = clock.tick(FPS)


if __name__ == '__main__':
    fileName = "images/music_symbol.txt"
    draw(fileName)