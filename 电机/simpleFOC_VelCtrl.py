import time

import numpy as np
import matplotlib.pyplot as plt


def _constrain(amt, low, hight):
    if amt > hight:
        return hight
    elif amt < low:
        return low
    else:
        return amt


voltage_limit = 10
voltage_power_supply = 12.6
shaft_angle = 0
open_loop_timestamp = 0
zero_electric_angle = 0
Ubeta = 0
Ua = 0
Ub = 0
Uc = 0
dc_a = 0
dc_b = 0
dc_c = 0
angle=[]
a=[]
b=[]
c=[]

plt.ion()
plt.figure()
# fig, ax = plt.subplots()
def _electricalAngle(shaft_anglr, pole_pairs):
    return shaft_anglr * pole_pairs


def _normalizeAngle(angle):
    a=angle % (2*np.pi)
    result=a if a>=0 else (a+2*np.pi)
    return result



def setPwm( Ua,  Ub,  Uc):


    Ua = _constrain(Ua, 0.0, voltage_power_supply)
    Ub = _constrain(Ub, 0.0, voltage_power_supply)
    Uc = _constrain(Uc, 0.0, voltage_power_supply)

    dc_a = _constrain(Ua / voltage_power_supply, 0.0 , 1.0 )
    dc_b = _constrain(Ub / voltage_power_supply, 0.0 , 1.0 )
    dc_c = _constrain(Uc / voltage_power_supply, 0.0 , 1.0 )


#    print(dc_a, dc_b, dc_c)
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




def setPhaseVoltage(Uq, Ud, angle_el):
    angle.append(angle_el)
    angle_el = _normalizeAngle(angle_el + zero_electric_angle)

    Ualpha = -Uq * np.sin(angle_el)+Ud*np.cos(angle_el)
    Ubeta = Uq * np.cos(angle_el)+Ud*np.sin(angle_el)

    Ua = Ualpha + voltage_power_supply / 2
    Ub = (np.sqrt(3) * Ubeta - Ualpha) / 2 + voltage_power_supply / 2
    Uc = (-Ualpha - np.sqrt(3) * Ubeta) / 2 + voltage_power_supply / 2
    print(Ua,Ub,Uc)
    setPwm(Ua, Ub, Uc)


def velocityOpenloop(target_velocity):
    global open_loop_timestamp,shaft_angle
    now_us = time.time()*1000
 #   print(now_us)
    Ts = (now_us - open_loop_timestamp) * 1e-6

    if (Ts <= 0 or Ts > 0.5):
        Ts = 1e-2
    shaft_angle = _normalizeAngle(shaft_angle + target_velocity * Ts)

    Uq = voltage_limit/2
    Ud = voltage_limit / 4
    # print(shaft_angle)
    setPhaseVoltage(Uq, 0, _electricalAngle(shaft_angle, 7))

    open_loop_timestamp = now_us

    return Uq

if __name__ == '__main__':
    while True:
        velocityOpenloop(50)




