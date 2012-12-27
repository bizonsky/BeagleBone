from smbus import SMBus

MCPADDR = 0x62
WRITEDACFASTMODE = 0x00

#--------------------------------

def setup_bus(x):
	bus = SMBus(x)	 # x indicates /dev/i2c-x
	return bus

#--------------------------------

def dac(bus,x):
	data = [(x >> 8) & 0x0F,x & 0xFF]
	bus.write_byte_data(MCPADDR,WRITEDACFASTMODE|data[0],data[1])	
	return

