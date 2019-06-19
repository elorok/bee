import smbus
import sys
from module import Module

class Proximity(Module):
		def __init__(self):
			self.ADDR = 81
			i2c = smbus.SMBus(1)
			i2c.write_word_data(self.ADDR, 0, 0)	# Enable Ambilight Sensor
			i2c.write_word_data(self.ADDR, 3, 2250)	# Setup Proximity Sensor
			i2c.write_word_data(self.ADDR, 4, 1888) #


		def sync(self):
			try:
				i2c = smbus.SMBus(1)
				proxy = i2c.read_word_data(self.ADDR, 8)
				ambi = i2c.read_word_data(self.ADDR, 9)

			except IOError:
				print("No Communication with I2C Slave " + str(self.ADDR) + ".")
				return


			file = open("/tmp/i2c_" + str(self.ADDR), "w")
			file.write(str(proxy) + "\n" + str(ambi))
			file.close()