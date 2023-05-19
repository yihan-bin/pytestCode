import numpy as np

import random
n=30
class Two_Dim_Matrix:
    def __init__(self,n):
        self.n=n

    A11=np.zeros(30)
    A12=np.zeros(30)
    A21=np.zeros(30)
    A22=np.zeros(30)#Two_Dim_Matrix
class Status_struct:
    def __init__(self,n):
        self.n=n
    Position=np.zeros(30)
    Velocity=np.zeros(30)#Status_struct

W1,W2=[],[]#Status_Reeor_Struct
V1,V2=[],[]#Measurement_Error_struct
E1,E2,E3,E4=[],[],[],[]

X=Status_struct(n)
Z=Status_struct(n)
X_hat=Status_struct(n)
X_Hat_Prediction=Status_struct(n)

Q,R,A,H=Two_Dim_Matrix(n),Two_Dim_Matrix(n),Two_Dim_Matrix(n),Two_Dim_Matrix(n)
P_k=Two_Dim_Matrix(n)
P_k_Prediction=Two_Dim_Matrix(n)
K_k=Two_Dim_Matrix(n)


for i in range(29):
     E1.append(np.random.normal(0, 1))
     E2.append(np.random.normal(0, 1))
     E3.append(np.random.normal(0, 1))
     E4.append(np.random.normal(0, 1))


def Status_Parameter_Init():
    for i in range(29):
        W1.append(E1[i])
        W2.append(E2[i])
    X.Position[0]=0.0
    X.Velocity[0]=1.0
    print('X vel \n ')
    for i in range(28):
        X.Position[i+1]=A.A11*X.Position[i]+A.A12*X.Velocity[i]+W1[i]
        X.Velocity[i+1]=A.A22*X.Velocity[i]+W2[i]
def Measurement_Parameter_Init():
    for i in range(29):
        V1.append(E3[i])
        V2.append(E4[i])
    print('Z vel \n')
    for i in range(29):
        Z.Position[i+1]=H.A11*X.Position[i+1]+H.A12+X.Velocity[i]+V1[i+1]
        Z.Velocity[i+1]=H.A22*X.Velocity[i+1]+V2[i+1]
        print(Z.Velocity[i+1])











if __name__ == "__main__":
    pass