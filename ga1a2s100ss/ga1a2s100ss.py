#             100Kohms           100Kohms 
#  GND  ------\/\/\/\------------\/\/\/\------ I0 (GA1A2S100SS)
#                          |
#                          |
#                          |
#                       P9_39 (AIN0) 
#
# and 3.3 V to +Vcc (GA1A2S100S)

from termcolor import colored
from analogRead import analogRead , delay

#-------------------------

print "setup: GA1A2S100SS ..."
print "Press CTRL+C to stop"
delay(1000)

while(True):
	try:
	#
		analog = analogRead(0)
		#
		print colored('------------------------------------------','green')
		i =(18.0/4096.0)*analog 		# 2xR = 100000 ohms and [i]=microA
		lx = 10.0 + 2.0*(i - 5.0)		# datasheet's plot :  GA1A2S100SS
		if (10 <= lx <= 10000):
			print colored('Illuminance: {0:.3f} lx  ->  {1:.3f} microA','cyan',attrs=['bold']) .format(lx,i)
		else:
			print colored('Out of range !','red',attrs=['bold'])		
		#
		delay(1000)
	#
	except KeyboardInterrrupt:
		break
