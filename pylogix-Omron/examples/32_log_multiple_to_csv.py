"""
We're going to log a few tag values 10
times to a CSV file

For the first row, we'll write tag names,
then log each set of values with each read
"""
import csv
import time
from pylogix import PLC

with PLC() as comm:
    comm.IPAddress = '192.168.1.9'
    tags = ['Zone1ASpeed', 'Zone1BSpeed', 'Zone2ASpeed', 'Zone2BSpeed']
    with open('32_log.csv', 'w') as csv_file:
        csv_file = csv.writer(csv_file, delimiter=',', lineterminator='\n', quotechar='/', quoting=csv.QUOTE_MINIMAL)
        csv_file.writerow(tags)
        for i in range(10):
            ret = comm.Read(tags)
            row = [x.Value for x in ret]
            csv_file.writerow(row)
            time.sleep(1)
