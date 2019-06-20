import smbus
import sys
from .module import Module

class Button(Module):
		__ADDR = 10


		def __init__(self):
			super().setSetup()


		def sync(self):
			try: 
				i2c = smbus.SMBus(1)
				result = i2c.read_byte(__ADDR)

			except IOError:
				print("No Communication with I2C Slave " + str(__ADDR) + ".")
				return

			file = open("/tmp/i2c_" + str(__ADDR), "w")
			file.write(str(result))
			file.close()
