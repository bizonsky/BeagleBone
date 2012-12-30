from time import sleep
from termcolor import colored
import math

B = 3950.0
T0 = 298.15
R0 = 10.0

#-------------------------

def delay(x):
	sleep(x*1e-3)
	return

#-------------------------

def analogRead():
	f = open("/sys/devices/platform/omap/tsc/ain1","r")
	data = f.read()
	input = data.split('\x00')
	ain0 = int(input[0])
	f.close
	return ain0

#-------------------------

def measure():
	R = 0.0
	T = 0.0
	for i in range(0,50):
		r = R0/(4095.0/analogRead() - 1.0)
		R += r
		T += 1/(1/T0 + math.log(r/R0)/B)
		delay(10)
	#
	R = R/50
	T = T/50 - 273.15
	return [R,T]

#-------------------------
