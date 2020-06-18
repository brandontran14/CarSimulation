#this function is for a bump
#inputs are length, height, length of top/flat portion of bump, position along bump, and velocity
#will return relative position and velocity going through the bump
import numpy as np, math
def bump(length,height,top,X,V):
    if(not np.isscalar(length)):
        return ValueError("All inputs must be scalars (bump)")
    if(not np.isscalar(height)):
        return ValueError("All inputs must be scalars (bump)")
    if(not np.isscalar(top)):
        return ValueError("All inputs must be scalars (bump)")
    if(not np.isscalar(X)):
        return ValueError("All inputs must be scalars (bump)") 
    if(not np.isscalar(V)):
        return ValueError("All inputs must be scalars (bump)")
    if (length <= 0):
        return ValueError("length must be positive")
    if(X>length):
        return ValueError("X must be <= length")
    if(top > length):
        return ValueError("top must be <= length")
    if(V<0):
        return ValueError("Velocity must be positive")


    if (X < ((length-top)/2)):
        phi_x = 2*math.pi*(X/(length-top))
    elif((length-top)/2 <= X and X <= (length+top)/2):
        phi_x = math.pi
    else:
        phi_x = 2*math.pi*(X-top)/(length-top)

    R = (height/2)*(1-math.cos(phi_x))
    dRdt = math.pi * (height/(length-top)) * math.sin(phi_x)*V
    return R, dRdt

