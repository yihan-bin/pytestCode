import numpy as np
import matplotlib.pyplot as plt

from middle_filter import Filter


def FUN_FindNearestPoint(ppointList, ppoint, distance):
    searchx = ppoint[1] - distance

    FindNearestPoint = False
    ppointRetL = [0, 0]
    ppointRetR = [0, 0]
    if ppointList[-1]:
        newerPoint = ppointList[-1]
        # 如果想找的这个点比最新的一个点还要靠后，则直接判断输出点和构造偏移点
        if searchx >= newerPoint[0]:
            ppointRetL[0] = newerPoint[0]
            ppointRetL[1] = newerPoint[1]
            ppointRetR[0] = searchx + 500000
            ppointRetR[1] = ppoint[1] - distance + 500000
            FindNearestPoint = True
        else:
            if (len(ppointList) >= 2):

                for i in range(len(ppointList)):
                    i = i + 1
                    if i == 50:
                        a = 0
                    if ppointList[-i]:
                        tmpPoint = ppointList[-i]
                        # 找到这个分布在查找点两侧的点，输出
                        if (searchx >= tmpPoint[0]) and (searchx < newerPoint[0]):
                            ppointRetL[0] = tmpPoint[0]
                            ppointRetL[1] = tmpPoint[1]
                            ppointRetR[0] = newerPoint[0]
                            ppointRetR[1] = newerPoint[1]
                            FindNearestPoint = True
                            return FindNearestPoint, ppointRetL, ppointRetR
                        else:
                            newerPoint = [x for x in tmpPoint]
    return FindNearestPoint, ppointRetL, ppointRetR


class measLSensorOffset():
    # 产生下降沿
    def __init__(self):

        self.KeyPoints = []
        self.KeyPoints2 = []
        self.KeyPointsOK = []
        self.distanceRecorder = []
        self.offsetRecorder = []
        self.cal = Filter()
        self.thisRCounter = 0
        self.kkk=0
    # 当前架下降沿来了，计数，然后记录点的位置
    def findpoint(self, thisFSignal, nextSignal, thisMDPos, nextMDPos, filmLength, distanceSet):
        MAX_D2_OFFSET = 500
        if thisFSignal:
            self.thisRCounter = self.thisRCounter + 1
            if self.thisRCounter >= 0:
                # 记录点信息
                thisRCounter = 0
                tempPoint = []

                tempPoint.append(thisMDPos)
                tempPoint.append(nextMDPos)
                # self.tempPoint.Z = thisAxisPosition

                self.KeyPoints.append(tempPoint)

        # 后架感应到下降沿后，查找点
        valid = False
        outValid = False
        findPointFlag = False
        outDistance = 0.0
        if nextSignal:
            tmpPointNext = []
            tmpPointNext.append(thisMDPos)
            tmpPointNext.append(nextMDPos)
            # self.tmpPointNext.Z = nextAxisPosition

            # 查找最近点，返回左点和右点
            findPointFlag, findPointL, findPointR = FUN_FindNearestPoint(self.KeyPoints, tmpPointNext, distanceSet)

        if findPointFlag:
            # 来一个记一个，来两个记一双
            self.KeyPoints2.append(tmpPointNext)
            # 找到最近坐标点后，需要减去一个D2的距离再做距离运算，才能获得偏差值
            disL = np.abs(tmpPointNext[1] - distanceSet - findPointL[0])
            disR = np.abs(tmpPointNext[1] - distanceSet - findPointR[0])
            # 留下来的判断在这道理有啥用
            distance=0
            offset=0
            if (disL < min(filmLength / 2, MAX_D2_OFFSET)) and (disL < disR):
                offset = disL
                distance = abs(tmpPointNext[1] - findPointL[0])
                # AxisPositionOffset =tmpPointNext.X - findPointL.X
                valid = True
            elif disR < min(filmLength / 2, MAX_D2_OFFSET) and (disR < disL):
                offset = -disR
                distance = abs(findPointR[0] - tmpPointNext[1])
                # axisPositionOffset =findPointR.X - tmpPointNext.X
                valid = True
            else:
                valid = False

            # 把每次检测到的D2记录下来
            self.distanceRecorder.append(distance)
            # 把检测到的偏差数据记录一下
            self.offsetRecorder.append(offset)
            # 从链表中找到的
            #minDist = SEL(disL < disR, -disR, disL)

            self.KeyPointsOK.append(tmpPointNext)
            self.kkk=self.kkk+1
            if self.kkk>200 and valid:
                m=0
            # 如果找到最近的边界点，则使用滤波器对这些距离点进行处理
            if valid:

                filterValid = self.cal.filter_value(distance * 1000)
                if filterValid:
                    outDistance = (filterValid) / 1000
                    outValid = True
                    return outValid, outDistance
            else:
                outValid = False
        # #现在链表中加入一个负的点，偏差很大
        if 0 == len(self.KeyPoints):
            self.tempPoint[0] = -500000
            self.tempPoint[1] = -500000
            self.KeyPoints2.append(self.tempPoint)
        return False, outDistance


if __name__ == "__main__":
    findnearpointA = measLSensorOffset()
    findnearpointB = measLSensorOffset()
    findnearpointC = measLSensorOffset()
    findnearpointD = measLSensorOffset()
    lenthA, lenthB, lenthC, lenthD, = [], [], [], []
# valid = False
    list1 = np.genfromtxt(open("../exportdata/222.csv", "rb"), delimiter=",", encoding='GBK')
    for i in range(len(list1)):
        if list1[i][2] == 1:

            vaild, lenth_tem = findnearpointA.findpoint(True, False, list1[i][3] * 0.025, 0, 700, 9236)
        elif list1[i][2] == 2:
            vaild, lenth_tem = findnearpointA.findpoint(False, True, 0, list1[i][3] * 0.025, 700, 9236)
            findnearpointB.findpoint(True, False, list1[i][3] * 0.025, 0, 700, 59380)
            if vaild:
                lenthA.append(lenth_tem)
        elif list1[i][2] == 3:
            vaild, lenth_tem = findnearpointB.findpoint(False, True, 0, list1[i][3] * 0.025, 700, 59380)
            findnearpointC.findpoint(True, False, list1[i][3] * 0.025, 0, 700, 12589)
            if vaild:
                lenthB.append(lenth_tem)
        elif list1[i][2] == 4:
            vaild, lenth_tem = findnearpointC.findpoint(False, True, 0, list1[i][3] * 0.025, 700, 12589)
            findnearpointD.findpoint(True, False, list1[i][3] * 0.025, 0, 700, 69615)
            if vaild:
                lenthC.append(lenth_tem)
        elif list1[i][2] == 5:
            vaild, lenth_tem = findnearpointD.findpoint(False, True, 0, list1[i][3] * 0.025, 700, 69615)
            if vaild:
                lenthD.append(lenth_tem)

    plt.figure()
    plt.plot(lenthA)
    plt.figure()
    plt.plot(lenthB)
    plt.figure()
    plt.plot(lenthC)
    plt.figure()
    plt.plot(lenthD)
    plt.show()
