"""
Write an array of values

I have a tag called "LargeArray", which is DINT[10000]
We can write a list of values all at once to be more efficient.
You should be careful not to exceed the ~500 byte limit of
the packet.  You can pack quite a few values into 500 bytes.
"""
from pylogix import PLC

values = [8.0, 6.0, 7.0, 5.0, 3.0, 0.0, 9.0]

with PLC() as comm:
    comm.IPAddress = '192.168.250.1'
    comm.Write('test_z1[0]', values)
comm.Close()
