import numpy as np
import random
import datetime
import matplotlib.pyplot as plt


class Filter():
    def __init__(self):
        self.mF_LISTLEN = 30
        self.dataCnt = 0
        self.databuf = [0.0] * 100
        self.data = [0.0] * 100
        self.OutValue = 0.0
    def filter_value(self, invalue):

        kkk = self.dataCnt
        if (self.dataCnt >= self.mF_LISTLEN):
            for i in range(self.mF_LISTLEN - 1):
                self.data[i] = self.data[i + 1]
            self.data[self.mF_LISTLEN - 1] = invalue
            self.dataCnt = self.mF_LISTLEN
        elif self.dataCnt >= 0:
            self.data[self.dataCnt] = invalue
            self.dataCnt = self.dataCnt + 1
        else:
            self.data[0] = invalue
            self.dataCnt = 1
        if self.dataCnt >= 3:
            for i in range(self.dataCnt):
                self.databuf[i] = self.data[i]
            # print(data)
            for i in range(self.dataCnt):
                for j in range(i + 1, self.dataCnt):
                    if self.databuf[i] > self.databuf[j]:
                        tempval = self.databuf[i]
                        self.databuf[i] = self.databuf[j]
                        self.databuf[j] = tempval
            # print(databuf)
            uindex = (self.dataCnt * 7 + 5) / 10 - 1
            dindex = (self.dataCnt * 3 + 5) / 10
            sum = 0
            min = int(dindex)
            max = int(uindex)
            for i in range(min, max+1):
               # xxx=range(min,max+1)
                sum = sum + self.databuf[i]
            OutValue = sum / (max + 1 - min)
            return OutValue
        elif self.dataCnt > 0:
            OutValue = self.data[self.dataCnt - 1]
            return OutValue
        else:
            OutValue = 0
            return OutValue

    def mean_filtering(self, invalue):
        data_len = 20
        global data_t
        global i
        if i < data_len:
            data_t.append(invalue)
            i = i + 1
            return np.mean(data_t)

        if i >= data_len:
            j = np.mod(i, data_len)
            i = i + 1

            data_t[j] = invalue
            return np.mean(data_t)


def text_save(filename, data, data2):  # filename为写入CSV文件的路径，data为要写入数据列表.
    file = open(filename, 'a')
    now_time = datetime.datetime.now()
    #    time1_str = datetime.datetime.strftime(now_time,%H:%M:%S')
    da_str = str(data)
    da2_str = str(data2)
    file.writelines(str(now_time) + ',' + da_str + ',' + da2_str + '\n')

    file.close()


if __name__ == '__main__':
    a = 0
    data_t = []
    i = 0
    len_t = 500
    x = np.arange(len_t)
    y1 = np.zeros_like(x, dtype='float')
    y2 = np.zeros_like(x)
    y3 = np.zeros_like(x)

    cal = Filter()
    while (a < (len_t / 2)):
        writename = '222.txt'
        value = random.uniform(0, 5)

        output = cal.filter_value(value)
        output2 = cal.mean_filtering(value)
        # text_save(writename, value,output)

        y1[a] = value
        y2[a] = output
        y3[a] = output2
        a = a + 1
    while (a < len_t - 1):
        writename = '222.txt'
        value = random.uniform(0, 10)


        output = cal.filter_value(value)
        # text_save(writename, value,output)
        output2 = cal.mean_filtering(value)
        a = a + 1

        y1[a] = value
        y2[a] = output
        y3[a] = output2

    plt.plot(x, y1, color='black', linewidth=1.5, label='Nosiy')
    plt.plot(x, y2, color='blue', linewidth=2, label='Clean')
    plt.plot(x, y3, color='red', linewidth=2, label='Clean2')
    plt.xlim(x[0], x[-1])
    plt.show()
