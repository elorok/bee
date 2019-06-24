import smbus
import sys
from .module import Module

class Button(Module):
		__ADDR = 10


		def __init__(self):
			super().__init__()
			super().setSetup(True)


		def checkOnline(self):
			super().checkOnline(__ADDR)


		def sync(self):
			try: 
				i2c = smbus.SMBus(1)
				result = i2c.read_byte(__ADDR)

			except IOError:
				setOnline(False)
				setSetup(False)
				return

			file = open("/tmp/i2c_" + str(__ADDR), "w")
			file.write(str(result))
			file.close()
