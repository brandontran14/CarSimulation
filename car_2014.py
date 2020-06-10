# % FSAE Race Car Data Structure for 2014 
import importlib
import driver_sally, chassis_2014, motor_2014, suspension_front_2014, suspension_rear_2014, wheel_front_2014, wheel_rear_2014

pilot = driver_sally.pilot
chassis = chassis_2014.chassis
power_plant = motor_2014.power_plant
suspension_front = suspension_front_2014.suspension_front
suspension_rear = suspension_rear_2014.suspension_rear
wheel_front = wheel_front_2014.wheel_front
wheel_rear = wheel_rear_2014.wheel_rear


# value01 = '2014 Texas A&M';       
# value02 = 2014;            
# value03 = 62;                %mph
# value04 = 3.84;              %sec
# value05 = pilot;
# value06 = chassis;          
# value07 = power_plant;             
# value08 = suspension_front;              
# value09 = suspension_rear;             
# value10 = wheel_front;               
# value11 = wheel_rear;              

# FSAE_Race_Car = struct(field01, value01, field02, value02, field03, value03, field04, value04, field05, value05, field06, value06, field07, value07, field08, value08, field09, value09, field10, value10, field11, value11);



Car = {"team": "2014 Texas A&M", 
            "year": 2014,
            "top_speed": 62, 
            "t2top_speed": 3.84, 
            "pilot": pilot, 
            "chassis": chassis,
            "power_plant": power_plant,
            "suspension_front": suspension_front,
            "suspension_rear": suspension_rear,
            "wheel_front": wheel_front,
            "wheel_rear": wheel_rear
            }
