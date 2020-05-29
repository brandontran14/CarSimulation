function z0=get_static_deflection(vibration_model,FSAE_Race_Car)
%this function takes inputs vibration_model and FSAE_Race_Car
%and returns the static deflection z0
%vibration_model must be either 'quarter_car_1_DOF',
%'quarter_car_2_DOF',half_car_2_DOF', half_car_4_DOF, full_car_3_DOF, or
%full_car_7_DOF
%otherwise will return an error
%FSAE_Race_Car as an input must be the car structure, otherwise it will
%return an error.
%z0, the returned displacement vector will have units in ft or radians
if isstruct(FSAE_Race_Car) == 1
    
    if strcmp(vibration_model,'quarter_car_1_DOF')
        k=get_stiffness_matrix(vibration_model,FSAE_Race_Car);
        weight=(FSAE_Race_Car.pilot.weight+FSAE_Race_Car.chassis.weight+FSAE_Race_Car.power_plant.weight)/4;
        z0=weight/k;
        
    elseif strcmp(vibration_model,'quarter_car_2_DOF')
        k=get_stiffness_matrix(vibration_model,FSAE_Race_Car);
        weight=(FSAE_Race_Car.pilot.weight+FSAE_Race_Car.chassis.weight+FSAE_Race_Car.power_plant.weight)/4;
        weightw=(FSAE_Race_Car.wheel_front.weight + FSAE_Race_Car.wheel_rear.weight)/2;
        weightmatrix=[weight;weightw];
        z0=k\weightmatrix;
        
    elseif strcmp(vibration_model,'half_car_2_DOF')
        k=get_stiffness_matrix(vibration_model,FSAE_Race_Car);
        weight=(FSAE_Race_Car.pilot.weight+FSAE_Race_Car.power_plant.weight+FSAE_Race_Car.chassis.weight)/2;
        z0=k\[weight;0];
        
    elseif strcmp(vibration_model, 'half_car_4_DOF')
        k=get_stiffness_matrix(vibration_model,FSAE_Race_Car);
        weight=(FSAE_Race_Car.pilot.weight+FSAE_Race_Car.power_plant.weight+FSAE_Race_Car.chassis.weight)/2;
        weightf=FSAE_Race_Car.wheel_front.weight;
        weightr=FSAE_Race_Car.wheel_rear.weight;
        z0=k\[weight;0;weightf;weightr];
    elseif strcmp(vibration_model,'full_car_3_DOF')
        k=get_stiffness_matrix(vibration_model,FSAE_Race_Car);
        weight=(FSAE_Race_Car.pilot.weight+FSAE_Race_Car.power_plant.weight+FSAE_Race_Car.chassis.weight);
        z0=k\[weight;0;0];
    elseif strcmp(vibration_model,'full_car_7_DOF')
        k=get_stiffness_matrix(vibration_model,FSAE_Race_Car);
        weight=(FSAE_Race_Car.pilot.weight+FSAE_Race_Car.power_plant.weight+FSAE_Race_Car.chassis.weight);
        weightf=FSAE_Race_Car.wheel_front.weight;
        weightr=FSAE_Race_Car.wheel_rear.weight;
        z0=k\[weight;0;0;weightf;weightf;weightr;weightr];
    else
        error('you did not input the right string!')
    end
    
else
    error('you did not input the right car structure for FSAE_Race_Car')
end
end
