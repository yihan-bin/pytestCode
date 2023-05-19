"""
This shows using the large forward open to increase
the packet size.  This will only have a benefit when
reading large chunks of data, like in this example,
we're reading 20,000 values from the tag YugeArray

NOTE: LargeForwardOpen is not supported on all
controllers and was introduced in v20
"""
from pylogix import PLC
with PLC() as comm:
    comm.IPAddress = '192.168.1.9'
    comm.ConnectionSize = 4000
    ret = comm.Read('YugeArray[0]', 20000)
