import pyqtgraph as pg
from pyqtgraph.Qt import QtCore,QtGui
import numpy as np


win=pg.GraphicsLayoutWidget(show=True)

win.setWindowTitle('jijsi')
p1=win.addPlot()
data1=np.random.normal(size=300)
curvel1=p1.plot(data1)

def updata1():
    global data1,ptr1
    data1[:-1]=data1[1:]
    data1[-1]=np.random.normal()
    curvel1.setData(data1)

timer=pg.QtCore.QTimer()
timer.timeout.connect(updata1)
timer.start(50)


if __name__=='__main__':
    import sys
    if (sys.flags.interactive!=1) or not hasattr(QtCore,'PYQT_VERSION'):
        QtGui.QApplication.instance().exec()
#        QtGui.QApplication.instance().exec_()

