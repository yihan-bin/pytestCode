import math
def _RotateThransform(point,angle):
		angle = angle*math.pi/180
		x = point[0]*math.cos(angle)+point[1]*math.sin(angle)
		y = -point[0]*math.sin(angle)+point[1]*math.cos(angle)
		return x,y
		
def Local2Global(LocalPoint,OriginalPoint,OriginalAngle):
    """
    说明：在全局坐标系O中，由已知坐标A和方向Theta建立局部坐标系O'，计算局部坐标系O'下某点坐标B在全局坐标O中的坐标。
    输入：\'LocalPoint\'为局部坐标下的位置，\'OriginalPoint\'为局部坐标系在全局坐标系的位置，\'OriginalAngle\'为局部坐标系在全局坐标系的角度。
    结果：返回坐标(x,y)
    例子：图像坐标系下，已知矩形中心点A的位置和矩形角度，以及矩形上一点B相对于矩形中心的位置，计算B点在图像坐标下的位置。
        ###第一步：以矩形中心点A位置和矩形角度，建立局部坐标系，并设置B点在局部坐标系下的位置
    	◆ OriginalPoint = (200,200)
        ◆ OriginalAngle = 30
        ◆ LocalPoint = (100,0)
        ###第二步：计算B点在全局坐标系下的位置
        ◆ Point = Local2Global(LocalPoint,OriginalPoint,OriginalAngle)
        ◆ print(Point)
    """
    rotatept = _RotateThransform(LocalPoint,-OriginalAngle)
    x = rotatept[0] + OriginalPoint[0]
    y = rotatept[1] + OriginalPoint[1]
    return round(x,6),round(y,6)


def Global2Local(GlobalPoint,OriginalPoint,OriginalAngle):	
    """
    说明：在全局坐标系O中，由已知坐标A和方向Theta建立局部坐标系O'，计算全局坐标系O下某点坐标B在局部坐标O'中的坐标。
    输入：\'GlobalPoint\'为全局坐标下的位置，\'OriginalPoint\'为全局坐标系在局部坐标系的位置，\'OriginalAngle\'为全局坐标系在局部坐标系的角度。
    结果：返回坐标(x,y)
    例子：图像坐标系下，已知矩形中心点A的位置和矩形角度，以及矩形上一点B在图像坐标系下的位置，计算B点相对于矩形中心点A的位置。
        ###第一步：以矩形中心点A位置和矩形角度，建立局部坐标系，并设置B点在全局坐标系下的位置
    	◆ OriginalPoint = (200,200)
        ◆ OriginalAngle = 30
        ◆ GlobalPoint = (100,0)
        ###第二步：计算B点在局部坐标系下的位置
        ◆ Point = Global2Local(GlobalPoint,OriginalPoint,OriginalAngle)
        ◆ print(Point)
    """
    localpt = (GlobalPoint[0] - OriginalPoint[0],GlobalPoint[1] - OriginalPoint[1])
    globalpt = _RotateThransform(localpt,OriginalAngle)
    x = globalpt[0]
    y = globalpt[1]
    return round(x,6),round(y,6)
	
def RotateAroundPoint(StartPoint,CenterPoint,Angle):
    """
    说明：计算起点A，绕中心点B旋转Theta角度后的位置。
    输入：\'StartPoint\'为起点的位置，\'CenterPoint\'为旋转中心位置，\'OriginalAngle\'为旋转角度。
    结果：返回坐标(x,y)
    例子：
    	◆ StartPoint = (100,0)
    	◆ CenterPoint = (200,200)
        ◆ Angle = 30
        ◆ RotatePoint = RotateAroundPoint(StartPoint,CenterPoint,Angle)
        ◆ print(RotatePoint)
    """
    Angle = Angle*math.pi/180
    x = (StartPoint[0] - CenterPoint[0]) * math.cos(Angle) - (StartPoint[1] - CenterPoint[1]) * math.sin(Angle) + CenterPoint[0];
    y = (StartPoint[0] - CenterPoint[0]) * math.sin(Angle) + (StartPoint[1] - CenterPoint[1]) * math.cos(Angle) + CenterPoint[1];
    return round(x,6),round(y,6)
	

def Point2PointCenter(Point1,Point2):		
    """
    说明：计算两点的中点坐标。
    输入：\'Point1\'为起点，\'Point2\'为终点
    结果：返回坐标(x,y)
    例子：
    	◆ Point1 = (100,0)
    	◆ Point2 = (200,200)
        ◆ CenterPoint = Point2PointCenter(Point1,Point2)
        ◆ print(CenterPoint)
    """
    x = Point1[0]/2.0 + Point2[0]/2.0
    y = Point1[1]/2.0 + Point2[1]/2.0
    return round(x,6),round(y,6)


def Point2PointDistance(Point1,Point2):	
    """
    说明：计算两点的距离。
    输入：\'Point1\'为起点，\'Point2\'为终点
    结果：返回坐标(x,y)
    例子：
    	◆ Point1 = (100,0)
    	◆ Point2 = (200,200)
        ◆ Distance = Point2PointDistance(Point1,Point2)
        ◆ print(Distance)
    """
    len = math.pow(Point2[1] - Point1[1],2)+math.pow(Point2[0] - Point1[0],2)
    return round(math.sqrt(len),6)


def Point2PointAngle(Point1,Point2):	
    """
    说明：计算两点连线的角度。
    输入：\'Point1\'为起点，\'Point2\'为终点
    结果：返回坐标(x,y)
    例子：
    	◆ Point1 = (100,0)
    	◆ Point2 = (200,200)
        ◆ Angle = Point2PointAngle(Point1,Point2)
        ◆ print(Angle)
    """
    angle = math.atan2(Point2[1] - Point1[1],Point2[0] - Point1[0])*180/math.pi
    return round(angle,6)
	

def Point2LineFoot(Point,Line):	
    """
    说明：计算点到直线的垂足。
    输入：\'Point\'为起点，\'Line\'为直线，直线的结构为(startx,starty,endx,endy)。
    结果：返回坐标(x,y)
    例子：
    	◆ Point = (100,0)
    	◆ Line = (200,200,400,400)
        ◆ FootPoint = Point2LineFoot(Point,Line)
        ◆ print(FootPoint)
    """
    LinePt1 = (Line[0],Line[1])
    LinePt2 = (Line[2],Line[3])
    A = LinePt2[1] - LinePt1[1] 
    B = LinePt1[0] - LinePt2[0]
    C = LinePt2[0]*LinePt1[1] - LinePt1[0]*LinePt2[1]
    if(A*A + B*B < 1e-6):
    	x = LinePt1[0]
    	y = LinePt1[1]
    	return round(x,6),round(y,6)
    elif(math.fabs(A*Point[0]+B*Point[1]+C)<1e-6):
    	x = Point[0]
    	y = Point[1]
    	return round(x,6),round(y,6)
    else:
    	x = (B*B*Point[0] - A*B*Point[1] - A*C)/(A*A + B*B)
    	y = (-A*B*Point[0] + A*A*Point[1] -B*C)/(A*A + B*B)
    	return round(x,6),round(y,6)	


def Point2LineDistance(Point,Line):	
    """
    说明：计算点到直线的距离。
    输入：\'Point\'为起点，\'Line\'为直线，直线的结构为(startx,starty,endx,endy)。
    结果：返回坐标(x,y)
    例子：
    	◆ Point = (100,0)
    	◆ Line = (200,200,400,400)
        ◆ Distance = Point2LineDistance(Point,Line)
        ◆ print(Distance)
    """
    LinePt1 = (Line[0],Line[1])
    LinePt2 = (Line[2],Line[3])
    dis = 0
    if(LinePt1[0] == LinePt2[0]):
    	if(LinePt1[1] == LinePt2[1]):
    		dx = Point[0] - LinePt1[0]
    		dy = Point[1] - LinePt1[1]
    		dis = math.sqrt(dx*dx+dy*dy)
    	else:
    		dis = math.fabs(Point[0] - LinePt1[0])
    else:
    	A = (LinePt2[1] - LinePt1[1])/(LinePt2[0] - LinePt1[0])
    	B = (LinePt2[0]*LinePt1[1] - LinePt1[0] * LinePt2[1])/(LinePt2[0] - LinePt1[0])
    	dis = math.fabs(A*Point[0] - Point[1] + B)/(math.sqrt(A*A+1))
        
    return round(dis,6)	

###从两点式转换到线参数模式
def _getLineParamFromLine (Line):
    a = 0
    b = 0
    c = 0
    if Line[0] != Line[2] or Line[1] != Line[3]:
        a = Line[3] - Line[1]
        b = Line[0] - Line[2]
        c = Line[2] * Line[1] - Line[0] * Line[3]
    else:
        raise Exception("起始终止点位置相同")
    
    return (a,b,c)

def Line2LineCross(Line1,Line2):	
    """
    说明：计算直线与直线的交点。
    输入：\'Line1\'为直线1，\'Line2\'为直线2，直线的结构为(startx,starty,endx,endy)。
    结果：返回坐标(x,y)
    例子：
    	◆ Line1 = (400,400,200,200)
    	◆ Line2 = (200,200,400,400)
        ◆ CrossPoint = Line2LineCross(Line1,Line2)
        ◆ print(CrossPoint)
    """
    x = 0
    y = 0   
    
    try:
        line1abc = _getLineParamFromLine(Line1)
    except:
        raise Exception("输入line1起始终止点位置相同")
    
    try:
        line2abc = _getLineParamFromLine(Line2)
    except:
        raise Exception("输入line2起始终止点位置相同")
    
    a1 = line1abc[0]
    b1 = line1abc[1]
    c1 = line1abc[2]
    a2 = line2abc[0]
    b2 = line2abc[1]
    c2 = line2abc[2]    
    c1 *= -1
    c2 *= -1
    
    fenMu = a1 * b2 - a2 * b1 

    if (abs(fenMu) < 0.000001):
        return (x,y)
    else:
        fenZi1 = c1 * b2 - c2 * b1
        fenZi2 = a1 * c2 - a2 * c1
        
        x = fenZi1 / fenMu
        y = fenZi2 / fenMu
    	
        return (round(x,6),round(y,6))	
    	
 

def Line2LineDistance(Line1,Line2):	
    """
    说明：计算直线与直线的距离。
    输入：\'Line1\'为直线1，\'Line2\'为直线2，直线的结构为(startx,starty,endx,endy)。
    结果：返回坐标(x,y)
    例子：
    	◆ Line1 = (400,400,200,200)
    	◆ Line2 = (200,200,400,400)
        ◆ Distance = Line2LineDistance(Line1,Line2)
        ◆ print(Distance)
    """
    cenx = (Line1[0] + Line1[2]) / 2
    ceny = (Line1[1] + Line1[3]) / 2
    dis = Point2LineDistance((cenx, ceny), Line2)
    return round(dis,6)
	

# 获取列表的第二个元素
def _sortSecond(elem):
    return elem[1]

# 获取列表的第一个元素
def _sortFirst(elem):
    return elem[0]

def GetRectDirLine(rotRect, direction):
    """
    说明：计算旋转矩形的方向的边。
    输入：\'rotRect\'为旋转矩形，旋转矩形的结构为(cenX, cenY, mainAxis, viceAxis, angle),
    \'direction\'为特定方向，'left':左侧边，'right':右侧边， 'top':上边 'bottom':下边。
    结果：返回边(startptx,startpty,endptx,endpty,angle)
    例子：
    	◆ rotRect = (100,100,200,200,45)
    	◆ direction = 'left'
        ◆ Line = GetRectDirLine(rotRect,direction)
        ◆ print(Line)
    """
    cenX = rotRect[0]
    cenY = rotRect[1]
    halfmainAxis = rotRect[2] / 2
    halfviceAxis = rotRect[3] / 2
    angle = rotRect[4] * 3.1415926 / 180
    c = math.cos(angle)
    s = math.sin(angle)

    posList = []    
    dirList = []
    rtnLine = []

    #右上角点
    x =  halfmainAxis
    y = -halfviceAxis
    posX = x * c - y * s + cenX
    posY = x * s + y * c + cenY
    posList.append((posX, posY))
    x = 1
    y = 0
    index = 0
    posX = x * c - y * s 
    posY = x * s + y * c 
    dirList.append((posX, posY, index))

    #右下角点
    x = +halfmainAxis
    y = +halfviceAxis
    posX = x * c - y * s + cenX
    posY = x * s + y * c + cenY
    posList.append((posX, posY))
    x = 0
    y = 1
    index = 1
    posX = x * c - y * s 
    posY = x * s + y * c 
    dirList.append((posX, posY, index))

    #左下角点
    x = -halfmainAxis
    y = +halfviceAxis
    posX = x * c - y * s + cenX
    posY = x * s + y * c + cenY
    posList.append((posX, posY))
    x = -1
    y = 0
    index = 2
    posX = x * c - y * s 
    posY = x * s + y * c 
    dirList.append((posX, posY, index))

    #左上角点
    x = -halfmainAxis
    y = -halfviceAxis
    posX = x * c - y * s + cenX
    posY = x * s + y * c + cenY
    posList.append((posX, posY))
    x = 0
    y = -1
    index = 3
    posX = x * c - y * s 
    posY = x * s + y * c 
    dirList.append((posX, posY, index))

    #print(posList)

    if direction == 'left': #左时，则按x排序
    	dirList.sort(key=_sortFirst)
    	s = dirList[0][2]
    	sp = (s+1)%4
    	rtnLine = (posList[s][0], posList[s][1], posList[sp][0], posList[sp][1],  0)
        
    elif direction == 'right': #右时，按x排序
    	dirList.sort(key=_sortFirst)
    	s = dirList[3][2]
    	sp = (s+1)%4
    	rtnLine = (posList[s][0], posList[s][1], posList[sp][0], posList[sp][1],  0)
        
    elif direction == 'top': #上时，按y排序
    	dirList.sort(key=_sortSecond)
    	s = dirList[0][2]
    	sp = (s+1)%4
    	rtnLine = (posList[s][0], posList[s][1], posList[sp][0], posList[sp][1],  0)
        
    elif direction == 'bottom': #下时，按y排序
    	dirList.sort(key=_sortSecond)
    	s = dirList[3][2]
    	sp = (s+1)%4
    	rtnLine = (posList[s][0], posList[s][1], posList[sp][0], posList[sp][1],  0)
        
    else:
    	rtnLine = (0,0,0,0, 0)
        
    diffX = rtnLine[2] - rtnLine[0]
    diffY = rtnLine[3] - rtnLine[1]
    angle = math.atan2(diffY, diffX) * 180 / 3.1415926


    return rtnLine[0], rtnLine[1], rtnLine[2], rtnLine[3], angle
	

	
def SortByXYPos(PosDatas, y_Increase, x_Increase, minMargin):
    """
    说明：排序函数，对XY列表数据进行排序。
    输入：\'PosDatas\'为包含xy数据的列表，结构为(x, y, ...)，y_Increase,True表示y增大顺序，False表示y减小顺序，
    x_Increase，True表示x增大顺序，False表示x减小顺序,minMargin: 表示行列间隔的距离，一般以行距的一半即可，小于该值将被分到一行或一列。
    结果：返回为排序后的列表数据
    例子：
    	◆ PosDatas = (100,200,101,201,301,401)
    	◆ y_Increase = False
        ◆ x_Increase = True
        ◆ minMargin = 20
        ◆ ResultXY = SortByXYPos(PosDatas,y_Increase,x_Increase,minMargin)
        ◆ print(ResultXY)
    """
    num = len(PosDatas)

    #先排序y
    PosDatas.sort(key=_sortSecond, reverse = not y_Increase)
    linePosIndex = []  
    for i in range(0, num-1):      
        posCur = PosDatas[i]   
        posNext = PosDatas[i+1]        
        if abs(posNext[1] - posCur[1]) < minMargin:
            linePosIndex.append(0)
        else:
            linePosIndex.append(1)
    linePosIndex.append(0)

    sortAllPosY = []
    linePos = []
    for i in range(0, num):    
        if linePosIndex[i] == 0:
            linePos.append(PosDatas[i])
        else:
            linePos.append(PosDatas[i])
            sortAllPosY.append(linePos)
            linePos = []        
    if len(linePos) != 0:
        sortAllPosY.append(linePos)
            

    for i in range(0,len(sortAllPosY)):
        sortAllPosY[i].sort(key=_sortFirst, reverse=not x_Increase)


    newSortedPos = []
    for i in range(0,len(sortAllPosY)):
        for j in range(0, len(sortAllPosY[i])):
            newSortedPos.append(sortAllPosY[i][j])
            
    return newSortedPos

