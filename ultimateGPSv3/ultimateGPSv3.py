import serial
from termcolor import colored

#------------

def setup_gps():
	ser = serial.Serial(
        port='/dev/ttyO1',
        baudrate=9600,
        timeout=1,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS
	) 
	return ser

#------------

def get_gps(x):
	list = x.readline()
	if (list[4]=='M' and list[5]=='C' and list[18]=='A'):
		#--------------------------
		hor = 10*int(list[7])+int(list[8])
		min = 10*int(list[9])+int(list[10])
		sec = 10*int(list[11])+int(list[12])	
		#--------------------------
		long1 =10*int(list[20]) + int(list[21])
		long2 =10*int(list[22]) + int(list[23])+0.1*int(list[25])+0.01*int(list[26])+0.001*int(list[27])+0.0001*int(list[28])
		long3 = list[30]
		#--------------------------
		lati1 =100*int(list[32])+10*int(list[33]) + int(list[34])
		lati2 =10*int(list[35]) + int(list[36])+0.1*int(list[38])+0.01*int(list[39])+0.001*int(list[40])+0.0001*int(list[41])
		lati3 = list[43]
		#--------------------------
		vel = int(list[45])+0.1*int(list[47])+0.01*int(list[48])
		#--------------------------
		print colored('------------------------','green')
		print colored('Time: {0}:{1}:{2} GMT','cyan',attrs=['bold']) .format(hor,min,sec)
		print colored('Longitude: {0}* {1} {2}','red',attrs=['bold']) .format(long1,long2,long3)
		print colored('Latitude: {0}* {1} {2}','red',attrs=['bold']) .format(lati1,lati2,lati3)
		print colored('Velocity: {0} Knots','red',attrs=['bold']) .format(vel)
	#--------------------------
	if (list[4]=='M' and list[5]=='C' and list[18]=='V'):
		print colored('No validity data from scan !','green')
	#--------------------------
	return
