from smbus2 import SMBus, i2c_msg
import sys
from .module import Module

class Button(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(10)


		def sync(self):
			try: 
				i2c = SMBus(1)
				state = i2c.read_byte(super().getAddress())

			except IOError:
				super().setOnline(False)
				super().setSetup(False)
				return

			file = open("/tmp/i2c_" + str(super().getAddress()) + "_in", "w")
			file.write(str(state))
			file.close()
