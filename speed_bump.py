#this function models a speed bump
#takes wheelbase, entering position, x coordinate, and velocity as inputs
#returns fron and rear position/velocities of tires
import numpy as np, bump
def speed_bump(wheelbase,X_enter,X,V):
    if(wheelbase <= 0 or X < 0 or V < 0 or X_enter < 0):
        return ValueError("one of the input arguments is not positive")
    if(not (np.isscalar(wheelbase) or np.isscalar(X_enter) or np.isscalar(X) or np.isscalar(V))):
        return ValueError("one of your inputs isnt a scalar")
    length, height, top, R_f, R_r, R_dot_f, R_dot_r = 1, 2/12, 3/12, 0, 0, 0, 0
    if(X_enter <= X and X <= (X_enter+length)):
        R_f, R_dot_f = bump.bump(length,height,top,X-X_enter,V)
    if(X_enter <= (X-wheelbase) and (X-wheelbase) < (X_enter+length)):
        R_r, R_dot_r = bump.bump(length,height, top, X-X_enter-wheelbase, V)
    return R_f, R_r, R_dot_f, R_dot_r