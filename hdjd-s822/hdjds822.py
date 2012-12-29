from time import sleep
from termcolor import colored

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
	#
	f = open("/sys/devices/platform/omap/tsc/ain2","r")
	data = f.read()
	input = data.split('\x00')
	ain1 = int(input[0])
	#
	f = open("/sys/devices/platform/omap/tsc/ain3","r")
	data = f.read()
	input = data.split('\x00')
	ain2 = int(input[0])
	#
	f.close
	return [ain0,ain1,ain2]

#-------------------------

def get_color():
	COLOR = analogRead()
	RED = 11*(1.8/4095.0)*(8.24/3.0)*COLOR[0] 	 	#see plots from the datasheet
	GREEN = 11*(1.8/4095.0)*(10.98/3.0)*COLOR[1]
	BLUE = 11*(1.8/4095.0)*(14.61/3.0)*COLOR[2]
	#
	if (RED > 8.24):
		RED = 0.0
		print colored('Red : Out of range!','cyan')
	if (GREEN > 10.98):
		GREEN = 0.0
		print colored('Green : Out of range!','cyan')
	if (BLUE > 14.61):
		BLUE = 0.0
		print colored('Blue : Out of range!','cyan')
	#		
	return [RED,GREEN,BLUE]
	
#-------------------------
