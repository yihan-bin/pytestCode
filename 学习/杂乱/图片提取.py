from PIL import Image
import numpy as np
import sys


def reveal_file(imgMixed):
    bytesMixed = np.array(imgMixed).flatten()#降维打击，吧多维数组转成设定维数
    child_len = (bytesMixed[0]<<24)+(bytesMixed[1]<<16)+(bytesMixed[2]<<8)+bytesMixed[3]

    bytesChild = bytearray()

    for i in range(0,child_len):
        byteData = 0
        for index in range(0,8):
            byteData+=((bytesMixed[4+8*i +index]&0x01<<index)

        bytesChild.append(byteData)

    return bytesChild


if __name__=='__main__':
    print(sys.argv[1])#eg:在cmd里面输入 python 图片提取.py 123.jpg 那么sys.argv[1]代表的就是：图片提取.py
    print(sys.argv[2])
    imgMixed = Image.open(sys.argv[1])
    bytesChild=reveal_file(imgMixed)

    with open(sys.argv[2],'wb') as f:
        f.write(bytesChild)

