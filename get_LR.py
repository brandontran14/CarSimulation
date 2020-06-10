import math
def get_LR(side, FSAE_Race_Car):
    if(isinstance(FSAE_Race_Car, dict)):
        if (side == "front"):
            if(FSAE_Race_Car["suspension_front"]["location"] == "inboard"):
                return (FSAE_Race_Car["suspension_front"]["travel"]/FSAE_Race_Car["wheel_front"]["travel"])**2
            else:
                return math.cos(FSAE_Race_Car["suspension_front"]["angle"]*(math.pi/180))
        elif (side == "rear"):
            if(FSAE_Race_Car["suspension_rear"]["location"] == "inboard"):
                return (FSAE_Race_Car["suspension_rear"]["travel"]/FSAE_Race_Car["wheel_rear"]["travel"]) **2
            else:
                return math.cos(FSAE_Race_Car["supension_rear"]["angle"]*(math.pi/180))
    raise ValueError("You didnt not input a car file or a side of the car")