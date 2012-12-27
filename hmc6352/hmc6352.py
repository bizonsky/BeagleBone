# P9_19 --->  SCL (HMC6352)
# P9_20 --->  SDA (HMC6352)

# You must run first this line (like root):
#
# echo hmc6352 0x21 > /sys/class/i2c-adapter/i2c-3/new_device
#
# to check:
#
# dmesg | grep hmc

from time import sleep
from termcolor import colored

print "setup: HMC6352 ..."
print "Press CTRL+C to stop"
sleep(1.5)

while(True):
	f = open ("/sys/bus/i2c/drivers/hmc6352/3-0021/hmc6352/heading0_input","r")
	data=float(f.read())
	print colored ("-----------------",'red')
	data2 =360.0 - data

	if (data == 0): print colored('{0:.1f}*, N  --> N ','cyan') .format(data)
	if (0< data <90): print colored('{0:.1f}*, N  --> NE','cyan') .format(data)
	if (data == 90): print colored('{0:.1f}*, N  --> E','cyan') .format(data)
	if (90< data <180): print colored('{0:.1f}*, N  --> SE','cyan') .format(data)
	if (data == 180): print colored('{0:.1f}*, N  --> S','cyan') .format(data)
	if (180< data <270): print colored('{0:.1f}*, N  --> SW','cyan') .format(data2)
	if (data == 270): print colored('{0:.1f}*, N  --> W','cyan') .format(data2)
	if (270< data <360): print colored('{0:.1f}*, N  --> NW','cyan') .format(data2)
	if (data == 360): print colored('{0:.1f}*, N  --> N','cyan') .format(data2)
	sleep(1.0)
