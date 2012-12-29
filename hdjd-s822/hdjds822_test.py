"""

For each color:

	10K				100K
GND ------\/\/\/\-----------\/\/\/\------  VR, VG, VR --> (HDJD-S822)
			 |
			 |
			 |
			P9.39: RED
			P9.40: GREEN
			P9.37: BLUE

Vcc = 5.0 V (HDJD-S822)

MODE: GS10

I did not use the led, I get best result without the led. You can try it.

"""


from termcolor import colored
from hdjds822 import get_color , delay

#-------------------------

print colored('Press CTRL+C to stop','green')
print colored('setup: HDJD-S822 ...','green')
delay(1000)

#-------------------------

while(True):
	color = get_color()	
	print colored('----------------------','cyan')
	print colored('Red : {0:.3f} mW/cm^2','red') .format(color[0])
	print colored('Green : {0:.3f} mW/cm^2','green') .format(color[1])
	print colored('Blue : {0:.3f} mW/cm^2','blue') .format(color[2])
	delay(1000)
