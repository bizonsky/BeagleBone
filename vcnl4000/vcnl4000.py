from smbus import SMBus
from time import sleep

#--------------------------------

VCNL_ADDR = 0x13
REG0 = 0x80
REG3 = 0x83
REG4 = 0x84
REG5_LIGHT_H = 0x85
REG6_LIGHT_L = 0x86
REG7_PROX_H = 0x87
REG8_PROX_L = 0x88
REG9 = 0x89

MEAS_L = 0b00010000
MEAS_P = 0b00001000
IR_3125 = 0x00		 # 3.125 MHz
IR_15625 = 0x01		 # 1.5625 MHz
IR_78125 = 0x02		 # 781.25 KHz :  default
IR_390625 = 0x03	 # 390.625 kHz

#--------------------------------

def setup_bus(x):
	bus = SMBus(x)	# x indicates /dev/i2c-x
	return bus

#--------------------------------

def setup_vcnl(bus,I_LED,IR_RANGE):
	# current set : 20 -->  200 mA   (I_LED * 10 mA). I_LED: 1 -> 20
	bus.write_byte_data(VCNL_ADDR,REG3,I_LED)
	# proximity measurement signal frecuency 
	bus.write_byte_data(VCNL_ADDR,REG9,IR_RANGE)
	return

#--------------------------------

def get_vcnl(bus):
	bus.write_byte_data(VCNL_ADDR,REG0,MEAS_P)
	sleep(0.05)
	prox = 256*bus.read_byte_data(VCNL_ADDR,REG7_PROX_H)+bus.read_byte_data(VCNL_ADDR,REG8_PROX_L)

	bus.write_byte_data(VCNL_ADDR,REG0,MEAS_L)
	sleep(0.2)
	lux = 256*bus.read_byte_data(VCNL_ADDR,REG5_LIGHT_H)+bus.read_byte_data(VCNL_ADDR,REG6_LIGHT_L)
	return [0.25*lux,prox] 
