from smbus2 import SMBus, i2c_msg
import sys
from .module import Module

class Led(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(9)


		def sync(self):
			super().checkOnline()

			if(super().getOnline()):
				try:
					with open("/tmp/i2c_" + str(super().getAddress()) + "_out", "r") as file:
						try:
							red = int(file.readline())
							green = int(file.readline())
							blue = int(file.readline())
						except ValueError:
							print("Invalid Values in File /tmp/i2c_" + str(super().getAddress()) + "_out")
							return
						file.close()

				except IOError:
					print("File /tmp/i2c_" + str(super().getAddress()) + "_out not found.")
					red = 0
					green = 0
					blue = 0

			
				try:
					with SMBus(1) as bus:
						bus.write_word_data(super().getAddress(), red, (green + blue * 256))

				except IOError:
					super().setOnline(False)
					super().setSetup(False)