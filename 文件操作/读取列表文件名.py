import os
import sys
from pathlib import Path
def readname():
    filePath = 'F:\\桌面\\left\\'
    dir_list = os.listdir(filePath)
    print(dir_list)
    dir_list=sorted(dir_list,key=lambda x:os.path.getmtime(os.path.join(filePath,x)))
    return dir_list


if __name__ == "__main__":
    name = readname()
    name.sort()
    print(name)
    for i in name:
        if '.' in i:
            print(i)
        else:
            print('文件夹')

    FILE = Path(__file__).resolve()
    print('*'*30)
    print(FILE)
    ROOT = FILE.parents[0]  # YOLOv5 root directory
    print(ROOT)
    if str(ROOT) not in sys.path:
        sys.path.append(str(ROOT))  # add ROOT to PATH
    ROOT = Path(os.path.relpath(ROOT, Path.cwd()))  # relative
    print(ROOT)