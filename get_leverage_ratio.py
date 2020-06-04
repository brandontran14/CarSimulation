
# def LR = get_leverage_ratio(front_or_rear, FSAE_Race_Car)

# %This function takes in two inputs
# %input 1: a string called front or rear.
# %Must input as 'front' or 'rear' or will return an error.
# %input 2: the strucute called FSAE_Race_Car. Any car can be loaded
# %into that structure, but it must be a car structure otherwise
# %the function will return an error.
# %the function output returns the leverage ratio as a scalar!

# if isstruct(FSAE_Race_Car) == 1
#     if strcmp(front_or_rear,'front')
#         if strcmp(FSAE_Race_Car.suspension_front.location,'inboard') ==1
#             LR=(FSAE_Race_Car.suspension_front.travel/FSAE_Race_Car.wheel_front.travel)^2; 
#         else
#             LR=cos(FSAE_Race_Car.suspension_front.angle*(pi/180));
#         end
#     elseif strcmp(front_or_rear, 'rear')
#         if strcmp(FSAE_Race_Car.suspension_rear.location, 'inboard') ==1
#             LR=(FSAE_Race_Car.suspension_rear.travel/FSAE_Race_Car.wheel_rear.travel)^2;
#         else
#             LR=cos(FSAE_Race_Car.suspension_rear.angle*(pi/180));
#         end
#     else
#         error(' front or rear was not specified, GET OUT!')
        
#     end
# else
#     error('you did not input a car file!')
# end

import math
def get_LR(side, FSAE_Race_Car):
    if(isinstance(FSAE_Race_Car, dict)):
        if (side == "front"):
            if(FSAE_Race_Car["suspension_front"]["location"] == "inboard"):
                return (FSAE_Race_Car["suspension_front"]["travel"]/FSAE_Race_Car["wheel_front"]["travel"])**2
            else:
                return math.cos(FSAE_Race_Car["suspension_front"]["angle"]*(pi/180))
        elif (side == "rear"):
            if(FSAE_Race_Car["suspension_rear"]["location"] == "inboard"):
                return (FSAE_Race_Car["suspension_rear"]["travel"]/FSAE_Race_Car["wheel_rear"]["travel"]) **2
            else:
                return math.cos(FSAE_Race_Car["supension_rear"]["angle"]*(pi/180))
    raise ValueError("You didnt not input a car file or a side of the car")