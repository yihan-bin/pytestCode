import numpy as np
filename = r'b.txt'
varname=[]
varvalue=[]
with open(filename,'r',encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        t=line.split('\t')
        varname.append(t[0])
        varvalue.append(list(map(float,t[1:])))
        # varvalue.append(t[1:])

print(varname)
print(varvalue)



from pylogix import PLC
comm = PLC()
comm.IPAddress = '192.168.250.1'
for i in range(len(varname)):
    if len(varvalue[i])>1:
        te=varname[i]+'[0]'
        comm.Write(te, varvalue[i])
    if len(varvalue[1])==1:
        comm.Write(varname[i], varvalue[i])

comm.Close()





# from pylogix import PLC
# comm = PLC()
# comm.IPAddress = '192.168.250.1'
# comm.Write('D6', 20)
# comm.Close()























