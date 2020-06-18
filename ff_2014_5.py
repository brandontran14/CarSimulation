#forcing function data structure
import car_2014, trajectory, speed_bump, bump
ff_data = {"t_prev": 0,
            "X_prev": 0,
            "car": car_2014.Car,
            "model": "full_car_3_DOF",
            "trajectory": trajectory.trajectory,
            "t_in": 0,
            "t_out": 1.5,
            "V_in": 5,
            "V_out": 5,
            "N": 2500,
            "roadway_d": speed_bump.speed_bump,
            "X_enter_d": 1,
            "roadway_p": speed_bump.speed_bump,
            "X_enter_p": 3
            }



