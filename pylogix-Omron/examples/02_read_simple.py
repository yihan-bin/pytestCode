"""
A simple single read using a with statement.

One advantage of using a with statement is that
you don't have to call .Close() when you are done,
this is handled automatically.
"""
from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '192.168.250.1'
    ret = comm.Read('Unload_HMIStart')
    print(ret.Value)
