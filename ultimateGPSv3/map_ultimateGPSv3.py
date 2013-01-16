""" 	1. P9_24 (UART1_TXD) --> RX (GPS)
		   P9_26 (UART1_RXD) --> TX (GPS)

		2. intall: $sudo apt-get install gpsd gpsd-clients

		3. download pygmaps.py: http://code.google.com/p/pygmaps/ 		

		4. run (root):

		#echo 20 > /sys/kernel/debug/omap_mux/uart1_rxd
		#echo 0 > /sys/kernel/debug/omap_mux/uart1_txd
		$sudo gpsd /dev/tty01  (or #sudo gpsd /dev/tty01)

		5. to check: $cgps  (or $xgps only for Raspberry)

		6. $sudo python map_ultimateGPSv3.py
		
		"""

from gps import *
from time import *
from pygmaps import *

#------------

path = []
session = gps(mode=WATCH_ENABLE)
report = session.next()
report = session.next()
report = session.next()
report = session.next()

lat = session.fix.latitude
lon = session.fix.longitude
mymap = maps(lat,lon,20)
mymap.addpoint(lat, lon, "#FF0000")


while(True):
	try:
	#------------
		report = session.next()
		lat = session.fix.latitude
		lon = session.fix.longitude
		alt = session.fix.altitude
		mymap = maps(lat,lon,20)
		path.append((lat,lon))
		print 'Lat:{0},  Lon:{1}, Alt:{2}' .format(lat,lon,alt)
	#------------
	except (KeyboardInterrupt, SystemExit):
		break
print 
print 'GPS has terminated' 
print 'MAP is  mymap.html' 
mymap.addpath(path,"#00FF00")
mymap.addpoint(lat, lon, "#0000FF")
mymap.draw('./mymap.html')
session.close()
