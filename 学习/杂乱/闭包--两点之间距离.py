import math


def getDIs(x1,y1,x2,y2):
    return math.sqrt((x1-x2)**2+(y1-y2)**2)

print(getDIs(1,1,2,2))


#使用闭包求两点之间距离
def GetDisOut(x1,y1):
    def GetDIsIn(x2,y2):
        return  math.sqrt((x1-x2)**2+(y1-y2)**2)
    return GetDIsIn
f = GetDisOut(2,3)
result=f(5,5)
print(result)

