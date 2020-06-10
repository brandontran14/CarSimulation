import math
def trajectory(t,X,h,t_in,t_out,V_in,V_out,Car):
    V_top = Car["top_speed"]
    t_top = Car['t2top_speed']
    if(t_in < 0):
        return ValueError("t_in must be greater than zero")
    if(t_out < t_in):
        return ValueError("t_out must be less than t_in")
    if(t < t_in):
        return ValueError("t must be greater than t_in")
    if(h <= 0):
        return ValueError("h must be greater than zero")
    if (t+h > t_out):
        return ValueError("t_out must be greater than t+h")
    if(X<0):
        return ValueError("X must be positive or zero")
    if(V_in < 0):
        return ValueError("V_in must be positive or zero")
    if(V_out < 0):
        return ValueError("V_out must be positive or zero")
    if(Car['top_speed'] < V_in):
        return ValueError("Top speed must be greater than V_in")
    if(Car['top_speed'] < V_out):
        return ValueError("Top speed must be greater than V_out")
    if(V_out > V_in):
        if( ((V_out-V_in)/(t_out-t_in)) > (V_top/t_top)):
            return ValueError("trajectory is greater than max acceleration")
    if(V_out < V_in):
        if( ((5280*(V_out-V_in)/3600)/(t_out-t_in)) < (-1.4*32.174)):
            return ValueError("trajectory deceleration is greater than max deceleration")
    V_out = 5280*V_out/3600
    V_in = 5280 *V_in/3600
    V_t = V_in + ((V_out - V_in) / 2) * (1 - math.cos(math.pi * ((t - t_in) / (t_out - t_in))))
    V_th2 = V_in + ((V_out - V_in) / 2) * (1 - math.cos(math.pi * (((t + h/2) - t_in) / (t_out - t_in))))
    V_th = V_in + ((V_out - V_in) / 2) * (1-math.cos(math.pi * (((t+h) - t_in) / (t_out - t_in))))
    X = X + ((h / 6) * (V_t + 4 * V_th2 + V_th))
    V = V_t
    t = t+h
    return t,X,V

# %disp('Location of front axle at end of step (ft)')
# %disp(X)
# %disp('Velocity of the vehicle at end of step (ft/s)')
# %disp(V)
# %disp('Time at end of integration step (s)')
# %disp(t)



