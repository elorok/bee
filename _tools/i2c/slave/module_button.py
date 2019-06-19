import smbus
import sys
from module import Module

class Button(Module):
		def __init__(self):
			self.ADDR = 10

		def sync(self):
			try: 
				i2c = smbus.SMBus(1)
				result = i2c.read_byte(self.ADDR)

			except IOError:
				print("No Communication with I2C Slave " + str(self.ADDR) + ".")
				return

			file = open("/tmp/i2c_" + str(self.ADDR), "w")
			file.write(str(result))
			file.close()
