#            100Kohms (Trimmer) 
#  GND  ------\/\/\/\/\/\------ Vout (HIH-4000-200)
#       1          ^          3
#                  |             ----> You must set the trimmer !!!!! (Be careful)
#                  | 2                 So: pin 3 = 5.0 V  -->  pin 2 =1.8 V	 
#                  |
#              P9_39 (AIN0) 
#
# and 5.0 V to Vcc (HIH-4000-200)

from time import sleep
from termcolor import colored

#-------------------------

def delay(x):	          # Create and assign function
	sleep(x*1e-3)
	return

#-------------------------

print "setup: HIH-4000-200 ..."
print "Press CTRL+C to stop"
sleep(1.0)

while(True):
	f = open("/sys/devices/platform/omap/tsc/ain1","r")
	data = f.read()
	input = data.split('\x00')
	analog = int(input[0])
	#
	print colored('-------------------------------------','green')
	vol =(5170.0/1800.0)*(1800.0/4096.0)*analog  # my Beaglebone: 5.0V = 5.17 V
	hum = (vol-958)/30.680		# datasheet HIH-4000-002
	print colored('Humidity: {0:.3f} %RH  ->  {1:.3f} mV','cyan',attrs=['bold']) .format(hum,vol)
	#
	f.close()
	delay(1000)
