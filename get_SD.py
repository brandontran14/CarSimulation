import numpy as np
import numpy.linalg
def get_SD(model, Car): 
    if(not isinstance(Car,dict)):
        return ValueError("You did not supply the right Car struct")
    k = get_SM(model,Car)
    if(model == "quarter_car_1_DOF"):
        z0 = (Car[pilot][weight] + Car[chassis][weight] + Car[power_plant][weight])/(4*k)
    elif(model == "quarter_car_2_DOF"):
        wm = np.array([
            [(Car[pilot][weight]+Car[chassis][weight]+Car[power_plant][weight])/4],
            [(Car[wheel_front][weight] + Car[wheel_rear][weight])/2]
        ])
        z0 = np.linalg.lstsq(k,wm)
    elif(model == "half_car_2_DOF"):
        wm = np.array([
            [(Car[pilot][weight]+Car[chassis][weight]+Car[power_plant][weight])/2],
            [0]
        ])
        z0 = np.linalg.lstsq(k,wm)
    elif(model == "half_car_4_DOF"):
        wm = np.array([
            [(Car[pilot][weight] + Car[power_plant][weight] + Car[chassis][weight])/2],
            [0],
            [Car[wheel_front][weight]],
            [Car[wheel_rear][weight]]
        ])
        z0 = np.linalg.lstsq(k,wm)
    elif(model == "full_car_3_DOF"):
        wm = np.array([
            [Car[pilot][weight] + Car[power_plant][weight] + Car[chassis][weight]],
            [0],
            [0]
        ])
        z0 = np.linalg.lstsq(k,wm)
    elif(model == "full_car_7_DOF"):
        wm = np.array([
            [Car[pilot][weight] + Car[power_plant][weight] + Car[chassis][weight]],
            [0],
            [0],
            [Car[wheel_front][weight]],
            [Car[wheel_front][weight]],
            [Car[wheel_rear][weight]],
            [Car[wheel_rear][weight]]
        ])
        z0 = np.linalg.lstsq(k,wm)
    else:
        return ValueError("You did not input right string in get_SD")
    return z0
