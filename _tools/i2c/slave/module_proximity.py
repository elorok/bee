import smbus
import sys
from .module import Module

class Proximity(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(81)


		def setup(self):
			try:
				i2c = smbus.SMBus(1)
				i2c.write_word_data(super().getAddress(), 0, 0)		# Enable Ambilight Sensor
				i2c.write_word_data(super().getAddress(), 3, 2250)	# Setup Proximity Sensor
				i2c.write_word_data(super().getAddress(), 4, 1888)	#
				super().setSetup(True)
			except:
				super().setSetup(False)
				raise

				
		def checkOnline(self):
			super().__checkOnline(super().getAddress())


		def sync(self):
			try:
				i2c = smbus.SMBus(1)
				proxy = i2c.read_word_data(super().getAddress(), 8)
				ambi = i2c.read_word_data(super().getAddress(), 9)

			except IOError:
				setOnline(False)
				setSetup(False)
				return


			file = open("/tmp/i2c_" + str(super().getAddress()), "w")
			file.write(str(proxy) + "\n" + str(ambi))
			file.close()