


function M=get_mass_matrix(vibration_model,FSAE_Race_Car)

%Task 3a assembling mass matrix
%input vibration_model and car, returns M
%This function has two inputs
%input 1: enter a string, either 'quarter_car_1_DOF', 'quarter_car_2_DOF'
%'half_car_2_DOF', 'half_car_4_DOF', 'full_car_3_DOF', or 'full_car_7_DOF'
%any other inputs will result in an error.
%input 2: enter the FSAE_Race_Car structure, you must have the structure
%defined if you enter an other structure there will be an error
%This function returns the mass matrix for the given vibration model
%returns mass matrix in slugs and moments of inertia in ft-lb
if isstruct(FSAE_Race_Car) == 1
    if strcmp(vibration_model,'quarter_car_1_DOF')
        w=FSAE_Race_Car.pilot.weight + FSAE_Race_Car.power_plant.weight+FSAE_Race_Car.chassis.weight;
        M=w/(4*32.174); %in slugs
    elseif strcmp(vibration_model, 'quarter_car_2_DOF')
         w1=FSAE_Race_Car.pilot.weight + FSAE_Race_Car.power_plant.weight+FSAE_Race_Car.chassis.weight;
         m=w1/(4*32.174);
         w2=FSAE_Race_Car.wheel_rear.weight + FSAE_Race_Car.wheel_front.weight;
         mw=w2/(2*32.174);
         M=[m,0;0,mw]; %in slugs
         
    elseif strcmp(vibration_model,'half_car_2_DOF')
        J=get_Jy(FSAE_Race_Car)/2;
        w1=FSAE_Race_Car.pilot.weight + FSAE_Race_Car.power_plant.weight + FSAE_Race_Car.chassis.weight;
        m1=w1/(2*32.174);
        m2=J;
        M=[m1,0;0,m2];
    elseif strcmp(vibration_model,'half_car_4_DOF')
        J=get_Jy(FSAE_Race_Car)/2;
        w1=FSAE_Race_Car.pilot.weight + FSAE_Race_Car.power_plant.weight + FSAE_Race_Car.chassis.weight;
        m1=w1/(2*32.174);
        m2=J;
        wf=(FSAE_Race_Car.wheel_front.weight)/32.174;
        wr=(FSAE_Race_Car.wheel_rear.weight)/32.174;
        M=[m1,0,0,0;0,m2,0,0;0,0,wf,0;0,0,0,wr];
    elseif strcmp(vibration_model,'full_car_3_DOF')
        Jy=get_Jy(FSAE_Race_Car);
        Jx=get_Jx(FSAE_Race_Car);
        w1=FSAE_Race_Car.pilot.weight + FSAE_Race_Car.power_plant.weight + FSAE_Race_Car.chassis.weight;
        m1=w1/32.174;
        M=[m1, 0 ,0; 0, Jy, 0; 0, 0, Jx];
    elseif strcmp(vibration_model,'full_car_7_DOF')
        Jy=get_Jy(FSAE_Race_Car);
        Jx=get_Jx(FSAE_Race_Car);
        w1=FSAE_Race_Car.pilot.weight + FSAE_Race_Car.power_plant.weight + FSAE_Race_Car.chassis.weight;
        m1=w1/32.174;
        wf=(FSAE_Race_Car.wheel_front.weight)/32.174;
        wr=(FSAE_Race_Car.wheel_rear.weight)/32.174;
        M=[m1, 0, 0,0,0,0,0;0,Jy,0,0,0,0,0;0,0,Jx,0,0,0,0;0,0,0,wf,0,0,0;0,0,0,0,wf,0,0;0,0,0,0,0,wr,0;0,0,0,0,0,0,wr];
        
    else
        error('you did not input the right vibration model!')
    end
    
else
    error(' you did not input the right file for the car!')
end
