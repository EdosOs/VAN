import Navigation
import numpy as np
def move_robot(R ,step , pos , angle):
    pos = pos + np.array([step ,0, 0])@ R
    R = R@Navigation.Euler_to_RotMat(roll = 0 ,pitch = 0,yaw = angle)
    return R , pos

def calc_T(t ,R , dim):
    if dim == 2 :
        T = np.array([
            [R[0,0] , R[0,1] ,t['x'] ],
            [R[1, 0], R[1, 1], t['y']],
            [   0,       0,      1],
             ])
    elif dim == 3:
        T = np.array([
            [R[0,0], R[0,1], R[0,2], t['x']],
            [R[1,0], R[1,1], R[1,2],  t['y']],
            [R[2,0], R[2,1], R[2,2],  t['z']],
            [   0,       0,     0,      1],
             ])
    return T
