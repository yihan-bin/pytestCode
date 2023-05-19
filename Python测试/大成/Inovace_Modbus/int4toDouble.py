import struct
def int2float(a,b,c,d):
    f=0
    try:
        z0=hex(a)[2:].zfill(4) #取0x后边的部分 右对齐 左补零
        z1=hex(b)[2:].zfill(4) #取0x后边的部分 右对齐 左补零
        z2=hex(c)[2:].zfill(4) #取0x后边的部分 右对齐 左补零
        z3=hex(d)[2:].zfill(4) #取0x后边的部分 右对齐 左补零
        z=z3+z2+z1+z0 #高字节在前 低字节在后
        #z=z0+z1 #低字节在前 高字节在后
        #print (z)
        f=struct.unpack('!d', bytes.fromhex(z))[0] #返回浮点数
    except BaseException as e:
        print(e)
    return f
while True:
    a=input('请输入：')
    b=input('请输入：')
    c=input('请输入：')
    d=input('请输入：')
    f=int2float(int(a),int(b),int(c),int(d))
    print('c={0}'.format(f))