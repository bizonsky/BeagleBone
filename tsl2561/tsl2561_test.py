# P9_19 --->  SCL (TSL2561)
# P9_20 --->  SDA (TSL2561)

import tsl2561
from time import sleep
from termcolor import colored

#--------------------------------

print colored('Press CTRL+C to stop','red')
print colored('setup: tsl2561 ....','red')
sleep(1.0)

bus = tsl2561.setup_bus(3)
setup = tsl2561.setup_tsl(bus,tsl2561.GX1_T402)
#                                         ^
#         ________________________________|     
#        |
#        v
#Gain x1:
#GX1_T137	# 13.7ms, scale 0.034
#GX1_T101	# 101ms, scale 0.252
#GX1_T402	# 402ms, scale 1.0 
#Gain x16:
#GX16_T137	# 13.7ms, scale 0.034
#GX16_T101	# 101ms, scale 0.252
#GX16_T402	# 402ms, scale 1.0 

#--------------------------------
while(True):
	tsl = tsl2561.get_lux(bus,setup[0],setup[1])
	print colored('----------------------','cyan')
	print colored('Full: {0:.1f}','red') .format(tsl[0])
	print colored('IR: {0:.1f}','red') .format(tsl[1])
	print colored('Visible: {0:.1f}','red') .format(tsl[2])
	print colored('Illuminance: {0:.1f} Lux','red') .format(tsl[3])
	sleep(0.5)
