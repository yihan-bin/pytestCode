import numpy
import random
import datetime
class Filter():


    def filter_value(Invalue):
        global mF_LISTLEN
        global dataCnt
        global databuf
        global data
        global OutValue
        kkk=dataCnt
        if (dataCnt>=mF_LISTLEN):
            for i in range(mF_LISTLEN-2):
                data[i]=data[i+1]
            data[mF_LISTLEN-1]=Invalue
            dataCnt=mF_LISTLEN
        elif dataCnt>=0:
            data[dataCnt]=Invalue
            dataCnt=dataCnt+1
        else:
            data[0]=Invalue
            dataCnt=1
        if dataCnt>=3:
            for i in range(dataCnt-1):
                databuf[i]=data[i]
            for i in range(dataCnt-1):
                for j in range(i+1,dataCnt-1):
                    if databuf[i]>databuf[j]:
                        tempval=databuf[i]
                        databuf[i]=databuf[j]
                        databuf[j]=tempval

            uindex = (dataCnt * 7 + 5) / 10 - 1
            dindex = (dataCnt * 3 + 5) / 10
            sum = 0
            min=int(dindex)
            max=int(uindex)
            for i in range(min,max):
                sum = sum + databuf[i]
            OutValue = sum / (uindex + 1 - dindex)
            return OutValue
        elif dataCnt>0:
            OutValue=data[dataCnt-1]
            return OutValue
        else:
            OutValue=0
            return OutValue
def text_save(filename, data,data2):#filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename,'a')
    now_time = datetime.datetime.now()
#    time1_str = datetime.datetime.strftime(now_time,%H:%M:%S')
    da_str=str(data)
    da2_str=str(data2)
    file.writelines(str(now_time)+','+da_str+','+da2_str+'\n')

    file.close()

if __name__ == '__main__':
    a=0
    b=0
    dataCnt = 0
    databuf = [0.0]*100
    data = [0.0]*100
    OutValue = 0.0
    mF_LISTLEN = 50
    cal = Filter
    while(a<1000):

        writename = '数据/111.txt'
        value=random.uniform(0,8)


        output=cal.filter_value(value)
        text_save(writename, value,output)

        a=a+1
    while(b<500):

        writename = '数据/111.txt'
        value=50#random.uniform(0,100)
        cal=Filter

        output=cal.filter_value(value)
        text_save(writename, value,output)

        b=b+1


