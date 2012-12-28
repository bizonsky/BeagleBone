from smbus import SMBus
from bitstring import BitArray
import math

#--------------------------------

L3GADDR = 0x6B
CTREG1 = 0x20
CTREG4 = 0x23
#------------
ON = 0x0F
DPS250 = 0x00	# dps: 250 (Default)
DPS500 = 0x10	# dps: 500
DPS2000 = 0x20	# dps: 2000
#------------
XOUTLOW = 0x28
XOUTHIGH = 0x29
YOUTLOW = 0x2A
YOUTHIGH = 0x2B
ZOUTLOW = 0x2C
ZOUTHIGH = 0x2D

RAD = math.pi/180.0

#--------------------------------

def setup_bus(x):
	bus = SMBus(x)		# x indicates /dev/i2c-x
	return bus

#--------------------------------

def setup_gyro(bus,SCALE):
	bus.write_byte_data(L3GADDR,CTREG1,ON)
	bus.write_byte_data(L3GADDR,CTREG4,SCALE)
	#
	if(SCALE == DPS250):
		S = 250.0/32768.0
	if(SCALE == DPS500):
		S = 500.0/32768.0
	if(SCALE == DPS2000):
		S = 2000.0/32768.0
	#
	return S

#--------------------------------

def get_gyro(bus,S):
	wx = 256*bus.read_byte_data(L3GADDR,XOUTHIGH)+bus.read_byte_data(L3GADDR,XOUTLOW)
	if(wx >= 32768 ):
		wx = BitArray(bin(wx)).int

	wy = 256*bus.read_byte_data(L3GADDR,YOUTHIGH)+bus.read_byte_data(L3GADDR,YOUTLOW)
	if(wy >= 32768 ):
		wy = BitArray(bin(wy)).int

	wz = 256*bus.read_byte_data(L3GADDR,ZOUTHIGH)+bus.read_byte_data(L3GADDR,ZOUTLOW)
	if(wz >= 32768 ):
		wz = BitArray(bin(wz)).int

	return [S*wx,S*wy,S*wz,RAD*S*wx,RAD*S*wy,RAD*S*wz]
