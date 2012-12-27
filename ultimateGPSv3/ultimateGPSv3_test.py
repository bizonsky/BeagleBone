# 		P9_24 (UART1_TXD) --> RX (GPS)
# 		P9_26 (UART1_RXD) --> TX (GPS)

#		First run (root):
#
#		echo 20 > /sys/kernel/debug/omap_mux/uart1_rxd
#		echo 0 > /sys/kernel/debug/omap_mux/uart1_txd
#

import ultimateGPSv3
from time import sleep
from termcolor import colored

print colored('Ultimate GPS V3. setup ... ','green')
print colored('Get out: ctrl + c','green')
sleep(1.0)

ser = ultimateGPSv3.setup_gps()

while(True):
	ultimateGPSv3.get_gps(ser)
