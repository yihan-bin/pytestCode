from pylogix import PLC
import numpy as np

# with open("mm.txt",'r') as f:
#     X_Y_str=f.readlines()
#     X_Y=[i.split(",") for i in X_Y_str]
#     print(X_Y)

a=np.loadtxt("mm.txt",delimiter=",")
print(a)
with PLC() as comm:
    comm.IPAddress = '192.168.250.1'
    for x_y in a:
        x1 = comm.Write('Load_GetCellXAxis1_WorkPos1[0]', x_y[0], datatype=202)
        y1 = comm.Write('Load_GetCellXAxis1_WorkPos1[1]', x_y[1], datatype=202)
        e= comm.Write('In_CylinderCtrl[1].ToWork[1]', True,datatype=193)
        while(not (comm.Read('Load_GetPressure_I',datatype=193).Value[0])):
            pass

