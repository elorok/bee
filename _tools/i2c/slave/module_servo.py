from smbus2 import SMBus, i2c_msg
import sys
from .module import Module

class Servo(Module):
	def __init__(self):
		super().__init__()
		super().setAddress(12)

	def sync(self):
		super().checkOnline()

		if(super().getOnline()):
			try:
				with open("/tmp/i2c_" + str(super().getAddress()) + "_out", "r") as file:
					try:
						servo0 = int(file.readline())
						servo1 = int(file.readline())
						servo2 = int(file.readline())
						servo3 = int(file.readline())
						servo4 = int(file.readline())
						servo5 = int(file.readline())
					except ValueError:
						print("Invalid Values in File /tmp/i2c_" + str(super().getAddress()) + "_out")
						return
					file.close()

			except IOError:
				print("File /tmp/i2c_" + str(super().getAddress()) + "_out not found.")
				servo0 = 0
				servo1 = 0
				servo2 = 0
				servo3 = 0
				servo4 = 0
				servo5 = 0


			try:
				with SMBus(1) as bus:
					bus.write_word_data(super().getAddress(), servo0, servo1)
					#msg = i2c_msg.write(super().getAddress(),[servo0,servo1,servo2,servo3,servo4,servo5])
					#bus.i2c_rdwr(msg)

			except IOError:
				super().setOnline(False)
				super().setSetup(False)
