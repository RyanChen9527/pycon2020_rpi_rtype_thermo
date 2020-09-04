import board
import busio
import digitalio
import adafruit_max31856
import time
 
# create a spi object
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
 
# allocate a CS pin and set the direction
cs = digitalio.DigitalInOut(board.D7)
cs.direction = digitalio.Direction.OUTPUT
 
# create a thermocouple object with the above
thermocouple = adafruit_max31856.MAX31856(spi, cs)
 
# print the temperature!
while True:
	print("temprature=>",int(thermocouple.temperature))
	time.sleep(1)
