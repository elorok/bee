import smbus
import sys

class Led:
		def __init__(self):
			self.ADDR = 9

		def sync(self):
			i2c = smbus.SMBus(1)
			file = open("/tmp/i2c_" + str(self.ADDR), "r")
			red = file.readLine()
			green = file.readLine()
			blue = file.readLine()
			file.close()

			print(red + "\n" + green + "\n" + blue)