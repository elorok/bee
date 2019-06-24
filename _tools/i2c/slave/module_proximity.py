import smbus
import sys
from .module import Module

class Proximity(Module):
		__ADDR = 81


		def setup(self):
			try:
				i2c = smbus.SMBus(1)
				i2c.write_word_data(__ADDR, 0, 0)		# Enable Ambilight Sensor
				i2c.write_word_data(__ADDR, 3, 2250)	# Setup Proximity Sensor
				i2c.write_word_data(__ADDR, 4, 1888)	#
				super().setSetup(True)
			except:
				super().setSetup(False)
				raise

				
		def checkOnline(self):
			super().__checkOnline(__ADDR)


		def sync(self):
			try:
				i2c = smbus.SMBus(1)
				proxy = i2c.read_word_data(__ADDR, 8)
				ambi = i2c.read_word_data(__ADDR, 9)

			except IOError:
				setOnline(False)
				setSetup(False)
				return


			file = open("/tmp/i2c_" + str(__ADDR), "w")
			file.write(str(proxy) + "\n" + str(ambi))
			file.close()