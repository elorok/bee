import smbus
import sys
from module import Module

class Led(Module):
		__ADDR = 9


		def __init__(self):
			self.setup = True


		def sync(self):
			try:
				with open("/tmp/i2c_" + str(__ADDR), "r") as file:
					try:
						red = int(file.readline())
						green = int(file.readline())
						blue = int(file.readline())
					except ValueError:
						print("Invalid Values in File /tmp/i2c_" + str(__ADDR))
						red = 0
						green = 0
						blue = 0
					file.close()

			except IOError:
				print("File /tmp/i2c_" + str(__ADDR) + " not found.")
				red = 0
				green = 0
				blue = 0

			
			try:
				i2c = smbus.SMBus(1)
				i2c.write_word_data(__ADDR, red, (green + blue * 256))

			except IOError:
				print("No Communication with I2C Slave " + str(__ADDR) + ".")