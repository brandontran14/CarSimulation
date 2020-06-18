#This function constructs a forcing function that governs the equation of motion for the car. 
#inputs are time and the ff object
#returns FF matrix and the updated ff object
import ff_2014_5, trajectory, speed_bump, numpy as np, get_DM, get_SM, get_LR, get_cg

def get_FF(time,ff):
    if(not isinstance(ff,dict)):
        return ValueError("You did not supply the right Car struct")
    t,X,V = ff['trajectory'](ff["t_prev"],ff["X_prev"], (ff["t_out"]-ff["t_in"])/ff["N"], ff["t_in"],ff['t_out'],ff['V_in'], ff['V_out'], ff['car'])
    R_f_d, R_r_d, dRdt_f_d, dRdt_r_d = ff["roadway_d"](ff["car"]["chassis"]['wheelbase']/12, ff["X_enter_d"], X, V)
    R_f_p, R_r_p, dRdt_f_p, dRdt_r_p = ff['roadway_p'](ff["car"]["chassis"]['wheelbase']/12, ff["X_enter_p"], X, V)
    model = ff["model"]
    if(model == "quarter_car_1_DOF"):
        c = get_DM.get_DM(ff["model"],ff["car"])
        k = get_SM.get_SM(ff["model"],ff['car'])
        FF = ((ff['car']['pilot']['weight'] + ff['car']['power_plant']['weight'] + ff['car']['chassis']['weight'])/4) - c * dRdt_f_d - k * R_f_d
    elif(model == "quarter_car_2_DOF"):
        frontwheel = ff['car']['wheel_front']['weight']
        rearwheel = ff['car']['wheel_rear']['weight']
        wheelw = (frontwheel+rearwheel)/2
        FF = np.array([
            [(ff['car']['pilot']['weight'] + ff['car']['power_plant']['weight'] + ff['car']['chassis']['weight'])/4],
            [wheelw-(c[1][1]-c[0][0]) * dRdt_f_d - (k[1][1]-k[0][0]) * R_f_d]
        ])
    elif(model == "half_car_2_DOF"):
        w = (ff['car']['pilot']['weight'] + ff['car']['power_plant']['weight'] + ff['car']['chassis']['weight'])/2
        lrf = get_LR.get_LR('front',ff['car'])
        lrr = get_LR.get_LR('rear',ff['car'])
        cf = ff['car']['suspension_front']['c']* lrf * 12
        cr = ff['car']['suspension_rear']['c'] * lrr * 12
        kf = ff['car']['suspension_front']['k'] * lrf * 12
        kr = ff['car']['suspension_rear']['k'] * lrr * 12
        lf = get_cg.get_cg(ff['car'])
        lr = ff['car']['chassis']['wheelbase']/12 - lf
        FF = np.array([
            [w - cf*dRdt_f_d - cr*dRdt_r_d - kf*R_f_d - kr*R_r_d],
            [cf*lf*dRdt_f_d - cr*lr*dRdt_r_d + kf*lf*R_f_d - kr*lr*R_r_d]
        ])
    elif(model == "half_car_4_DOF"):
        w = (ff['car']['pilot']['weight'] + ff['car']['power_plant']['weight'] + ff['car']['chassis']['weight'])/2
        lrf = get_LR.get_LR('front',ff['car'])
        lrr = get_LR.get_LR('rear',ff['car'])
        kf = ff['car']['wheel_front']['k']*12
        kw = ff['car']['wheel_rear']['k']*12
        cf=ff['car']['wheel_front']['c']*12
        cr=ff['car']['wheel_rear']['c']*12
        frontwheel=ff['car']['wheel_front']['weight']
        rearwheel=ff['car']['wheel_rear']['weight']
        FF = np.array([
            [w],
            [0],
            [frontwheel-cf*dRdt_f_d-kf*R_f_d],
            [rearwheel-cr*dRdt_r_d-kr*R_r_d]
        ])
    elif(model == "full_car_3_DOF"):
        w = (ff['car']['pilot']['weight'] + ff['car']['power_plant']['weight'] + ff['car']['chassis']['weight'])
        lrf = get_LR.get_LR('front',ff['car'])
        lrr = get_LR.get_LR('rear',ff['car'])
        kf = ff['car']['suspension_front']['k']['lrf']*12
        kr = ff['car']['suspension_rear']['k']['lrr']*12
        cf=ff['car']['suspension_front']['c']*12
        cr=ff['car']['suspension_rear']['c']*12
        lf = get_cg.get_cg(ff['car'])
        lr = ff['car']['chassis']['wheelbase']/12 - lf
        rf = ff['car']['chassis']['radius_f']/12
        rr = ff['car']['chassis']['radius_r']/12
        FF = np.array([
            [w-cf*dRdt_f_d-cf*dRdt_f_p-cr*dRdt_r_p-cr*dRdt_r_d-kf*R_f_d-kf*R_f_p-kr*R_r_p-kr*R_r_d],
            [(cf*dRdt_f_d+cf*dRdt_f_p+kf*R_f_d+kf*R_f_p)*lf-(cr*dRdt_r_p+cr*dRdt_r_d+kr*R_r_p+kr*R_r_d)*lr],
            [(cf*dRdt_f_d-cf*dRdt_f_p+kf*R_f_d-kf*R_f_p)*rf-(cr*dRdt_r_p-cr*dRdt_r_d+kr*R_r_p-kr*R_r_d)*rr]
        ])
    elif(model == "full_car_7_DOF"):
        w = (ff['car']['pilot']['weight'] + ff['car']['power_plant']['weight'] + ff['car']['chassis']['weight'])
        wf = ff['car']['wheel_front']['weight']
        wr = ff['car']['wheel_rear']['weight']
        kf = ff['car']['wheel_front']['k']*12
        kr = ff['car']['wheel_rear']['k']*12
        cf = ff['car']['wheel_front']['c']*12
        cr = ff['car']['wheel_rear']['c']*12
        FF = np.array([
            [w],
            [0],
            [0],
            [wf - cf * dRdt_f_d-kf*R_f_d],
            [wf-cf*dRdt_f_p-kf*R_f_p],
            [wr-cr*dRdt_r_p-kr*R_r_p],
            [wr-cr*dRdt_r_d-kr*R_r_d]
        ])
    else:
        return ValueError("Model inputted in FF doeasnt work")
    ff['t_prev'] = t
    ff['X_prev'] = X
    return FF, ff

