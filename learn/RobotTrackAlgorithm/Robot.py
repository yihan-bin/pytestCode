from math import pi
import numpy as np
from roboticstoolbox import DHRobot, RevoluteDH, PrismaticDH, RevoluteMDH, PrismaticMDH
class MYROBOT(DHRobot):
    """
    Create model of MYROBOT manipulator
    KR5()是一个用标准DH约定对Kuka KR5机器人建模并描述其运动学特征的类。
       .
       定义的关节构型为:
       qk1，公称工作位置1
       qk2，公称工作位置2
       qk3，公称工作位置3.

    :notes:
       .使用国际计量单位米
       .包括一个11.5厘米的工具在z方向
       .

    :references:
       .
       .
       .

    """

    def __init__(self):
        deg = pi / 180

        L0 = RevoluteDH(
            d=0,  # link length (Dennavit-Hartenberg notation)
            a=0,  # link offset (Dennavit-Hartenberg notation)
            alpha=pi / 2,  # link twist (Dennavit-Hartenberg notation)
            I=[0, 0.35, 0, 0, 0, 0],  # inertia tensor of link with respect to
            # center of mass I = [L_xx, L_yy, L_zz,
            # L_xy, L_yz, L_xz]
            r=[0, 0, 0],  # distance of ith origin to center of mass [x,y,z]
            # in link reference frame
            m=0,  # mass of link
            Jm=200e-6,  # actuator inertia
            G=-62.6111,  # gear ratio
            B=1.48e-3,  # actuator viscous friction coefficient (measured
            # at the motor)
            Tc=[0.395, -0.435],  # actuator Coulomb friction coefficient for
            # direction [-,+] (measured at the motor)
            qlim=[-160 * deg, 160 * deg])  # minimum and maximum joint angle

        L1 = RevoluteDH(
            d=0, a=0.4318, alpha=0,
            qlim=[-45 * deg, 225 * deg])
    super().__init__(
        [L0, L1, L2, L3, L4, L5],
        name="MYROBOT",
        manufacturer="COMPANY THAT BUILDS MYROBOTs")
    # 零角度，L形姿势
    self._MYCONFIG = np.array([1, 2, 3, 4, 5, 6])  # 创建实例属性
    self.addconfiguration("qz", np.array([0, 0, 0, 0, 0, 0]))  # 零角度，L形姿势
    self.addconfiguration("qr", np.array([0.610865, 1.047198, 0.785398, 1.134464, 0.628319, 0]))

    @property
    def MYCONFIG(self):
        return self._MYCONFIG
if __name__ == '__main__':

    robot = MYROBOT()
    print(robot)
    print(robot._MYCONFIG)
