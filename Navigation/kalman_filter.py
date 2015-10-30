import math
import serial
import numpy as np

Q_angle = 0.01
Q_gyro = 0.0003
R_angle = 0.03

x_bias = 0
y_bias = 0
z_bias = 0
P_00 = 0
P_01 = 0
P_10 = 0
P_11 = 0

dt = 0.18
newAngle = []
newRate = []
newAngle.append(atan2(accy/accz))
newAngle.append(atan2(accz/accx))
newAngle.append(atan2(accx/accy))
newRate.append(gyrox)
newRatey.append(gyroy)
newRatez.append(gyroz)


def kalmanCalculate(newAngle, newRate, dt):
    x_angle += dt * (newRate[1] - x_bias)
    y_angle += dt * (nemRate[2] - y_bias)
    z_angle += dt * (nemRate[3] - z_bias)
    P_00 += - dt * (P_10 + P_01) + Q_angle * dt
    P_01 += - dt * P_11
    P_10 += - dt * P_11
    P_11 += + Q_gyro * dt

    y_x = newAnglex - x_angle
    y_y = newAngley - y_angle
    y_z = newAnglez - z_angle
    S = P_00 + R_angle
    K_0 = P_00 / S
    K_1 = P_10 / S

    x_angle += K_0 * y_x
    y_angle += K_0 * y_y
    z_angle += K_0 * y_z
    x_bias += K_1 * y_x
    y_bias += K_1 * y_y
    z_bias += K_1 * y_z
    P_00 -= K_0 * P_00
    P_01 -= K_0 * P_01
    P_10 -= K_1 * P_00
    P_11 -= K_1 * P_01
    angles = [x_angle, y_angle, z_angle]
    return angles
