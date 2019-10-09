import smbus
import sys
from .module import Module

class io(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(9)


		def sync(self):
			super().checkOnline()

			if(super().getOnline()):
				
			try: 
				i2c = smbus.SMBus(1)
				state = i2c.read_byte(super().getAddress())

			except IOError:
				super().setOnline(False)
				super().setSetup(False)
				return

				try:
					i2c = smbus.SMBus(1)
					i2c.write_word_data(super().getAddress(), red, (green + blue * 256))

				except IOError:
					super().setOnline(False)
					super().setSetup(False)