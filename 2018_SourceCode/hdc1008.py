import smbus
import time

#Get I2C bus
bus = smbus.SMBus(1)

#HDC1000 address, 0x42
bus.write_byte_data(0x40, 0x02, 0x42)
#bus.write_byte_data(0x40, 0x02, 0x42)
#Send temp measurement command
bus.write_byte(0x40, 0x00)
time.sleep(0.5)
while True:
#Read temp data
	data0 = bus.read_byte(0x40)
	data1 = bus.read_byte(0x40)

#Convert the data
	temp = (data0 * 256) + data1
	celsTemp = (temp / 65536.0)  * 165.0 - 40
	fahrTemp = celsTemp * 1.8 +32

#Send humidity measurement command
	bus.write_byte(0x40, 0x01)
	time.sleep(0.5)

#Read humidity data
	data0 = bus.read_byte(0x40)
	data1 = bus.read_byte(0x40)

#Convert the data
	humidity = (data0 * 256) + data1
	humidity = (humidity / 65536.0) * 100.0

#Output data

	print "Relative Humidity : %.2f percent" %humidity
	print "Temperature in Celsius : %.2f C" %celsTemp
	print "Temperature in Fahrenheit : %.2f F" %fahrTemp
	time.sleep(1.0)
