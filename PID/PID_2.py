
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
    abs_err=0

    current_Err = (Sv-value)*100000

    proportion=pid_P*current_Err/pid_P

    if (current_Err>=-pid_b) and (current_Err<=pid_b):
        if current_Err>-5 and current_Err<=pid_b:
            Integral=Integral+(pid_T*pid_T*current_Err)/(pid_P+pid_I)#变速积分
        elif current_Err>-10 and current_Err<=-5:
            Integral=Integral+(2*pid_T*pid_T*current_Err)/(pid_P+pid_I)#变速积分
        elif current_Err>-15 and current_Err<=-10:
            Integral=Integral+(4*pid_T*pid_T*current_Err)/(pid_P+pid_I)#变速积分
        else:
            Integral=Integral+(8*pid_T*pid_T*current_Err)/(pid_P+pid_I)#变速积分
    elif current_Err<=-pid_ab or current_Err>=-pid_ab
        Integral=0;
    else:
        abs_err=current_Err
        if (abs_err<0):
            abs_err=-current_Err
        Integral=Integral+(pid_P*pid_T*current_Err)/(pid_ab-abs_err/100000)/(pid_p*pid_I*(pid_ab-pid_b))#速变积分

    if  Integral>(pid_IM*pid_T*10000):
        Integral=pid_IM*pid_T*10000
    elif Integral<0
        Integral=0

    Derivative=(pid_D*Derivative)/(10*pid_T+pid_D)+((current_Err-Last_Err)*10*pid_D)/(pid_P*(10*pid_T+pid_D))
    result=(proportion+Integral+Derivative)/1000
    if result>pid_T*1000:
        result=pid_T*1000
    elif result<0:
        result=0
    Last_Err=current_Err;
    return result





