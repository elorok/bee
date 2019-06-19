import smbus
import sys
from module import Module

class Led(Module):
		def __init__(self):
			self.ADDR = 9

		def sync(self):
			try:
				with open("/tmp/i2c_" + str(self.ADDR), "r") as file:
					try:
						red = int(file.readline())
						green = int(file.readline())
						blue = int(file.readline())
					except ValueError:
						print("Invalid Values in File /tmp/i2c_" + str(self.ADDR))
						red = 0
						green = 0
						blue = 0
					file.close()

			except FileNotFoundError:
				print("File /tmp/i2c_" + str(self.ADDR) + " not found.")
				red = 0
				green = 0
				blue = 0


			i2c = smbus.SMBus(1)
			i2c.write_word_data(self.ADDR, red, (green + blue * 256))