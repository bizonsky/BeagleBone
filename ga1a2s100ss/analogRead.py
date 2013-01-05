from time import sleep , time
startTime = time()

#-------------------------

def delay(x):
	sleep(x*1e-3)
	return

#-------------------------

def delayMS(x):
	sleep(x*1e-6)
	return

#-------------------------

def millis():
	t = time()-startTime
	return t

#-------------------------

def analogRead(ANALOG):
	if (ANALOG == 0):
		f = open("/sys/devices/platform/omap/tsc/ain1","r")
		data = f.read()
		input = data.split('\x00')
		ain = int(input[0])
	#
	if (ANALOG == 1):	
		f = open("/sys/devices/platform/omap/tsc/ain2","r")
		data = f.read()
		input = data.split('\x00')
		ain = int(input[0])
	#
	if (ANALOG == 2):	
		f = open("/sys/devices/platform/omap/tsc/ain3","r")
		data = f.read()
		input = data.split('\x00')
		ain = int(input[0])
	#
	if (ANALOG == 3):	
		f = open("/sys/devices/platform/omap/tsc/ain4","r")
		data = f.read()
		input = data.split('\x00')
		ain = int(input[0])
	#
	if (ANALOG == 4):	
		f = open("/sys/devices/platform/omap/tsc/ain5","r")
		data = f.read()
		input = data.split('\x00')
		ain = int(input[0])
	#
	if (ANALOG == 5):	
		f = open("/sys/devices/platform/omap/tsc/ain6","r")
		data = f.read()
		input = data.split('\x00')
		ain = int(input[0])
	#
	if (ANALOG == 6):	
		f = open("/sys/devices/platform/omap/tsc/ain7","r")
		data = f.read()
		input = data.split('\x00')
		ain = int(input[0])
	#
	f.close()
	return ain
