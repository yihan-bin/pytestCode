import time

import numpy as np
import matplotlib.pyplot as plt



Sensor_DIR=-1
Motor_PP=7



def loop():

    Kp=0.133
    Sensor_Angle=DFOC_M0_Angle()
    etTorque(Kp*(serial_motor_target()-Sensor_DIR*Sensor_Angle)*180/PI,_electricalAngle())



pwmA = 32

pwmB = 33

pwmC = 25

def _constrain(amt, low, hight):
    if amt > hight:
        return hight
    elif amt < low:
        return low
    else:
        return amt


voltage_limit = 12.6

voltage_power_supply = 12.6

shaft_angle = 0
open_loop_timestamp = 0

zero_electric_angle = 0
Ualpha=0
Ubeta = 0
Ua = 0
Ub = 0
Uc = 0
dc_a = 0
dc_b = 0
dc_c = 0
_3PI_2=4.71238898038
angle=[]
a=[]
b=[]
c=[]

plt.ion()
plt.figure()

PP = 7
DIR = -1
def getAngle_Without_track():
    return _normalizeAngle(getAngle())
    # return 2 - aa

def _normalizeAngle(angle):
    a=angle % (2*np.pi)
    result=a if a>=0 else (a+2*np.pi)
    return result

def _electricalAngle():

    return _normalizeAngle((DIR * PP) * getAngle_Without_track() - zero_electric_angle)



def setPwm( Ua,  Ub,  Uc):
    global a,b,c

    Ua = _constrain(Ua, 0.0, voltage_power_supply)
    Ub = _constrain(Ub, 0.0, voltage_power_supply)
    Uc = _constrain(Uc, 0.0, voltage_power_supply)

    dc_a = _constrain(Ua / voltage_power_supply, 0.0 , 1.0 )
    dc_b = _constrain(Ub / voltage_power_supply, 0.0 , 1.0 )
    dc_c = _constrain(Uc / voltage_power_supply, 0.0 , 1.0 )


    print(dc_a, dc_b, dc_c)
    a.append(dc_a)
    b.append(dc_b)
    c.append(dc_c)

    # plt.clf()
    plt.plot(angle, a, 'r')
    plt.plot(angle, b, 'b')
    plt.plot(angle, c, 'g')
    # ax.plot(angle,a)
    # ax.plot(angle, b)
    # ax.plot(angle, c)
    # plt.draw()
    # time.sleep(0.1)
    # ax.legend()
    plt.pause(0.1)
    plt.ioff()

bb=0

def setPhaseVoltage(Uq, Ud, angle_el):
    global bb
    bb=bb+0.1
    angle.append(bb)
    angle_el = _normalizeAngle(angle_el + zero_electric_angle)

    Ualpha = -Uq * np.sin(angle_el)+Ud*np.cos(angle_el)
    Ubeta = Uq * np.cos(angle_el)+Ud*np.sin(angle_el)

    Ua = Ualpha + voltage_power_supply / 2
    Ub = (np.sqrt(3) * Ubeta - Ualpha) / 2 + voltage_power_supply / 2
    Uc = (-Ualpha - np.sqrt(3) * Ubeta) / 2 + voltage_power_supply / 2
    #print(Ua,Ub,Uc)
    setPwm(Ua, Ub, Uc)
def setup():


    #BeginSensor()
    setPhaseVoltage(3, 0, _3PI_2)
    delay(3000)
    zero_electric_angle = _electricalAngle()
    setPhaseVoltage(0, 0, _3PI_2)
motor_target=0
commaPosition=0
aa=0
def getAngle():
    global aa

    aa=aa+0.03
    if aa>=1:
        aa=1\
    print(aa)
    return 1-aa

if __name__ == '__main__':
    while True:
        Sensor_Angle = getAngle()
        Kp = 0.133
        setPhaseVoltage(_constrain(Kp * (motor_target - DIR * Sensor_Angle) * 180 / np.pi, -6, 6), 0, _electricalAngle())


