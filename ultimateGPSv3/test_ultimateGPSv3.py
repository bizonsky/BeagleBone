""" 	1. P9_24 (UART1_TXD) --> RX (GPS)
		   P9_26 (UART1_RXD) --> TX (GPS)

		2. intall: $sudo apt-get install gpsd gpsd-clients

		3. run (root):

		#echo 20 > /sys/kernel/debug/omap_mux/uart1_rxd
		#echo 0 > /sys/kernel/debug/omap_mux/uart1_txd
		$sudo gpsd /dev/tty01  (or #sudo gpsd /dev/tty01)

		4. to check: $cgps  (or $xgps only for Raspberry)

		5. $sudo python test_ultimateGPSv3.py
		
		"""

from gps import *
import os
from time import *

#------------

session = gps(mode=WATCH_ENABLE)

while(True):
	try:
	#------------
		os.system('clear')
		session.next()
		print '---------------'
		print '  GPS reading  '
		print '---------------'
		print 'latitude :  ' , session.fix.latitude
		print 'longitude : ' , session.fix.longitude
		print 'time utc :  ' , session.utc, session.fix.time
		print 'altitude :  ' , session.fix.altitude
		#print 'eph         ' , session.fix.eph
		print 'epv :       ' , session.fix.epv
		print 'ept :       ' , session.fix.ept
		print 'speed :     ' , session.fix.speed	
		print 'climb :     ' , session.fix.climb
	#------------
		print
		print ' Satellites (total of', len(session.satellites) , ' in view)'
		for i in session.satellites:
			print '\t', i
	#------------
		sleep(1)
	except (KeyboardInterrupt, SystemExit):
		break
print 
print 'GPS has terminated' 
session.close()
