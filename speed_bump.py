function [ R_f, R_r, R_dot_f, R_dot_r ] = speed_bump( wheelbase, X_enter, X, V )
%This function models a speed bump. Included input arguements are wheelbase
%(distance between axles), X enter (locates the entrace of the speed bump),
%X (location of front axle along roadway), and V (velocity of the vehicle)
if wheelbase <= 0 || X<0 || V<0
    error(' One of the input arguemnts is not positive')
end
if isscalar(wheelbase)==0 || isscalar(X_enter)==0 || isscalar(X)==0 || isscalar(V)==0
    error('One of your inputs is not a scalar')
end
if X_enter <0
    error('X_enter is not greater or equal to 0')
end

length = 1;
height= 2/12;
top= 3/12;
R_f=0;
R_r=0;
R_dot_f=0;
R_dot_r=0;

%This if statement represented the situation if the position of the FRONT wheel is located
%during the bump

if (X_enter<=X) && (X<=(X_enter+length))
    [R_f, R_dot_f]=bump(length,height, top, X-X_enter, V);
end

%This if statement represented the situation if the position of the REAR wheel is located
%during the bump

if (X_enter<=(X-wheelbase)) && ((X-wheelbase)<(X_enter+length))
    [R_r, R_dot_r]=bump(length,height, top, X-X_enter-wheelbase, V);

end

end

