# % FSAE Race Car Data Structure for 2014 
import importlib

import driver_sally
import chassis_2014, motor_2014, suspension_front_2014, suspension_rear_2014, wheel_front_2014, wheel_rear_2014

pilot = driver_sally.pilot
chassis = chassis_2014.chassis
power_plant = motor_2014.power_plant
suspension_front = suspension_front_2014.suspension_front
suspension_rear = suspension_rear_2014.suspension_rear
wheel_front = wheel_front_2014.wheel_front
wheel_rear = wheel_rear_2014.wheel_rear

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
