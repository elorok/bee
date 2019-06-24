import smbus
import sys
from .module import Module

class Led(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(9)
			super().setSetup(True)

						
		def checkOnline(self):
			super().__checkOnline(super().getAddress())


		def sync(self):
			try:
				with open("/tmp/i2c_" + str(super().getAddress()), "r") as file:
					try:
						red = int(file.readline())
						green = int(file.readline())
						blue = int(file.readline())
					except ValueError:
						print("Invalid Values in File /tmp/i2c_" + str(super().getAddress()))
						red = 0
						green = 0
						blue = 0
					file.close()

			except IOError:
				print("File /tmp/i2c_" + str(super().getAddress()) + " not found.")
				red = 0
				green = 0
				blue = 0

			
			try:
				i2c = smbus.SMBus(1)
				i2c.write_word_data(super().getAddress(), red, (green + blue * 256))

			except IOError:
				setOnline(False)
				setSetup(False)