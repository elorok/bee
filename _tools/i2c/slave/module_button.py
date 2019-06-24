import smbus
import sys
from .module import Module

class Button(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(10)
			super().setSetup(True)


		def checkOnline(self):
			super().checkOnline(super().getAddress())


		def sync(self):
			try: 
				i2c = smbus.SMBus(1)
				result = i2c.read_byte(super().getAddress())

			except IOError:
				setOnline(False)
				setSetup(False)
				return

			file = open("/tmp/i2c_" + str(super().getAddress()), "w")
			file.write(str(result))
			file.close()
