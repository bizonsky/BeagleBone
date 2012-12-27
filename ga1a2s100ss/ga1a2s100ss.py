#             100Kohms           100Kohms 
#  GND  ------\/\/\/\------------\/\/\/\------ I0 (GA1A2S100SS)
#                          |
#                          |
#                          |
#                       P9_39 (AIN0) 
#
# and 3.3 V to +Vcc (GA1A2S100S)

from time import sleep
from termcolor import colored

#-------------------------

def delay(x):	          # Create and assign function
	sleep(x*1e-3)
	return

#-------------------------

print "setup: GA1A2S100SS ..."
print "Press CTRL+C to stop"
sleep(1.0)

while(True):
	f = open("/sys/devices/platform/omap/tsc/ain1","r")
	data = f.read()
	input = data.split('\x00')
	analog = int(input[0])
	#
	print colored('------------------------------------------','green')
	i =(18.0/4096.0)*analog 		# 2xR = 100000 ohms and [i]=microA
	lx = 10.0 + 2.0*(i - 5.0)		# datasheet's plot :  GA1A2S100SS
	if (10 <= lx <= 10000):
		print colored('Illuminance: {0:.3f} lx  ->  {1:.3f} microA','cyan',attrs=['bold']) .format(lx,i)
	else:
		print colored('Out of range !','red',attrs=['bold'])		
	#
	f.close()
	delay(1000)
