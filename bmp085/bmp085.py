# P9_19 --->  SCL (BMP085)
# P9_20 --->  SDA (BMP085)

# You must run first this line (like root):
#
# echo bmp085 0x77 > /sys/class/i2c-adapter/i2c-3/new_device
#
# to check:
#
# dmesg | grep bmp

from time import sleep
from termcolor import colored

print "setup: BMP085 ..."
print "Press CTRL+C to stop"
sleep(1.0)

while(True):
	f = open ("/sys/bus/i2c/drivers/bmp085/3-0077/pressure0_input","r")
	pres=float(f.read())
	f = open ("/sys/bus/i2c/drivers/bmp085/3-0077/temp0_input","r")	
	temp=float(f.read())/10.0
	alti = 44330.0*(1-pow(pres/101325.0,1/5.255))
	print colored ("---------------------",'red')
	print colored('Temperature : {0:.1f} *C','cyan') .format(temp)
	print colored('Pressure : {0:.3f} KPa','cyan') .format(pres/1000)
	print colored('Altitude : {0:.3f} m','cyan') .format(alti)
	sleep(1.0)
