import numpy as np
def get_DM(model,Car):
    if (not isinstance(Car,dict)):
        return ValueError("You did not supply the right Car struct")
    g = 32.174
    lrf = get_LR("front",Car)
    lrr = get_LR("rear",Car)
    cf = lrf * Car[suspension_front][c] * 12
    cr = lrr * Car[suspension_rear][c] * 12
    cwf = Car[wheel_front][c] * 12
    cwr = Car[wheel_rear][c] * 12
    if(model == "quarter_car_1_DOF"):
        C = (cf+cr)/2
    elif(model == "quarter_car_2_DOF"):
        c = (cf+cr)/2
        cw = (cwf + cwr)/2
        C = np.array([
            [c,-c],
            [-c,c+cw]
        ])
    elif(model == "half_car_2_DOF"):
        lf = get_cg(Car)
        lr = Car[chassis][wheelbase]/12 - lf
        C = np.array([
            [cr+cf,-cf*lf+cr*lr],
            [-cf*lf+cr*lr, cf*lf**2+cr*lr**2]
        ])
    elif(model == "half_car_4_DOF"):
        lf = get_cg(Car)
        lr = Car[chassis][wheelbase]/12 - lf
        C = np.array([
            [cf+cr, -cf*lf+cr*lr, -cf,-cr],
            [-cf*lf+cr*lr,cf*lf**2+cr*lr**2,cf*lf,-cr*lr],
            [-cf,cf*lf,cf+cwf,0],
            [-cr,-cr*lr,0,cr+cwr]
        ])
    elif(model == "full_car_3_DOF"):
        lf = get_cg(Car)
        lr = Car[chassis][wheelbase]/12 - lf
        rf = Car[chassis][radius_f]/12
        rr = Car[chassis][radius_r]/12
        C = np.array([
            [cf+cf+cr+cr,-(cf+cf)*lf+(cr+cr)*lr,-(cf-cf)*rf+(cr-cr)*rr],
            [-(cf+cf)*lf+(cr+cr)*lr,(cf+cf)*lf**2+(cr+cr)*lr**2,(cf-cf)*lf*rf+(cr-cr)*lr*rr],
            [-(cf-cf)*rf+(cr-cr)*rr,(cf-cf)*lf*rf+(cr-cr)*lr*rr,(cf+cf)*rf**2+(cr+cr)*rr**2]
        ])
    elif(model == "full_car_7_DOF"):
        lf=get_cg(FSAE_Race_Car)
        lr=FSAE_Race_Car.chassis.wheelbase/12-lf
        rf=FSAE_Race_Car.chassis.radius_f/12
        rr=FSAE_Race_Car.chassis.radius_r/12
        C= np.array([
            [cf+cf+cr+cr,-(cf+cf)*lf+(cr+cr)*lr,-(cf-cf)*rf+(cr-cr)*rr,-cf,-cf,-cr,-cr],
            [-(cf+cf)*lf+(cr+cr)*lr,(cf+cf)*lf**2+(cr+cr)*lr**2,(cf-cf)*lf*rf+(cr-cr)*lr*rr,cf*lf,cf*lf,-cr*lr,-cr*lr],
            [-(cf-cf)*rf+(cr-cr)*rr,(cf-cf)*lf*rf+(cr-cr)*lr*rr,(cf+cf)*rf**2+(cr+cr)*rr**2, cf*rf,-cf*rf,-cr*rr,cr*rr],
            [-cf,cf*lf,cf*rf,cf+cwf,0,0,0],
            [-cf,cf*lf,-cf*rf,0,cf+cwf,0,0],
            [-cr,-cr*lr,-cr*rr,0,0,cr+cwr,0],
            [-cr,-cr*lr,cr*rr,0,0,0,cr+cwr]
        ])
    else:
        return ValueError("You did not supply the right Car struct")
    return C