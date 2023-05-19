
import numpy as np

proportion=0
Integral=0
Derivative=0
Last_Err=0

def PID(Sv,value):
    result = 0
    para = [np.array(10)]*10
    pid_P = para[5]
    pid_I = para[6]
    pid_D = para[7]
    pid_T = para[9]
    global Last_Err

    current_Err = Sv-value

    proportion=pid_P*current_Err

    Integral=Integral+(pid_P*pid_T*current_Err)/pid_I

    if  Integral>para[8]:
        Integral=para[8]
    elif Integral<0
        Integral=0

    Derivative=((current_Err-Last_Err)*pid_P*pid_D)/pid_T
    result=proportion+Integral+Derivative
    if result>pid_T:
        result=pid_T
    elif result<0:
        result=0
    Last_Err=current_Err;
    return result





