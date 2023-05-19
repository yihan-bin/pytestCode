import os

f = open('run_manim.bat','w')

py_file_name='first.py'
classname='BraceAnnotation'
pL=' -pl'
pm=' -pm'
str01='python -m manim '+py_file_name+' '+classname+pL
f.write(str01)
f.close()
os.system('run manim.bat')