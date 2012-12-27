# P9_19 --->  SCL (VCNL4000)
# P9_20 --->  SDA (VCNL4000)

import vcnl4000
from time import sleep
from termcolor import colored


print colored('Press CTRL+C to stop','green')
print colored('setup: vcnl4000  ...','green')
sleep(1.0)

bus = vcnl4000.setup_bus(3)		# bus: 3 indicates /dev/i2c-3
# setup: 390.625 KHz and I_LED = 20*10 mA = 200 mA
vcnl4000.setup_vcnl(bus,20,vcnl4000.IR_390625)

#--------------------------------

while(True):
	print colored('---------------------------','green')
	vcnl = vcnl4000.get_vcnl(bus)
	print colored('Ambient Light:  {0:.2f} lux ','red') .format(vcnl[0])
	print colored('Proximity:  {0} ','red') .format(vcnl[1])
		
