#this function returns the mass matrix of the car
#inputs are the Car struct and which model
#outputs are the mass matrix
import numpy as np, get_Jy, get_Jx
def get_MM(model, Car):
    if (not isinstance(Car,dict)):
        print("uhm")
        return ValueError("You did not supply the right Car struct")
    g = 32.174
    if (model == "quarter_car_1_DOF"):
        w = Car['pilot']['weight'] + Car['power_plant']['weight'] + Car['chassis']['weight']
        M = w/(4*g)
    elif (model == "quarter_car_2_DOF"):
        w1 = Car['pilot']['weight'] + Car['power_plant']['weight'] + Car['chassis']['weight']
        m = w1/(4*g)
        w2 = Car['wheel_rear']['weight'] + Car['wheel_front']['weight']
        mw = w2/(2*g)
        M = np.array([[m, 0],[0, mw]])
    elif (model == "half_car_2_DOF"):
        J = get_Jy.get_Jy(Car)/2
        w1 = Car['pilot']['weight'] + Car['power_plant']['weight'] + Car['chassis']['weight']
        m1 = w1/(2*g)
        M = np.array([[m1,0],[0,J]])

    elif (model == "half_car_4_DOF"):
        J = get_Jy.get_Jy(Car)/2
        w1 = Car['pilot']['weight'] + Car['power_plant']['weight'] + Car['chassis']['weight']
        m1 = w1/(2*g)
        wf = Car['wheel_front']['weight']/g
        wr = Car['wheel_rear']['weight']/g
        M = np.array([
            [m1,0,0,0],
            [0,J,0,0],
            [0,0,wf,0],
            [0,0,0,wr]
        ]) 
    elif (model == "full_car_3_DOF"):
        Jy = get_Jy.get_Jy(Car)
        Jx = get_Jx.get_Jx(Car)
        w1 = Car['pilot']['weight'] + Car['power_plant']['weight'] + Car['chassis']['weight']
        m1 = w1/g
        M = np.array([
            [m1,0,0],
            [0,Jy,0],
            [0,0,Jx]
        ])
    elif (model == "full_car_7_DOF"):
        Jy = get_Jy.get_Jy(Car)
        Jx = get_Jx.get_Jx(Car)
        w1 = Car['pilot']['weight'] + Car['power_plant']['weight'] + Car['chassis']['weight']
        m1 = w1/g
        wf = Car['wheel_front']['weight']/g
        wr = Car['wheel_rear']['weight']/g
        M = np.array([
            [m1,0,0,0,0,0,0],
            [0,Jy,0,0,0,0,0],
            [0,0,Jx,0,0,0,0],
            [0,0,0,wf,0,0,0],
            [0,0,0,0,wf,0,0],
            [0,0,0,0,0,wr,0],
            [0,0,0,0,0,0,wr]
        ])
    return M
    