from smbus import SMBus

#--------------------------------

TSL_ADDR = 0x39
ON_ADDR = 0x80|0x00

ON = 0x03
OFF = 0x00

TSL_TIME =  0x80|0x01

CH0_LOW = 0x80|0x20|0x0C
CH0_HIGH = 0x80|0x20|0x0D
CH1_LOW = 0x80|0x20|0x0E
CH1_HIGH = 0x80|0x20|0x0F

#Gain: x1
GX1_T137 = 0b00000000	# 13.7ms, scale 0.034
GX1_T101 = 0b00000001	# 101ms, scale 0.252
GX1_T402 = 0b00000010	# 402ms, scale 1.0 

#Gain: x16
GX16_T137 = 0b00010000	# 13.7ms, scale 0.034
GX16_T101 = 0b00010001	# 101ms, scale 0.252
GX16_T402 = 0b00010010	# 402ms, scale 1.0 

#scale: 
SCALE_T137 = 0.034
SCALE_T101 = 0.252
SCALE_T402 = 1.0

#--------------------------------

def setup_bus(x):
	bus = SMBus(x)	# x indicates /dev/i2c-x
	return bus

#--------------------------------

def setup_tsl(bus,GAIN):
	bus.write_byte_data(TSL_ADDR,ON_ADDR,ON) 
	bus.write_byte_data(TSL_ADDR,TSL_TIME,GAIN)

	if (GAIN == GX1_T137):
		G = 1.0
		S = SCALE_T137
	if (GAIN == GX16_T137):
		G = 16.0
		S = SCALE_T137
	#
	if (GAIN == GX1_T101):
		G = 1.0
		S = SCALE_T101
	if (GAIN == GX16_T101):
		G = 16.0
		S = SCALE_T101
	#
	if (GAIN == GX1_T402):
		G = 1.0
		S = SCALE_T402
	if (GAIN == GX16_T402):
		G = 16.0
		S = SCALE_T402
	return [S,G]

#--------------------------------

def get_lux(bus,SCALE,GAIN):
	CH_0 = bus.read_i2c_block_data(TSL_ADDR,CH0_LOW)
	CH_1 = bus.read_i2c_block_data(TSL_ADDR,CH1_LOW)
	CH0 = (CH_0[0]+256*CH_0[1])/(SCALE*GAIN)
	CH1 = (CH_1[0]+256*CH_1[1])/(SCALE*GAIN)
	#
	r =CH1/CH0
	if (0<r<=0.52): 
		LUX = 0.0315*CH0-0.0593*CH0*r**1.4
	if (0.52<r<=0.65): 
		LUX = 0.0229*CH0-0.0291*CH1
	if (0.65<r<=0.8): 
		LUX = 0.0157*CH0-0.0180*CH1
	if (0.8<r<=1.3): 
		LUX = 0.00338*CH0-0.00260*CH1
	if (r>1.3): 
		LUX = 0.0
	#
	return [CH0,CH1,CH0-CH1,LUX]
