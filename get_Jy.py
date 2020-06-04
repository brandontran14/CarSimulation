import math, numpy
def get_Jy(Car):
    if(not isinstace(Car,dict)):
        return ValueError("You did not supply the right Car struct")
    g = 32.174
    cg=get_cg(Car)
# Chassis
    C_diameter = Car[chassis][diameter]/12
    C_length = Car[chassis][length]/12
    C_mass = Car[chassis][weight]/g
    C_cg = Car[chassis][cg_X]/12
    I_C = (C_mass/12)*(6*(C_diameter/2)**2 + C_length**2) + (C_mass * (cg-C_cg)**2)
# Engine
    P_diameter = Car[power_plant][diameter]/12
    P_mass = Car[power_plant][weight]/g
    P_cg = Car[chassis][motor_X]/12
    I_P = (2/5) * P_mass * (P_diameter/2)**2 + P_mass * (P_cg-cg)**2
# Pilot
    P_legmass = 0.6 * Car[pilot][weight]/g
    P_leglength = 0.4 * Car[pilot][height]/12
    P_legcg = (Car[chassis][seat_X]/12) - 0.5 * P_leglength
    P_radius = Car[pilot][girth]/(2*12*math.pi)
    P_torsomass = 0.6 * Car[pilot][weight]/g
    P_torsolength = 0.4 * Car[pilot][height]/12
    P_torsocg = (Car[chassis][seat_X]/12) - P_radius
    I_L = (P_legmass/12) * (3 * P_radius**2 + P_leglength**2) + P_legmass * (P_legcg - cg)**2
    I_T = (P_torsomass/12) * (3 * (P_radius**2) + P_torsolength**2) + P_torsomass * (P_torsocg-cg)**2

    return (I_C + I_P + I_L + I_T)



