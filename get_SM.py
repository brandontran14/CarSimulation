import numpy as np
import get_LR, get_cg
def get_SM(model, Car):
    if (not isinstance(Car,dict)):
        return ValueError("You did not supply the right Car struct")
    g = 32.174
    lrf = get_LR.get_LR("front",Car)
    lrr = get_LR.get_LR("rear",Car)
    kf = lrf * Car['suspension_front']['k'] * 12
    kr = lrr * Car['suspension_rear']['k'] * 12
    if (model == "quarter_car_1_DOF"):
        K = (kf+kr)/2
    elif(model == "quarter_car_2_DOF"):
        kwf = Car['wheel_front']['k'] * 12
        kwr = Car['wheel_rear']['k'] * 12
        K = np.array([
            [(kf+kr)/2, -(kf+kr)/2],
            [-(kf+kr)/2, (kf+kr)/2 + (kwf+kwr)/2]
        ])
    elif(model == "half_car_2_DOF"):
        lf = get_cg.get_cg(Car)
        lr = Car['chassis']['wheelbase']/12 - lf
        K = np.array([
            [kf+kr, -kf*lf+kr*lr],
            [-kf*lf+kr*lr, kf*lf**2+kr*lr**2]
        ])
    elif(model == "half_car_4_DOF"):
        kwf = Car['wheel_front']['k'] * 12
        kwr = Car['wheel_rear']['k'] * 12
        lf = get_cg.get_cg(Car)
        lr = Car['chassis']['wheelbase']/12 - lf
        K = np.array([
            [kf+kr,-kf*lf+kr*lr,-kf,-kr],
            [-kf*lf+kr*lr,kf*lf**2+kr*lr**2,kf*lf,-kr*lr],
            [-kf,kr*lf,kf+kwf,0],
            [-kr,-kr*lr,0,kr+kwr]
        ])
    elif(model == "full_car_3_DOF"):
        lf = get_cg.get_cg(Car)
        lr = Car['chassis']['wheelbase']/12 - lf
        rf = Car['chassis']['radius_f']/12
        rr = Car['chassis']['radius_r']/12
        K = np.array([
            [kf+kf+kr+kr,-(kf+kf)*lf+(kr+kr)*lr, -(kf-kf)*rf+(kr-kr)*rr],
            [-(kf+kf)*lf+(kr+kr)*lr, (kf+kf)*lf**2+(kr+kr)*lr**2, (kf-kf)*lf*rf+(kr-kr)*lr*rr],
            [-(kf-kf)*rf+(kr-kr)*rr, (kf-kf)*lf*rf+(kr-kr)*lr*rr, (kf+kf)*rf**2+(kr+kr)*rr**2]
        ])
    elif(model == "full_car_7_DOF"):
        kwf = Car['wheel_front']['k'] * 12
        kwr = Car['wheel_rear']['k'] * 12
        lf = get_cg.get_cg(Car)
        lr = Car['chassis']['wheelbase']/12 - lf 
        rf = Car['chassis']['radius_f']/12
        rr = Car['chassis']['radius_r']/12
        K = np.array([
            [kf+kf+kr+kr,-(kf+kf)*lf+(kr+kr)*lr,-(kf-kf)*rf+(kr-kr)*rr,-kf,-kf,-kr,-kr],
            [-(kf+kf)*lf+(kr+kr)*lr,(kf+kf)*lf**2+(kr+kr)*lr**2,(kf-kf)*lf*rf+(kr-kr)*lr*rr,kf*lf,kf*lf,-kr*lr,-kr*lr],
            [-(kf-kf)*rf+(kr-kr)*rr,(kf-kf)*lf*rf+(kr-kr)*lr*rr, (kf+kf)*rf**2+(kr+kr)*rr**2, kf*rf, -kf*rf, -kr*rr, kr*rr],
            [-kf, kf*lf, kf*rf, kf+kwf,0,0,0],
            [-kf, kf*lf, -kf*rf, 0, kf+kwf, 0,0],
            [-kr, -kr*lr, -kr*rr, 0,0, kr+kwr, 0],
            [-kr, -kr*lr, kr*rr, 0,0,0,kr+kwr]
        ])
    # else:
    #     return ValueError("You did not input the right struct for get_SM")
    return K