# P9_19 --->  SCL (TSL2561)
# P9_20 --->  SDA (TSL2561)

from time import sleep
from termcolor import colored
from smbus import SMBus

#--------------------------------
lux = 0.0
TSLADDR = 0x39
ONADDR = 0x80|0x00
ON = 0x03
TIME =  0x80|0x01
CH0LOW = 0x80|0x20|0x0C
CH0HIGH = 0x80|0x20|0x0D
CH1LOW = 0x80|0x20|0x0E
CH1HIGH = 0x80|0x20|0x0F
T1 = 0x00  # 13.7ms, scale 0.034
T2 = 0x01  # 101ms, scale 0.252
T3 = 0x02  # 402ms, scale 1.0 
#--------------------------------

print colored('Press CTRL+C to stop','red')
print colored('setup: tsl2561 ....','red')
sleep(1.0)

# 3 indicates /dev/i2c-3
bus = SMBus(3)  
# turn on tsl2561  --> 0x03
bus.write_byte_data(TSLADDR,ONADDR,ON) 
#integration time : 402 ms
bus.write_byte_data(TSLADDR,TIME,T3) 

#--------------------------------
while(True):
	print colored('-------------------------','cyan')
	ch00 = bus.read_i2c_block_data(TSLADDR,CH0LOW)
	ch01 = bus.read_i2c_block_data(TSLADDR,CH1LOW)
	ch0 = (int(ch00[0])+256*int(ch00[1]))/2
	ch1 = (int(ch01[0])+int(256*ch01[1]))/2

	print colored('IR: {0}','red') .format(ch1)
	print colored('Visible: {0}','red') .format(ch0-ch1)
	print colored('Full: {0}','red') .format(ch0)	
	#--------------------------------
	r =float(ch1)/float(ch0)
	print colored('CH1/CH0: {0}','red') .format(r)	
	if (0<r<=0.52): 
		lux = 0.0315*ch0-0.0593*ch0*r**1.4
	if (0.52<r<=0.65): 
		lux = 0.0229*ch0-0.0291*ch1
	if (0.65<r<=0.8): 
		lux = 0.0157*ch0-0.0180*ch1
	if (0.8<r<=1.3): 
		lux = 0.00338*ch0-0.00260*ch1
	if (r>1.3): 
		lux = 0.0
	#--------------------------------
	print colored('Lux: {0}','red') .format(lux)
	sleep(1.0)
