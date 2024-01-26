import numpy as np
import math
def Euler_to_RotMat(roll,pitch,yaw):
    Rx = np.array([[1 ,0 ,0] ,
          [0 ,math.cos(roll) , math.sin(roll)] ,
          [0 ,-math.sin(roll) ,math.cos(roll)]])

    Ry = np.array([[math.cos(pitch) ,0 ,-math.sin(pitch)] ,
                    [0 ,1 ,0] ,
                    [math.sin(pitch) ,0 ,math.cos(pitch)]])

    Rz = np.array([[math.cos(yaw) , math.sin(yaw),0] ,
          [-math.sin(yaw) ,math.cos(yaw),0],
          [0 ,0 ,1]])
    return np.dot(np.dot(Rz,Ry),Rx)

def RotMat_to_Euler(R):
    theta = math.asin(R[2,0])
    phi = math.acos(R[2,2]/math.cos(theta))
    psi = math.acos(R[0,0]/math.cos(theta))
    return np.array([phi , theta ,psi]) # roll Pitch yaw