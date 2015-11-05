import math
import serial
import numpy as np
import pickle
import matplotlib.pyplot as plt

def kalmanCalculate(lastAngle, newAngle, newRate, Pk, biask):
    lastAngle[0] += dt * (newRate[0] - biask[0])
    lastAngle[1] += dt * (newRate[1] - biask[1])
    lastAngle[2] += dt * (newRate[2] - biask[2])
    Pk[0][0] += - dt * (Pk[1][0] + Pk[0][1]) + qAngle * dt
    Pk[0][1] += - dt * Pk[1][1]
    Pk[1][0] += - dt * Pk[1][1]
    Pk[1][1] += + qGyro * dt

    Y = []
    Y.append(newAngle[0] - lastAngle[0])
    Y.append(newAngle[1] - lastAngle[1])
    Y.append(newAngle[2] - lastAngle[2])
    S = Pk[0][0] + rAngle
    k = []
    k.append(Pk[0][0] / S)
    k.append(Pk[1][0] / S)

    lastAngle[0] += k[0] * Y[0]
    lastAngle[1] += k[0] * Y[1]
    lastAngle[2] += k[0] * Y[2]
    biask[0] += k[1] * Y[0]
    biask[1] += k[1] * Y[1]
    biask[2] += k[1] * Y[2]
    Pk[0][0] -= k[0] * Pk[0][0]
    Pk[0][1] -= k[0] * Pk[0][1]
    Pk[1][0] -= k[1] * Pk[0][0]
    Pk[1][1] -= k[1] * Pk[0][1]

    return (lastAngle, Pk, biask)

# Sensor constants
qAngle = 0.01
qGyro = 0.0003
rAngle = 0.03

# Bias and P initial values
bias = [0, 0, 0]
P = [[0, 0], [0, 0]]

# Time interval between measurements
dt = 0.18

# Get data
with open('imuData', 'rb') as f:
    dataMatrix = pickle.load(f)

acc = dataMatrix[1:4]
gyro = dataMatrix[4:7]

filteredMatrix = []
initialAngle = []
for j in range(3):
    filteredMatrix.append([])
    initialAngle.append([])

filteredAngle = [0, 0, 0]


for i in range(len(dataMatrix[0])):
    measuredAngle = []
    measuredRate = []
    measuredAngle.append(math.atan2(acc[1][i], acc[2][i]))
    measuredAngle.append(math.atan2(acc[2][i], acc[0][i]))
    measuredAngle.append(math.atan2(acc[0][i], acc[1][i]))
    measuredRate.append(gyro[0][i])
    measuredRate.append(gyro[1][i])
    measuredRate.append(gyro[2][i])
    for k in range(3):
        initialAngle[k].append(measuredAngle[k])
        if i==0:
            filteredAngle[k] = measuredAngle[k]
    filteredAngle, P, bias = kalmanCalculate(filteredAngle, measuredAngle, measuredRate, P, bias)
    for j, item in enumerate(filteredAngle):
        filteredMatrix[j].append(item)

for i in range(3):
    for j in range(len(filteredMatrix[0])):
        filteredMatrix[i][j] = math.degrees(filteredMatrix[i][j])
        initialAngle[i][j] = math.degrees(initialAngle[i][j])

# plt.plot(filteredMatrix[0],'bs-', initialAngle[0], 'b*-')
# plt.plot(filteredMatrix[1],'rs-', initialAngle[1], 'r*-')
# plt.plot(filteredMatrix[2],'gs-', initialAngle[2], 'g*-')
plt.plot(dataMatrix[7],'bs-')
plt.plot(dataMatrix[8],'rs-')
plt.plot(dataMatrix[9],'gs-')

plt.show()


