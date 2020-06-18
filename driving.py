#This file "drives" the car by calling all the required files
#outputs plots of the dynamic/vibration models 

import Beeman, car_2014, chassis_2014, driver_sally, ff_2014_5, ff_2014_7, get_DM, get_FF, get_Jx, get_Jy, get_LR, get_MM, get_SD, get_SM, get_cg, motor_2014, speed_bump, suspension_front_2014, suspension_rear_2014, trajectory, wheel_front_2014, wheel_rear_2014
import numpy as np, math

ff = ff_2014_7.ff_data
ffmatrix, ffobject = get_FF.get_FF(ff['t_prev'],ff)
X0 = get_SD.get_SD(ff['model'],ff['car'])
DOF = X0.shape[0]
V0 = np.zeros((DOF,1))
A0 = np.zeros((DOF,3))
M = get_MM.get_MM(ff['model'],ff['car'])
C = get_DM.get_DM(ff['model'],ff['car'])
K = get_SM.get_SM(ff['model'],ff['car'])
# print(X0)
# print(type(X0))
# print(type(V0))
# print(type(A0))
# print(type(M))
# print(type(C))
# print(type(K))
# print(type(ffmatrix))
# print(type(ffobject))
# print(type(ff_2014_7))

T7, X7, V7, A7 = Beeman.Beeman(X0,V0,A0,M,C,K, get_FF.get_FF, ffobject)
