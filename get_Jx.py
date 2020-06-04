import math, numpy

def get_Jx(Car):
    if(not isinstace(Car,dict)):
        return ValueError("You did not supply the right Car struct")
    g = 32.174
# Chassis
    C_diameter = Car[chassis][diameter]/12
    C_radius = C_diameter/2
    C_length = Car[chassis][length]/12
    C_mass = Car[chassis][weight]/g
    C_cgz = Car[chassis][cg_Z]/12
    C_I = (C_mass*C_radius)**2
    c_J = C_I+(C_mass*(C_cgz**2))
# Engine
    E_diamter = Car[power_plant][diameter]/12
    E_radius = E_diameter/2
    E_mass = Car[power_plant][weight]/g
    E_cgZ = Car[chassis][motor_Z]/12
    E_I = (2/5)*E_mass*E_radius**2
    E_J = E_I+(E_mass*(E_cgZ**2))
# Pilot
    P_radius = Car[pilot][girth]/(12*2*math.pi)
    P_leglength = 0.6 * Car[pilot][height]/12
    P_legmass = 0.4 * Car[pilot][weight]/g
    P_legcgZ = Car[chassis][seat_Z]/12 + P_radius
    P_legI = 0.5 * P_legmass * (P_radius**2)
    P_legJ = P_legI + (P_legmass * (P_legcgZ**2))
    P_torsolength = 0.4 * Car[pilot][height]/12
    P_torsomass = 0.6 * Car[pilot][weight]/g
    P_torsocgZ = (Car[chassis][seat_Z]/12) + (Car[pilot][girth]/(12*math.pi)) +() Car[pilot][height]/(5/12))
    P_torsoI = (P_torsomass/12) * (3*(P_radius**2)) + (P_torsolength**2)
    P_torsoJ = P_torsoI + P_torsomass * (P_torsocgZ**2)

    return C_J + E_J + P_legJ + P_torsoJ # ft-lb/(rad/sec^2)