import datetime


writename = '111.txt'
def text_save(filename,*kgw,**kwargs):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    now_time = datetime.datetime.now()
    file.writelines(str(now_time)+',')
    if kgw!=None :
        lenth=len(kgw)
        for i in kgw:
            if type(i)!= tuple:
                file.writelines(str(i)+',')
            else:
                k=i
                for x in k :
                    file.writelines(str(x) + ',')


    if kwargs :#判断列表是否为空
        file.writelines(kwargs)
    file.writelines('\n')
    file.close()
tuble1=(1232,2342,4562,67542,)
# text_save(writename,123,234,tuble1,test="jil")
text_save(writename,tuble1[1],)