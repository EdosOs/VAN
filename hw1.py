import Navigation
import math
import numpy as np
import robot
import matplotlib.pyplot as plt
import pandas as pd
roll = math.pi/4
pitch = math.pi/5
yaw = math.pi/7# roll = math.pi/4

new_RotMat = np.array([[0.813797681, -0.440969611, 0.378522306],
                       [0.46984631, 0.882564119, 0.0180283112],
                       [-0.342020143, 0.163175911, 0.925416578]])
# roll = 0
# pitch = 0
# yaw = math.pi/2
Body_To_Global_R = Navigation.Euler_to_RotMat(roll = roll ,pitch = pitch,yaw = yaw)
R_to_Euler = Navigation.RotMat_to_Euler(Body_To_Global_R)
# C
new_Euler = Navigation.RotMat_to_Euler(new_RotMat)*180/math.pi

# 2
l_g = np.array([[450,400,50]]).T
R_C_G = np.array([[0.5363, -0.8440, 0],[0.8440, 0.5363, 0] ,[0, 0 ,1]])
l_c = R_C_G*l_g
t_G_C_to_G = np.array([[-451.2459,257.0322,400]])
T_G_C = robot.calc_T(t = pd.DataFrame(t_G_C_to_G , columns={'x','y','z'} , index=None).iloc[0],R = R_C_G, dim=3)


#3
steps = 0
pos = np.array([0,0,0])
pos1 = np.array([0,0,0])
pos_arr = [[0,0,0]]
pos_arr1 = [[0,0,0]]
R = Navigation.Euler_to_RotMat(roll = 0 ,pitch = 0,yaw = np.pi/180)
R1 = Navigation.Euler_to_RotMat(roll = 0 ,pitch = 0,yaw = 0)
R_arr = [R]
R_arr1 = [R1]
while steps<30:
    R,pos = robot.move_robot(R = R , step = 1.01 , pos = pos , angle = np.pi/180)
    # pos_arr.append(pos+np.random.randn())
    pos_arr.append(pos)
    R1,pos1 = robot.move_robot(R = R1 , step = 1.0 , pos = pos1 , angle = 0)
    pos_arr1.append(pos1)

    R_arr.append(R)
    R_arr1.append(R1)
    steps+=1

positions_skewd = pd.DataFrame(pos_arr , columns={'x','y','z'})
positions_neutral = pd.DataFrame(pos_arr1 , columns={'x','y','z'})

T_arr =np.array([robot.calc_T(positions_skewd.iloc[i] , R_arr[i] , dim = 2) for i in range(len(R_arr))])
plt.figure()
plt.plot(positions_skewd['x'],positions_skewd['y'] , '.b')
plt.plot(positions_neutral['x'],positions_neutral['y'] , '.r')
plt.title('Agents positions')
plt.xlabel('X [m]')
plt.ylabel('Y [m]')
plt.grid()
plt.legend(['Skewd' , 'Neutral'])
ax = plt.gca()
ax.set_aspect('equal', adjustable='box')
plt.draw()
