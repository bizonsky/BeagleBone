# P9_19 --->  SCL (L3GD20)
# P9_20 --->  SDA (L3GD20)

import l3gd20
from termcolor import colored
from time import sleep

print colored('Press CTRL+C to stop','green')
print colored('setup: l3gd20 ...','green')
sleep(1.0)

bus = l3gd20.setup_bus(3) 						# bus: 3 indicates /dev/i2c-3
S=l3gd20.setup_gyro(bus,l3gd20.DPS2000,2000.0)	# gyro scale +/- 2000.0 dps

while(True):
	W=l3gd20.get_gyro(bus,S)
	print colored('----------------------------------','cyan')	
	print colored('Wx = {0:.2f} dps =  {1:.2f} rad/s.','red') .format(W[0],W[3])
	print colored('Wy = {0:.2f} dps =  {1:.2f} rad/s.','red') .format(W[1],W[4])
	print colored('Wz = {0:.2f} dps =  {1:.2f} rad/s.','red') .format(W[2],W[5])
	sleep(0.5)
