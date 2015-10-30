import serial
import matplotlib.pyplot as plt

def is_float (s):
	try:
		number = float(s)
		return number
	except:
		print(s)
		return 0

T=[]
accx=[]
accy=[]
accz=[]
gyrox=[]
gyroy=[]
gyroz=[]
magx=[]
magy=[]
magz=[]

ser = serial.Serial('/dev/cu.usbmodem1411',9600)
count = 1
i = 1

while True:
	T.append(is_float(ser.readline()[:-1]))
	accx.append(is_float(ser.readline()[:-1]))
	accy.append(is_float(ser.readline()[:-1]))
	accy.append(is_float(ser.readline()[:-1]))
	gyrox.append(is_float(ser.readline()[:-1]))
	gyroy.append(is_float(ser.readline()[:-1]))
	gyroz.append(is_float(ser.readline()[:-1]))
	magx.append(is_float(ser.readline()[:-1]))
	magy.append(is_float(ser.readline()[:-1]))
	magz.append(is_float(ser.readline()[:-1]))
	# print(ser.readline()[:-1])
	i = i+1
	if i==1000:
		break
plt.plot(T)
plt.show()
