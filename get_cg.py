import math, numpy
def get_cg(Car):
    if(not isinstace(Car,dict)):
        return ValueError("You did not supply the right Car struct")
    wc = Car[chassis][weight]
    cx = Car[chassis][cg_X]
    sx = Car[chassis][seat_X]
    mx = Car[chassis][motor_X]
    wp - Car[pilot][weight]
    wm - Car[power_plant][weight]
    weightleg = 0.4 * wp 
    weighttorso = 0.6 wp 
    legx = sx - 0.5 * 0.6 * Car[pilot][height]
    torsox = sx - (Car[pilot][girth]/(2*math.pi))
    F = wc + wm + wp 
    M = wc * cx + mx*wm + weightleg*legx + torsox*weighttorso 
    
    return ((M/F)/12)


    
