from smbus2 import SMBus, i2c_msg
import sys
from .module import Module

class Proximity(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(81)


		def setup(self):
			try:
				with SMBus(1) as bus:
					bus.write_word_data(super().getAddress(), 0, 0)		# Enable Ambilight Sensor
					bus.write_word_data(super().getAddress(), 3, 2250)	# Setup Proximity Sensor
					bus.write_word_data(super().getAddress(), 4, 1888)	#
					super().setSetup(True)
			except:
				super().setSetup(False)
				raise


		def sync(self):
			try:
				with SMBus(1) as bus:
					proxy = bus.read_word_data(super().getAddress(), 8)
					ambi = bus.read_word_data(super().getAddress(), 9)

			except IOError:
				super().setOnline(False)
				super().setSetup(False)
				return


			file = open("/tmp/i2c_" + str(super().getAddress()) + "_in", "w")
			file.write(str(proxy) + "\n" + str(ambi))
			file.close()