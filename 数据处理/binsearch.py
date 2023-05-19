import numpy as np


def binsearch(arr, stidx, edidx, sortdir, tval, mpos):
    midx = 0
    if (stidx > edidx):
        if (sortdir == 1):
            mpos = stidx
        else:
            mpos = edidx
        return -1

    elif (stidx == edidx):
        if (arr[stidx] > tval):
            if (sortdir == 1):
                mpos = stidx
            else:
                mpos = stidx + 1
            return -1
        elif (arr[stidx] == tval):
            mpos = stidx
            return stidx
        else:
            if (sortdir == 1):
                mpos = stidx + 1
            else:
                mpos = stidx
            return -1
    else:
        midx = int((stidx + edidx) / 2)
        if (arr[midx] == tval):
            mpos = midx
            return midx
        elif ((arr[midx] > tval and sortdir == 1) or (arr[midx] < tval and sortdir == 0)):
            return binsearch(arr, stidx, midx - 1, sortdir, tval, mpos)
        else:
            return binsearch(arr, midx + 1, edidx, sortdir, tval, mpos)

pulsePos=[]
for i in range(101):
    pulsePos.append(i/10)
lastPos=0
mPos=0
px=4.5
dataLen=len(pulsePos)
print(binsearch(pulsePos, lastPos, dataLen - 1, 1, px, mPos))
