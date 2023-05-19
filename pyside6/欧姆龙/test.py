import socket, struct
import pandas as pd
import time, datetime
from PyQt5 import QtCore

pd.set_option('display.max_columns', None)  # 显示所有列
pd.set_option('display.max_rows', None)  # 显示所有行


class FinsSocketClass(QtCore.QObject):
    """
    used:
    Omron Fins socket com.V0.0.1 for used NJ301-1200CPU. Writed by tcy shanghai songjiang  2019/5/13
    You can used the word,bit.
    remark:
    REAL32 有效数据位2位;REAL64 有效数据17位
    """
    sin_s = QtCore.pyqtSignal(object)
    sin_s_ok = QtCore.pyqtSignal(object)

    def __init__(self, ip='10.110.59.192', ip_plc='10.110.59.33', port=9600):
        self.ip = ip
        self.ip_plc = ip_plc
        self.port = port

        self.s, self.s_ok, self.s_coning, self.com_err = None, False, False, False

        super(FinsSocketClass, self).__init__()

        _python_type = ['h', 'i', 'q', 'H', 'I', 'Q', 'f', 'd', 's', '?']
        _plc_type = ['INT16', 'INT32', 'INT64', 'UINT16', 'UINT32', 'UINT64', 'REAL32', 'REAL64', 'STR', 'BOOL']
        self.data_type = pd.Series(data=_python_type, index=_plc_type)

    def __del__(self):
        self.ip = ''
        self.ip_plc = ''
        self.port = 9600

        self.s, self.s_ok, self.s_coning, self.com_err = None, False, False, False
        # self.sin_s.emit(None);self.sin_s_ok.emit(False)
        self.close_socket()

    def __try_connect(self, try_conMode=False):
        """
        :param try_conMode: True mean test the fins connect ok or ng.
        :return: None
        """
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if try_conMode: s.settimeout(1)
            # self.s.setblocking(False)#非阻塞模式
            s.connect((self.ip_plc, 9600))
            if try_conMode:
                s.getpeername()  # ('192.168.115.33', 9600)
                s.close()
            else:
                self.s, self.s_ok, self.s_coning, self.com_err = s, True, False, False
                self.sin_s.emit(s);
                self.sin_s_ok.emit(True)
            return None
        except Exception as e:
            self.s, self.s_ok = None, False
            self.sin_s.emit(None);
            self.sin_s_ok.emit(False)
            return -1

    def __connect(self, timeout=0):
        """
        used:connect the server used the default value.
        :param timeout: >0 choose the auto connect after the err generate.
        :return:None
        """
        if not self.__try_connect(try_conMode=True):
            return self.__try_connect(try_conMode=False)
        else:
            if timeout <= 0: print('Connect Err!Please connect after hand check.');return -1
            print('Connect Err!Auto connect start...')

            while True:  # not self.s_ok
                self.s_coning = True
                time.sleep(timeout)
                print('Waited Fins Connect......')
                if not self.__try_connect(try_conMode=True):
                    if not self.__try_connect(try_conMode=False):
                        self.s_coning = False;
                        self.com_err = False
                        break

            return None

    def close_socket(self):
        try:
            self.s.shutdown(socket.SHUT_RDWR)
            self.s.close()
            a = None
        except Exception as e:
            a = -1
        finally:
            self.s = None;
            self.s_ok = False
            # self.sin_s.emit(None);self.sin_s_ok.emit(False)
            return a

    def __node(self, ip=''):  # From the ip address to _node NO. 2 bit hex str
        nodeStr = hex(int(ip.split('.')[3]))[2:]
        return ('0' + nodeStr)[-2:]

    def __existErr(self, BackValue=b'', shakeHandMode=False):
        if len(BackValue) < 16:
            return True
        v = BackValue
        b = (v[12] == 0) and (v[13] == 0) and (v[14] == 0) and (v[15] == 0)

        if not shakeHandMode:  # read write fins
            if len(BackValue) < 30: return True
            b = b and (v[28] == 0) and (v[29] == 0)

        return not b

    def con(self, timeout=1):  # timeout >0 auto connect mode
        """
        :param timeout: auto connect Mode :set timeout time
        :return: socket object or None
        """
        if self.__connect(timeout=timeout): return None  # Have error,Not connect
        shakeHandsStr = '46494E530000000C0000000000000000000000'
        shakeHandsStr = shakeHandsStr + self.__node(self.ip)

        try:
            self.s.send(bytes.fromhex(shakeHandsStr))
            BackValue = self.s.recv(1024)
            a = -1 if self.__existErr(BackValue, True) else None
        except Exception as e:
            a = -1
        finally:
            if a == -1:
                self.sin_s.emit(None);
                self.sin_s_ok.emit(False)
                self.s, self.s_ok = None, False
            return -1 if a else None

    def __dataType_n(self, data_type=''):  # word 16 bit =1
        offset = 1
        if (data_type == 'h') or (data_type == 'H') or (data_type == 's'):
            offset = 1
        elif (data_type == 'i') or (data_type == 'I') or (data_type == 'f'):
            offset = 2
        elif (data_type == 'q') or (data_type == 'Q') or (data_type == 'd'):
            offset = 4
        return offset

    def __dec_to_hex_n(self, data=None, strOrderMode=False):  # 1 byte
        """
        :param data:
        :param strOrderMode: 2 pcs str equal 1 byte.Having 3 mode
                             mode1: data length;mode2:str number;mode3:hex number
        :return:str: hex str n
        """
        if isinstance(data, str):
            str_n = '0000' + hex(int(len(data) / 2) if strOrderMode else int(data))[2:]
        else:
            str_n = '0000' + hex(data)[2:]
        return str_n[-4:].upper()

    def __adrWordBit_map(self, address='D0'):
        """
        Used:Split the address like 'D0' to address ('D') ,word('0'),bit('00')
        :param address: str
        :return: str normal addreass of PLC map fins to communication.
        """
        lst = address.split('.')
        exist_bit = (False if address.find('.') == -1 else True)
        if len(lst[0]) < 2: return '';adr = ''

        word_ = self.__dec_to_hex_n(lst[0][1:])
        word_bit = ('00' + self.__dec_to_hex_n(lst[1]))[-2:] if exist_bit else '00'

        if lst[0][0] == 'D':
            adr = '82';word_bit = '00'  # word_+bit
        elif lst[0][0] == 'H':
            adr = 'B2' if not exist_bit else '32'
        elif lst[0][0] == 'W':
            adr = 'B1' if not exist_bit else '31'
        elif len(lst) >= 4:
            if lst[0][0:3] == 'CIO':
                adr = 'B0' if not exist_bit else '30';
                word_ = self.__dec_to_hex_n(lst[0][3:])
            else:
                adr = '';word_ = '';word_bit = ''
        else:
            adr = '';word_ = '';word_bit = ''
        return adr + word_ + word_bit  # adr+word_+bit


    def __strOrder(self, address='D0', length=0, data_type='', read_model=False, data=None):
        offset = self.__dataType_n(data_type)
        read_write = '0101' if read_model else '0102'

        str1 = '000000020000000080000200' + self.__node(self.ip_plc) + '0000'
        str1 = str1 + self.__node(self.ip) + '0000' + read_write + self.__adrWordBit_map(address)  # word+bit
        str1 = str1 + self.__dec_to_hex_n(length * offset)  # data length

        if read_model == False:
            str1 = str1 + self.__data_to_hex(data, data_type)  # data
        return '46494E530000' + self.__dec_to_hex_n(str1, True) + str1


    def __TypeExchange(self, data=b''):
        n = len(data)
        barr = bytearray(n)
        for i in range(0, n, 2):
            barr[i] = data[i + 1]
            barr[i + 1] = data[i]
        return barr


    def __data_to_hex(self, data=None, data_type=''):
        lst = []
        if data:
            for i in data:
                b1 = struct.pack(data_type, i)  # byte
                b = (data_type != self.data_type.BOOL) and (data_type != self.data_type.STR)
                b1 = (self.__TypeExchange(b1) if b else b1)
                lst.append(b1)

            if (data_type == self.data_type.BOOL): lst.reverse()
        b1 = b''.join(lst)
        return b1.hex()


    def __byte_decode(self, data=b'', data_type='', length=0):
        b = (data_type != self.data_type.BOOL) and (data_type != self.data_type.STR)
        b_arr = (self.__TypeExchange(data) if b else data)
        fmt = str(int(length)) + data_type

        return struct.unpack(fmt, b_arr)


    def __DataAdr(self, address='D0', length=0, data_type=''):
        """
        used:Produce the writed address of PLC
        :param address: str
        :param length: int
        :param data_type: str
        :return: list
        """
        offset = self.__dataType_n(data_type)

        adr = '';
        bit_str = ''
        exist_bit = (False if address.find('.') == -1 else True)
        if exist_bit:
            if len(address) < 2: return []
            adr = address.split('.')[0];
            bit_str = address.split('.')[1]
        else:
            adr = address

        if exist_bit:
            adr_name = '';
            adr_start_number = 0;
            bit_start_number = 0;
            tmp = []
            if adr[0] == 'C':
                if len(adr) < 4: return []
                adr_name = adr[0:3];
                adr_start_number = int(adr[3:])
            else:
                adr_name = adr[0];
                adr_start_number = int(adr[1:])

            bit_start_number = int(bit_str)
            if bit_start_number >= 16: return []
            n1 = adr_start_number;
            n2 = bit_start_number;

            for i in range(length):
                tmp.append(adr_name + str(n1) + '.' + ('00' + str(n2))[-2:])
                n2 += 1
                if n2 >= 16: n2 = 0;n1 += 1

            return tmp
        else:
            if adr[0] == 'C':
                if len(adr) <= 3: return []
                n0 = int(adr[3:])
                return [adr[0:3] + '.' + (('00' + str(i))[-2:]) for i in range(n0, n0 + length * offset, offset)]
            else:
                if len(adr) <= 1: return []
                n0 = int(adr[1:])

                return [adr[0:1] + str(i) for i in range(n0, n0 + length * offset, offset)]


    def exist_con(self):
        try:
            return self.s.getpeername()
        except Exception as e:
            return None

    # =============================================================================================
    def readData(self, address='D0', length=0, data_type='', back_s=False):
        """
        :param address: address format D+Number; D:address name;Number:decimal.
        :param length: length int >0;number is 1,2,4 (16,32,64) int or float.
                You alse can use the str.1 word 16bit
        :param data_type:str
        :return: None or tupe or str Series
        """
        backEmptyValue = pd.Series() if back_s else None

        strOrder = self.__strOrder(address, length, data_type, True)
        try:
            self.s.send(bytes.fromhex(strOrder))
            BackValue = self.s.recv(1024)  # b'FINS\x00\x00\...'
        except Exception as e:
            self.sin_s.emit(None);
            self.sin_s_ok.emit(False)
            self.s = None;
            self.s_ok = False
            return backEmptyValue

        if (len(BackValue) <= 30) or self.__existErr(BackValue):
            self.com_err = True
            return backEmptyValue

        data = self.__byte_decode(data=BackValue[30:], data_type=data_type, length=length)
        data = list(data)
        data_adr = self.__DataAdr(address=address, length=length, data_type=data_type)

        # return data_adr if back_s else data
        # if (data_type=='?') and (back_s==False):data.reverse()#bool data left is high bit
        return (pd.Series(data, index=data_adr) if back_s else data)

    # =============================================================================================
    def writeData(self, address='D100', data=None, data_type=''):
        """
        :param address: str
        :param data: list decimal
        :return:None or -1
        """
        a = None
        if type(data) == type(pd.Series()): data = data.tolist()
        if isinstance(data, (str, int, float, bytes)): data = [data]
        # print('222222222222============',address,data,data_type)
        strOrder = self.__strOrder(address, len(data), data_type, False, data)  # 46494E53...
        # print('222222222222============',strOrder)
        try:
            self.s.send(bytes.fromhex(strOrder))
            BackValue = self.s.recv(1024)  # b'FINS\x00\x00\x00\...'#46494e5300000016000...
        except Exception as e:
            self.sin_s.emit(None);
            self.sin_s_ok.emit(False)
            self.s = None;
            self.s_ok = False;
            a = -1
            return a

        if self.__existErr(BackValue):
            a = -1;
            self.com_err = True;  # errOccur=True
        return a

    def rw_socket(self, adr='', data_or_len=[], data_type='?', r_mode=False, back_s=False):
        if r_mode:
            return self.readData(address=adr, length=data_or_len, data_type=data_type, back_s=back_s)
        else:
            return self.writeData(address=adr, data=data_or_len, data_type=data_type)


def test_fins_socket(ip='192.168.250.89', ip_plc='192.168.250.1'):
    s = FinsSocketClass(ip, ip_plc)
    # print(s.fileno())  # 212
    s.con()  # 默认发生错误自动连接，设置为0取消自动连接

    test_read_bit(s)
    test_write_bit(s)

    test_read_D(s)
    test_write_D(s)

    test_read_H(s)
    test_Write_H(s)
    s.close_socket()


def test_read_bit(s):
    print('1.1.bit=', s.readData('H1002.00', 16, s.data_type.BOOL))  # back list
    print('1.2.bit=', s.readData('H1002.00', 16, s.data_type.BOOL, True))  # back Series
    # 1.1.bit= [False, True, False, True, True, True, True, False, False, True, True, True, False, False, True, True]
    # 1.2.bit=
    # H1002.00    False
    # H1002.01     True
    # H1002.02    False
    # H1002.03     True
    # H1002.04     True
    # H1002.05     True
    # H1002.06     True
    # H1002.07    False
    # H1002.08    False
    # H1002.09     True
    # H1002.10     True
    # H1002.11     True
    # H1002.12    False
    # H1002.13    False
    # H1002.14     True
    # H1002.15     True
    # dtype: bool


def test_write_bit(s):
    print('2.1.writed data=', s.writeData('H1001.15', [1], '?'))

    data1 = [False, 1, False, 0, 1, True, False, 0x01, True, 0x00, True, 1, 0, 1, False, 1]
    data2 = [0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1]
    print('2.2.writed data=', s.writeData('H1200.00', data1, s.data_type.BOOL))
    print('2.3.writed data=', s.writeData('H1001.00', data2, '?'))
    # 2.1.writed data= None
    # 2.2.writed data= None
    # 2.3.writed data= None


def test_read_D(s):
    print('3.1.read data=', s.readData('D0', 3, s.data_type.REAL32))  # 有效数据位2位
    print('3.2.read data=', s.readData('D6', 3, s.data_type.REAL64))  # 17位有效数据，元祖输出
    print('3.3.read data=', s.readData('D18', 4, s.data_type.INT16))
    print('3.4.read data=', s.readData('D22', 3, s.data_type.INT32))
    print('3.5.read data=', s.readData('D28', 3, s.data_type.INT16))

    # 3.1.read data= [11111.22265625, 22200.0, 33333.4453125]
    # 3.2.read data= [1.23e+17, 12345.67891, 45678910.12]
    # 3.3.read data= [11111, 22222, 30000, 2000]
    # 3.4.read data= [1234567, 234567, 89456]
    # 3.5.read data= [12345, 23456, -12345]


def test_write_D(s):
    data = [0xfff0, 0x2222, 0x3333]
    print('4.1.writed data=', s.writeData('D100', data, s.data_type.UINT16))
    data = [6666.666, 7777.777, 8888.888]
    se = pd.Series(data, index=['D103', 'D105', 'D107'])
    print('4.2.writed data=', s.writeData('D103', data, s.data_type.REAL32))
    print('4.2.writed data=', s.writeData('D103', se, s.data_type.REAL32))
    data = [9112222333.44445555, 888877776666.55554444, -123456789.123456789]
    print('4.3.writed data=', s.writeData('D109', data, s.data_type.REAL64))
    data = [933, -444, -555]
    print('4.4.writed data=', s.writeData('D121', data, s.data_type.INT16))
    data = [3333444455556666, 1111222233334444, 5555]
    print('4.5.writed data=', s.writeData('D124', data, s.data_type.UINT64))

    # 4.1.writed data= None
    # 4.2.writed data= None
    # 4.2.writed data= None
    # 4.3.writed data= None
    # 4.4.writed data= None
    # 4.5.writed data= None


def test_read_H(s):
    print('5.11.1read data=', s.readData('H1000', 3, s.data_type.REAL32))  # 有效数据位2位
    print('5.12.read data=', s.readData('H1006', 3, s.data_type.REAL64))  # 17位有效数据，元祖输出
    print('5.13.read data=', s.readData('H1018', 4, s.data_type.UINT16))
    print('5.14.read data=', s.readData('H1022', 3, s.data_type.INT32))
    print('5.15.read data=', s.readData('H1028', 3, s.data_type.INT16))

    # 5.11.1read data= [8.708462946542583e-26, 2.2701035122062037e-43, 0.0]
    # 5.12.read data= [425984.0, 0.0, 666666.6665039062]
    # 5.13.read data= [10000, 15000, 20000, 4]
    # 5.14.read data= [1048576, 2345679, 3456789]
    # 5.15.read data= [12345, 23456, -30000]


def test_Write_H(s):
    data = [6666.66, 7777.77, 8888.88]
    print('6.1.writed data=', s.writeData('H1100', data, s.data_type.REAL32))
    data = [111122223333.4444, 888877776666.55554444, -123456789.123456789]
    print('6.2.writed data=', s.writeData('H1106', data, s.data_type.REAL64))
    data = [0xfff0, 0x2222, 0x3333, 0xffff]
    print('6.3.writed data=', s.writeData('H1118', data, s.data_type.UINT16))
    data = [333, -444, -555]
    print('6.4.writed data=', s.writeData('H1122', data, s.data_type.INT32))
    data = [3333, 4444, 5555]
    print('6.5.writed data=', s.writeData('H1128', data, s.data_type.INT16))

    # 6.1.writed data= None
    # 6.2.writed data= None
    # 6.3.writed data= None
    # 6.4.writed data= None
    # 6.5.writed data= None


def test_read_S(s):
    pass
    # print('3.6.read data=',s.readData('D50',2,s.data_type.STR))#待完善


if __name__ == '__main__':

    from PyQt5 import QtCore, Qt
    from queue import PriorityQueue, Queue

    global s_global_test
    q_test = Queue(1)


    class TestThread1(QtCore.QThread):
        def __init__(self):
            super(TestThread1, self).__init__()
            self.s_global_test = FinsSocketClass(ip='192.168.250.89', ip_plc='192.168.250.1')
            self.s_global_test.con()

        def run(self):
            global s_global_test
            while 1:
                print('Thread1')
                if not self.s_global_test.s_ok:
                    self.s_global_test = FinsSocketClass()
                    self.s_global_test.con()
                    s_global_test = self.s_global_test
                    if q_test.empty():
                        q_test.put(self.s_global_test)
                    while not self.s_global_test.s_ok: pass
                else:
                    s_global_test = self.s_global_test
                    if q_test.empty():
                        q_test.put(self.s_global_test)
                    while self.s_global_test.s_ok: pass
                self.sleep(1)


    # ==========================================================
    class TestThread2(QtCore.QThread):
        def __init__(self):
            super(TestThread2, self).__init__()
            self.s_global_test = None

        def run(self):
            global s_global_test
            while 1:
                print('Thread2')
                """             #全局变量
                if s_global_test:
                    if s_global_test.s_ok:
                         test_read_bit(s_global_test)
                """
                if not q_test.empty():  # 队列
                    ss = q_test.get()
                if ss:
                    if ss.s_ok:
                        test_read_bit(ss)
                        test_write_bit(ss)
                self.sleep(1)


    # ==========================================================
    import sys

    # 基础类测试
    test_fins_socket()


    # 线程中测试
    def test2():
        app = Qt.QApplication(sys.argv)
        t1 = TestThread1()
        t2 = TestThread2()
        t1.start()
        t2.start()

        sys.exit(app.exec())


    test2()
