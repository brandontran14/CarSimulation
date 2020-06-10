# function [FF,ff_data]=get_forcing_function(t,ff_data)
# %this function constructs a forcing function to govern the equation of
# %motion, the inputs are t, time, and ff_data, a structure with inputs used
# %for the forcing function the return arguments are FF and ff_data. FF is a
# %vector forcing function and ff_data is the updated structure
import ff_2014_5, trajectory, speed_bump

def get_FF(time,ff):
    if(not isinstance(ff,dict)):
        return ValueError("You did not supply the right Car struct")
    t,X,V = ff['trajectory'](ff["t_prev"],ff["X_prev"], (ff["t_out"]-ff["t_in"])/ff["N"], ff["t_in"],ff['t_out'],ff['V_in'], ff['V_out'], ff['car'])
    R_f_d, R_r_d, dRdt_f_d, dRdt_r_d = ff["roadway_d"](ff["car"]["chassis"]['wheelbase']/12, ff["X_enter_d"], X, V)
    R_f_p, R_r_p, dRdt_f_p, dRdt_r_p = ff['roadway_p'](ff["car"]["chassis"]['wheelbase']/12, ff["X_enter_p"], X, V)
    model = ff["model"]
    if(model == "quarter_car_1_DOF"):
        c = get_DM(ff["model"],ff["car"])
        k = get_SM(ff["model"],ff['car'])
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
        lrf = get_LR('front',ff['car'])
        lrr = get_LR('rear',ff['car'])
        cf = ff['car']['suspension_front']['c']* lrf * 12
        cr = ff['car']['suspension_rear']['c'] * lrr * 12
        kf = ff['car']['suspension_front']['k'] * lrf * 12
        kr = ff['car']['suspension_rear']['k'] * lrr * 12
        lf = get_cg(ff['car'])
        lr = ff['car']['chassis']['wheelbase']/12 - lf
        FF = np.array([
            [w - cf*dRdt_f_d - cr*dRdt_r_d - kf*R_f_d - kr*R_r_d],
            [cf*lf*dRdt_f_d - cr*lr*dRdt_r_d + kf*lf*R_f_d - kr*lr*R_r_d]
        ])
    elif(model == "half_car_4_DOF"):
        w = (ff['car']['pilot']['weight'] + ff['car']['power_plant']['weight'] + ff['car']['chassis']['weight'])/2
        lrf = get_LR('front',ff['car'])
        lrr = get_LR('rear',ff['car'])
        cf = ff['car']['suspension_front']['c']* lrf * 12
        cr = ff['car']['suspension_rear']['c'] * lrr * 12
        kf = ff['car']['suspension_front']['k'] * lrf * 12
        kr = ff['car']['suspension_rear']['k'] * lrr * 12
        kwf = ff['car']['wheel_front']['k'] * 12
        kwr = ff['car']['wheel_rear']['k'] * 12

        FF = np.array([
            [w],
            [0],
            [frontwheel-cf*dRdt_f_d-kf*R_f_d],
            [rearwheel-cr*dRdt_r_d-kr*R_r_d]
        ])
#     elseif strcmp(vm,'half_car_4_DOF')
#         w=(ff_data.car.pilot.weight + ff_data.car.power_plant.weight + ff_data.car.chassis.weight)/2;
#         lrf=get_leverage_ratio('front',ff_data.car);
#         lrr=get_leverage_ratio('rear',ff_data.car);
#         kf=ff_data.car.wheel_front.k*12;
#         kw=ff_data.car.wheel_rear.k*12;
#         kf=ff_data.car.suspension_front.k*lrf*12;
#         kr=ff_data.car.suspension_rear.k*lrr*12;
#         cf=ff_data.car.wheel_front.c*12;
#         cr=ff_data.car.wheel_rear.c*12;
        
#         frontwheel=ff_data.car.wheel_front.weight;
#         rearwheel=ff_data.car.wheel_rear.weight;
        
        
#         FF=[w;0;frontwheel-cf*dRdt_f_d-kf*R_f_d;rearwheel-cr*dRdt_r_d-kr*R_r_d];
#     elseif strcmp(vm,'full_car_3_DOF')
#         w=(ff_data.car.pilot.weight + ff_data.car.power_plant.weight + ff_data.car.chassis.weight);
#         lrf=get_leverage_ratio('front',ff_data.car);
#         lrr=get_leverage_ratio('rear',ff_data.car);
#         kf=ff_data.car.suspension_front.k*lrf*12;
#         kr=ff_data.car.suspension_rear.k*lrr*12;
#         c1=ff_data.car.suspension_front.c*lrf*12;
#         c3=ff_data.car.suspension_rear.c*lrr*12;
#         c2=c1;
#         c4=c3;
#         k1=kf;
#         k2=k1;
#         k3=kr;
#         k4=k3;
#         lf=get_cg(ff_data.car);
#         lr=ff_data.car.chassis.wheelbase/12-lf;
#         rf=ff_data.car.chassis.radius_f/12;
#         rr=ff_data.car.chassis.radius_r/12;
#         FF=[w-c1*dRdt_f_d-c2*dRdt_f_p-c3*dRdt_r_p-c4*dRdt_r_d-k1*R_f_d-k2*R_f_p-k3*R_r_p-k4*R_r_d;(c1*dRdt_f_d+c2*dRdt_f_p+k1*R_f_d+k2*R_f_p)*lf-(c3*dRdt_r_p+c4*dRdt_r_d+k3*R_r_p+k4*R_r_d)*lr;(c1*dRdt_f_d-c2*dRdt_f_p+k1*R_f_d-k2*R_f_p)*rf-(c3*dRdt_r_p-c4*dRdt_r_d+k3*R_r_p-k4*R_r_d)*rr];
        
#     elseif strcmp(vm,'full_car_7_DOF')
#         w=(ff_data.car.pilot.weight + ff_data.car.power_plant.weight + ff_data.car.chassis.weight);
#         wf=ff_data.car.wheel_front.weight;
#         wr=ff_data.car.wheel_rear.weight;
#         kf=ff_data.car.wheel_front.k*12;
#         kr=ff_data.car.wheel_rear.k*12;
#         cf=ff_data.car.wheel_front.c*12;
#         cr=ff_data.car.wheel_rear.c*12;
#         FF=[w;0;0;wf-cf*dRdt_f_d-kf*R_f_d;wf-cf*dRdt_f_p-kf*R_f_p; wr-cr*dRdt_r_p-kr*R_r_p;wr-cr*dRdt_r_d-kr*R_r_d];
#     else 
#         error('model inputted does not work')
#     end
#     ff_data.t_prev=t;
#     ff_data.X_prev=X;
# end
# end

