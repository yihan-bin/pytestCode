"""
The simplest example of reading a tag from a PLC

NOTE: You only need to call .Close() after you are done exchanging
data with the PLC.  If you were going to read in a loop or read
more tags, you wouldn't want to call .Close() every time.
"""
from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '192.168.250.2'
    ret = comm.Read('Cavity_VacuumUp[1]',10,)
    print(ret.Value)


# from pylogix import PLC
#
# with PLC() as comm:
#     comm.IPAddress = '192.168.250.2'
#     ret = comm.Read('Cavity_ModbusReadData[201]',100, datatype=0xd2)
#     print(ret.Value)

#
# import datetime
# import numpy as np
# t=datetime.datetime.now()
# lastT=datetime.datetime.now()
#
# A=[1,2,3,4,5]
# # with open('temp.txt', 'w', encoding='utf-8') as f:
# #     f.writelines(str(t) + str(A))
# from pylogix import PLC
#
# with PLC() as comm:
#         # for data in temp:
#         #     i = str(data[1]).strip('[').strip(']').replace(',', '\t').replace('\'', '')
#         #     f.writelines(data[0] + '\t' + i + '\n')
#     comm.IPAddress = '192.168.250.2'
#     while True:
#             t=datetime.datetime.now()
#             if t.second!=lastT.second:
#                 ret = comm.Read('Cavity_ModbusReadData[201]',100, datatype=0xd2)
#                 print(ret.Value)
#                 array=list(ret.Value)
#                 array=[x/100 for x in array]
#                 with open('temp.txt', 'a', encoding='utf-8') as f:
#                     f.writelines(str(t)+'\t'+str(array).strip('[').strip(']')+'\n')
#                 f.close()
#                 lastT = t