"""
The simplest example of writing a tag from a PLC

NOTE: You only need to call .Close() after you are done exchanging
data with the PLC.  If you were going to read/write in a loop or read/write
more tags, you wouldn't want to call .Close() every time.
"""
from pylogix import PLC
comm = PLC()
comm.IPAddress = '192.168.250.2'
err=comm.Write('Cavity_PressureValue', 90001)
print(err)
#comm.Close()
