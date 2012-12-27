# P9_19 --->  SCL (MCP4725)
# P9_20 --->  SDA (MCP4725)

from  mcp4725 import setup_bus, dac
import math
from time import sleep
from termcolor import colored
from time import sleep

#--------------------------------

print colored('---------------------------','green')
print colored('Press CTRL+C to stop','red')
print colored('setup: mcp4725 -->  SQUARE ','red')
print colored('---------------------------','green')
sleep(0.5)

bus = setup_bus(3)
v=1024					 # v: 0 --> 4095

#--------------------------------
while(True):
	dac(bus,v)
	sleep(0.100)
	dac(bus,v/2)
	sleep(0.200)
	dac(bus,0)
	sleep(0.300)
		
