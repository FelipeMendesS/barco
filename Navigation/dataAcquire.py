import serial
import time

ser = serial.Serial('/dev/cu.usbmodem1411',9600, timeout=2)
ser.flushInput()
print ser.inWaiting()

ser.readline()
ser.readline()
ser.readline()
c = []
a = ser.read(ser.inWaiting() or 1)
for i in range(120):
	time.sleep(0.1)
	a += ser.read(ser.inWaiting() or 1)
ser.close()
b = a.split("mamai")
for string in b:
	c.append(string.split("\r\n"))
for index, listing in enumerate(c):
	if len(listing) != 12:
		print index
print len(c)
