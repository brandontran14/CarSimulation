function K=get_stiffness_matrix(vibration_model,FSAE_Race_Car)
%This function takes in two inputs, vibration_model string and FSAE_Race_Car
%structure
%The vibration_model must have input of 'quarter_car_1_DOF',
%'quarter_car_2_DOF', 'half_car_2_DOF', 'half_car_4_DOF', full_car_3_DOF, or full_car_7_DOF  otherwise it will return an error
%the second input must be the car structure, if it is not then it will
%return an error. 
%the function returns the stiffness matrix for either 1 or 2 DOF models.
%returns stiffness matrix in lb/ft or ft-lb/rad
if isstruct(FSAE_Race_Car) ==1 
    if strcmp(vibration_model,'quarter_car_1_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        kf=lrf*FSAE_Race_Car.suspension_front.k*12; %convert to ft
        kr=lrr*FSAE_Race_Car.suspension_rear.k*12; %convert to ft
        k=(kf+kr)/2;
        K=[k];
    elseif strcmp(vibration_model,'quarter_car_2_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        kf=lrf*FSAE_Race_Car.suspension_front.k*12; %convert to ft
        kr=lrr*FSAE_Race_Car.suspension_rear.k*12; %convert to ft
        kwf=FSAE_Race_Car.wheel_front.k*12; %convert to ft
        kwr=FSAE_Race_Car.wheel_rear.k*12; %convert to ft
        k=(kf+kr)/2;
        kw=(kwf+kwr)/2;
        K=[k,-k;-k,k+kw];
    elseif strcmp(vibration_model,'half_car_2_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        kf=lrf*FSAE_Race_Car.suspension_front.k*12; %convert to ft
        kr=lrr*FSAE_Race_Car.suspension_rear.k*12; %convert to ft
        kwf=FSAE_Race_Car.wheel_front.k*12; %convert to ft
        kwr=FSAE_Race_Car.wheel_rear.k*12; %convert to ft
        k1=kf;
        k2=kr;
        lf=get_cg(FSAE_Race_Car);
        lr=(FSAE_Race_Car.chassis.wheelbase/12)-lf;
        K=[k1+k2,-k1*lf+k2*lr;-k1*lf+k2*lr,k1*lf^2+k2*lr^2];
        
    elseif strcmp(vibration_model,'half_car_4_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        kf=lrf*FSAE_Race_Car.suspension_front.k*12; %convert to ft
        kr=lrr*FSAE_Race_Car.suspension_rear.k*12; %convert to ft
        kwf=FSAE_Race_Car.wheel_front.k*12; %convert to ft
        kwr=FSAE_Race_Car.wheel_rear.k*12; %convert to ft
        k1=kf;
        k2=kr;
        lf=get_cg(FSAE_Race_Car);
        lr=(FSAE_Race_Car.chassis.wheelbase/12)-lf;
        K=[k1+k2,-k1*lf+k2*lr,-k1,-k2;-k1*lf+k2*lr,k1*lf^2+k2*lr^2,k1*lf,-k2*lr;-k1,k1*lf,k1+kwf,0;-k2,-k2*lr,0,k2+kwr];
        
    elseif strcmp(vibration_model,'full_car_3_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        kf=lrf*FSAE_Race_Car.suspension_front.k*12; %convert to ft
        kr=lrr*FSAE_Race_Car.suspension_rear.k*12; %convert to ft
        k1=kf;
        k2=k1;
        k3=kr;
        k4=k3;
        lf=get_cg(FSAE_Race_Car);
        lr=(FSAE_Race_Car.chassis.wheelbase/12)-lf;
        rf=FSAE_Race_Car.chassis.radius_f/12;
        rr=FSAE_Race_Car.chassis.radius_r/12;
        K=[k1+k2+k3+k4,-(k1+k2)*lf+(k3+k4)*lr, -(k1-k2)*rf+(k3-k4)*rr; -(k1+k2)*lf+(k3+k4)*lr, (k1+k2)*lf^2+(k3+k4)*lr^2, (k1-k2)*lf*rf+(k3-k4)*lr*rr; -(k1-k2)*rf+(k3-k4)*rr, (k1-k2)*lf*rf+(k3-k4)*lr*rr, (k1+k2)*rf^2+(k3+k4)*rr^2];
        
        
    elseif strcmp(vibration_model,'full_car_7_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        kf=lrf*FSAE_Race_Car.suspension_front.k*12; %convert to ft
        kr=lrr*FSAE_Race_Car.suspension_rear.k*12; %convert to ft
        kwf=FSAE_Race_Car.wheel_front.k*12; %convert to ft
        kwr=FSAE_Race_Car.wheel_rear.k*12; %convert to ft  
        k1=kf;
        k2=k1;
        k3=kr;
        k4=k3;
        lf=get_cg(FSAE_Race_Car);
        lr=(FSAE_Race_Car.chassis.wheelbase/12)-lf;
        kwf=FSAE_Race_Car.wheel_front.k*12; %convert to ft
        kwr=FSAE_Race_Car.wheel_rear.k*12; %convert to ft
        rf=FSAE_Race_Car.chassis.radius_f/12;
        rr=FSAE_Race_Car.chassis.radius_r/12;
        K=[k1+k2+k3+k4,-(k1+k2)*lf+(k3+k4)*lr,-(k1-k2)*rf+(k3-k4)*rr,-k1,-k2,-k3,-k4; -(k1+k2)*lf+(k3+k4)*lr,(k1+k2)*lf^2+(k3+k4)*lr^2,(k1-k2)*lf*rf+(k3-k4)*lr*rr,k1*lf,k2*lf,-k3*lr,-k4*lr; -(k1-k2)*rf+(k3-k4)*rr,(k1-k2)*lf*rf+(k3-k4)*lr*rr, (k1+k2)*rf^2+(k3+k4)*rr^2, k1*rf, -k2*rf, -k3*rr, k4*rr; -k1, k1*lf, k1*rf, k1+kwf,0,0,0; -k2, k2*lf, -k2*rf, 0, k2+kwf, 0,0; -k3, -k3*lr, -k3*rr, 0,0, k3+kwr, 0; -k4, -k4*lr, k4*rr, 0,0,0,kr+kwr];
        
        
    else
        error('you did not enter the one of the DOF strings!')
    end
    
else
    error('you did not input the correct car structure')
end
end
