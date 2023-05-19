import os
import sys
import numpy as np
from pathlib import Path
import keyboard
import cv2 as cv
import threading
import time
IMG_FORMATS = 'bmp', 'dng', 'jpeg', 'jpg', 'mpo', 'png', 'tif', 'tiff', 'webp'
FILE = Path(__file__).resolve()
ROOT = FILE.parents[0]
picDir = str(ROOT) + '\\data'
dirs = os.listdir(picDir)
labeldir = 'lable/'
tAr = []
tArl = []
m = 0

class imgmark():
    IMG_FORMATS = 'bmp', 'dng', 'jpeg', 'jpg', 'mpo', 'png', 'tif', 'tiff', 'webp'
    def __init__(self,dir):
        self.dir=dir
        # self.tAr = tAr
        # self.tAr1 = tAr1

    def readimg(self):
        dirpic = picDir + '\\' + self.dir
        ROOTpath = Path(os.path.relpath(dirpic, Path.cwd()))
        self.img = cv.imread('data/' + self.dir)
        cv.namedWindow("image")
        (w,h,d)=self.img.shape
        if w>3000:
            self.img = cv.resize(self.img, (int(h/10), int(w/10)), interpolation=cv.INTER_CUBIC)
        cv.setMouseCallback("image", on_EVENT_LBUTTONDOWN, self.img)
        cv.imshow("image", self.img)
    def readkey(self):
        key = cv.waitKey(0)
        return key
    def localProcess(self,tAr,tAr1):
        (w, h, z) = self.img.shape
        m = 0
        m = 0
        if test == 0:
            len_arr = len(tArl)
        else:
            len_arr = len(tArl) / 2
        for i in range(len_arr):
            x1 = tAr[2 * i][0] / w
            y1 = tAr[2 * i][1] / w
            x2 = tAr[2 * i + 1][0] / w
            y2 = tAr[2 * i + 1][1] / w
            tArl[0]
            self.write_to_txt(self.dir, (tArl[i], x1, y2, x2, y2))
        cv.destroyWindow("image")


    def write_to_txt(self,filename, classinfo):
        filename = labeldir + filename.split('.')[0] + '.txt'
        classinfo = np.array(classinfo)
        np.round(classinfo, 8)
        # np.savetxt(filename, classinfo, fmt='%f', delimiter=' ')
        f = open(filename, 'a')
        f.write(''.join(str(i) + ' ' for i in classinfo) + '\n')
        f.close()

def on_EVENT_LBUTTONDOWN(event, x, y, flags, param):
    global tAr, m
    if event == cv.EVENT_LBUTTONDOWN:
        xy = "%d,%d" % (x, y)
        m = 1
        tAr.append([x, y])
    if event == cv.EVENT_LBUTTONUP and m == 1:
        xy = "%d,%d" % (x, y)
        tAr.append([x, y])
        print(tAr)
        cv.rectangle(param, tAr[-1], tAr[-2], (255, 0, 0), thickness=1)
        cv.imshow("image", param)
        m = 0
def keyboardrecord():
    keyboard.hook(callback)
    keyboard.wait()


def callback(x):
    if x.event_type == keyboard.KEY_UP:
        # if x.name == 'space':
        #     tArl.append(x.name)
        #     print(tArl)
        if x.name.isdigit():
            tArl.append(int(x.name))
            print(tArl)
            time.sleep(1)
        if x.name.isdigit():
            if int(x.name)==2:
                print('ok')


if __name__=='__main__':
    test=0
    t = threading.Thread(target=keyboardrecord, name='aa', )
    t.start()

    for dir in dirs:
        if Path(dir).suffix[1:] in IMG_FORMATS:
            print(dir)
            imgclass = imgmark(dir)
            imgclass.readimg()
            while(True):
                x=imgclass.readkey()
                if imgclass.readkey()==32:
                    imgclass.localProcess(tAr,tArl)
                    tAr.clear()
                    tArl.clear()
                    break