#this function returns the leverage ratio for the car
#inputs are side of car and car struct
#outputs are the leverage ratio
import math
def get_LR(side, Car):
    if(isinstance(Car, dict)):
        if (side == "front"):
            if(Car["suspension_front"]["location"] == "inboard"):
                return (Car["suspension_front"]["travel"]/Car["wheel_front"]["travel"])**2
            else:
                return math.cos(Car["suspension_front"]["angle"]*(math.pi/180))
        elif (side == "rear"):
            if(Car["suspension_rear"]["location"] == "inboard"):
                return (Car["suspension_rear"]["travel"]/Car["wheel_rear"]["travel"]) **2
            else:
                return math.cos(Car["supension_rear"]["angle"]*(math.pi/180))