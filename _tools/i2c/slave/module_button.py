import smbus
import sys
import 

class Button(Module):
		def __init__(self):
			self.ADDR = 10

		def sync(self):
			i2c = smbus.SMBus(1)
			result = i2c.read_byte(self.ADDR)

			file = open("/tmp/i2c_" + str(self.ADDR), "w")
			file.write(str(result))
			file.close()