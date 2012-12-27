# P9_19 --->  SCL (MCP4725)
# P9_20 --->  SDA (MCP4725)

from  mcp4725 import setup_bus, dac
import math
from time import sleep
from termcolor import colored

#--------------------------------

print colored('---------------------------','green')
print colored('Press CTRL+C to stop','red')
print colored('setup: mcp4725  ---->  SAW ','red')
print colored('---------------------------','green')
sleep(0.5)

bus = setup_bus(3)

#--------------------------------
while(True):
	v=512					 # v: 0 --> 4095
	for n in range(0,v):
		dac(bus,n)	
