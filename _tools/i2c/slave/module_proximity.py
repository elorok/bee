import smbus
import sys

class Proximity:
		def __init__(self):
			self.ADDR = 81

		def sync(self):
			i2c = smbus.SMBus(1)
			result = i2c.read_word_data(self.ADDR, 8)

			file = open("/tmp/i2c_" + str(self.ADDR), "w")
			file.write(str(result))
			file.close()