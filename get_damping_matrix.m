function C=get_damping_matrix(vibration_model,FSAE_Race_Car)
%this function returns the damping matrix given a vibration model and Race
%Car input
%the input vibration_model must be either 'quarter_car_1_DOF', 
%quarter_car_2_DOF, half_car_2_DOF, half_car_4_DOF, full_car_3_DOF, or full_car_7_DOF. any other string will return an error.
%the second input is the FSAE_Race_Car structure that will be defined
%before. any other strucure that is not the race car structure will return
%an error. 
%returns damping ratio in lb/(ft/sec) or ft-lb/(rad/sec)
if isstruct(FSAE_Race_Car) ==1
    if strcmp(vibration_model,'quarter_car_1_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        cf=lrf*FSAE_Race_Car.suspension_front.c*12; %convert to ft
        cr=lrr*FSAE_Race_Car.suspension_rear.c*12;  %convert to ft
        c=(cf+cr)/2;
        C=[c];
    elseif strcmp(vibration_model,'quarter_car_2_DOF') == 1
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        cf=lrf*FSAE_Race_Car.suspension_front.c*12;
        cr=lrr*FSAE_Race_Car.suspension_rear.c*12;
        cwf=FSAE_Race_Car.wheel_front.c*12; %convert to ft
        cwr=FSAE_Race_Car.wheel_rear.c*12;
        c=(cf+cr)/2;
        cw=(cwf+cwr)/2;
        C=[c,-c;-c,c+cw];
    elseif strcmp(vibration_model, 'half_car_2_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        cf=lrf*FSAE_Race_Car.suspension_front.c*12;
        cr=lrr*FSAE_Race_Car.suspension_rear.c*12;
        c1=cf;
        c2=cr;
        cwf=FSAE_Race_Car.wheel_front.c*12; %convert to ft
        cwr=FSAE_Race_Car.wheel_rear.c*12;
        lf=get_cg(FSAE_Race_Car);
        lr=FSAE_Race_Car.chassis.wheelbase/12-lf;
        C=[c1+c2,-c1*lf+c2*lr;-c1*lf+c2*lr,c1*lf^2+c2*lr^2];
        
    elseif strcmp(vibration_model, 'half_car_4_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        cf=lrf*FSAE_Race_Car.suspension_front.c*12;
        cr=lrr*FSAE_Race_Car.suspension_rear.c*12;
        c1=cf;
        c2=cr;
        cwf=FSAE_Race_Car.wheel_front.c*12; %convert to ft
        cwr=FSAE_Race_Car.wheel_rear.c*12;
        lf=get_cg(FSAE_Race_Car);
        lr=FSAE_Race_Car.chassis.wheelbase/12-lf;
        C=[c1+c2,-c1*lf+c2*lr,-c1,-c2;-c1*lf+c2*lr,c1*lf^2+c2*lr^2,c1*lf,-c2*lr;-c1,c1*lf,c1+cwf,0;-c2,-c2*lr,0,c2+cwr];
        
    elseif strcmp(vibration_model,'full_car_3_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        cf=lrf*FSAE_Race_Car.suspension_front.c*12;
        cr=lrr*FSAE_Race_Car.suspension_rear.c*12;
        c1=cf;
        c2=c1;
        c3=cr;
        c4=c3;
        lf=get_cg(FSAE_Race_Car);
        lr=FSAE_Race_Car.chassis.wheelbase/12-lf;
        rf=FSAE_Race_Car.chassis.radius_f/12;
        rr=FSAE_Race_Car.chassis.radius_r/12;
        C=[c1+c2+c3+c4,-(c1+c2)*lf+(c3+c4)*lr,-(c1-c2)*rf+(c3-c4)*rr;-(c1+c2)*lf+(c3+c4)*lr,(c1+c2)*lf^2+(c3+c4)*lr^2,(c1-c2)*lf*rf+(c3-c4)*lr*rr;-(c1-c2)*rf+(c3-c4)*rr,(c1-c2)*lf*rf+(c3-c4)*lr*rr,(c1+c2)*rf^2+(c3+c4)*rr^2];
        
    elseif strcmp(vibration_model,'full_car_7_DOF')
        lrf=get_leverage_ratio('front',FSAE_Race_Car);
        lrr=get_leverage_ratio('rear',FSAE_Race_Car);
        cf=lrf*FSAE_Race_Car.suspension_front.c*12;
        cr=lrr*FSAE_Race_Car.suspension_rear.c*12;      
        c1=cf;
        c2=c1;
        c3=cr;
        c4=c3;
        lf=get_cg(FSAE_Race_Car);
        lr=FSAE_Race_Car.chassis.wheelbase/12-lf;
        rf=FSAE_Race_Car.chassis.radius_f/12;
        rr=FSAE_Race_Car.chassis.radius_r/12;
        cwf=FSAE_Race_Car.wheel_front.c*12; %convert to ft
        cwr=FSAE_Race_Car.wheel_rear.c*12;
        C=[c1+c2+c3+c4,-(c1+c2)*lf+(c3+c4)*lr,-(c1-c2)*rf+(c3-c4)*rr,-c1,-c2,-c3,-c4;-(c1+c2)*lf+(c3+c4)*lr,(c1+c2)*lf^2+(c3+c4)*lr^2,(c1-c2)*lf*rf+(c3-c4)*lr*rr,c1*lf,c2*lf,-c3*lr,-c4*lr; -(c1-c2)*rf+(c3-c4)*rr,(c1-c2)*lf*rf+(c3-c4)*lr*rr,(c1+c2)*rf^2+(c3+c4)*rr^2, c1*rf,-c2*rf,-c3*rr,c4*rr;-c1,c1*lf,c1*rf,c1+cwf,0,0,0;-c2,c2*lf,-c2*rf,0,c2+cwf,0,0;-c3,-c3*lr,-c3*rr,0,0,c3+cwr,0;-c4,-c4*lr,c4*rr,0,0,0,c4+cwr];
        
    else
        error(' you did not enter quarter_car_1_DOF, quarter_car_2_DOF, half_car_2_DOF, half_car_4_DOF, full_car_3_DOF, or full_car_7_DOF!')
    end
else
    error('you did not input the right structure for FSAE_Race_Car')
end
end

