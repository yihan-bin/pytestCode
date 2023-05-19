"""
We're going to log a tag value 10
times to a text file
"""
from pylogix import PLC
import time

with PLC() as comm:
    comm.IPAddress = '192.168.1.9'

    with open('30_log.txt', 'w') as txt_file:
        for i in range(10):
            ret = comm.Read('LargeArray[50]')
            txt_file.write(str(ret.Value)+'\n')
            time.sleep(1)
