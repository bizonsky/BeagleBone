"""
This is based from Adafruit: http://learn.adafruit.com/thermistor 

Analog input : P9.39

"""


from termcolor import colored
from thermistor import measure , delay

#-------------------------

print colored('Press CTRL+C to stop','green')
print colored('     Thermistor  ...','green')
delay(1000)

#-------------------------

while(True):
	data = measure()
	print colored('-------------------------','cyan')		
	print colored('Resistance : {0:.3f} Kohms ','red') .format(data[0])
	print colored('Temperature : {0:.3f} *C   ','red') .format(data[1])
	delay(200)
