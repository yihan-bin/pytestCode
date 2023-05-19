import numpy as np
from dft import dft
from tkinter import Canvas
from tkinter import *
import random
time=0
wave=[]
y=[]

fourierY=[]
root = Tk()

def setup_F():
#    global fourierY
#    createCanvas(600,400);
    cv = Canvas(root,width=600, height=400,bg = 'black')
    cv.pack()
    angle=0
#    y=[100,100,100,-100,-100,-100,100,100,100,-100,-100,-100,]
    for i in range(100):
        l=np.random.normal(0,angle)
        y.append(100*l-50)
        angle+=0.02
    fourierY=dft(y)

    print(fourierY)

def draw():
#    background(0)
#   translate(150,200)

    x=0
    y=0
    for i in range(len(fourierY)):
        prevX=x
        prevY=y
        freq=fourierY[i].freq
        radius = fourierY[i].radius
        phase = fourierY[i].phase
        radius=75*(4/(n*np.pi))
        x+=radius*np.cos(freq*time+phase+np.pi/2)
        y+=radius*np.sin(freq*time+phase+np.pi/2)

        stroke(255,100)
#        noFill()#禁止几何填充
        cv.ellipse(prevX,prevY,radius*2)
        stroke(255)
        line(prevX,prevY,x,y)

    wave.unshift(y)


    translate(200,0)
    line(x-200,y,0,wave[0])
    beginShape()
    noFill()
    for i in range(len(wave)):
        vertex(i,wave[i])
    endShape()

    dt= np.pi * 2 / len(fourierY)
    time+=dt
    if (len(wave)>250):
        wave.pop()





if __name__ == "__main__":
    setup_F()
    draw()
    root.mainloop()