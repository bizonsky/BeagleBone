"""

This is based from Adafruit: http://learn.adafruit.com/thermistor

Analog input : P9.39

"""


from termcolor import colored
from thermistor import measure , delay
from plots import setup_plot

#-------------------------

print colored('Press CTRL+C to stop','green')
print colored('     Thermistor  ...','green')
delay(1000)

#-------------------------

while(True):
	data = measure()
	""" Plot (maximize the window): temperature,  0 -> 20 (try to change this numbers) , label : 'T' unit: '*C' """
	setup_plot(data[1],0,20,'T','*C')
