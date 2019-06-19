import smbus
import sys
from module import Module

class Led(Module):
		def __init__(self):
			self.ADDR = 9

		def sync(self):
			try:
				file = open("/tmp/i2c_" + str(self.ADDR), "r")
				red = int(file.readline())
				green = int(file.readline())
				blue = int(file.readline())
				file.close()

			except FileNotFoundError:
				print("File /tmp/i2c_" + str(self.ADDR) + " not found.")
				break

			i2c = smbus.SMBus(1)
			i2c.write_word_data(self.ADDR, red, (green + blue * 256))