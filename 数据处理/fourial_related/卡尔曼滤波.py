import random
import numpy as np
n=100

Z_k=np.zeros(n)
E_mea=0
X_k=np.zeros(n)
k_k=np.zeros(n)
E_est=np.zeros(n)


#
# def Kalman_Parameter_Init():
X_k[0]=40
E_est[0]=5
E_mea=3


def  Generating_Random_Masurement(n):
    for i in range(n-1):
        n=np.random.normal(0,6)
        Z_k[i]=47.0+n
        print(Z_k[i])
def Kalman_Gain_Cal(E_est,E_mea):
    result=E_est/(E_est+E_mea)
    return  result
def Kalman_X_K_cal(n):
    for i in range(n-1):
        Kalman_Gain=Kalman_Gain_Cal(E_est[i],E_mea)
        X_k[i+1]=X_k[i]+Kalman_Gain*(Z_k[i+1]-X_k[i])
        E_est[i+1]=(1-Kalman_Gain)*E_est[i]
        print(Kalman_Gain,X_k[i+1],E_est[i+1])



if __name__ == "__main__":
    print('The actual length of the object is 50\n\t')
    Generating_Random_Masurement(n)
   #Kalman_Parameter_Init()
    Kalman_X_K_cal(n)

