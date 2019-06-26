import smbus
import sys
from .module import Module

class Button(Module):
		def __init__(self):
			super().__init__()
			super().setAddress(10)


		def sync(self):
			try: 
				msg = smbus.i2c_msg(); 
				msg.read(super().getAddress(), 1);
				i2c = smbus.SMBus(1)
				i2c.i2c_rdwr(msg);
				#state = i2c.read_byte(super().getAddress())

			except IOError:
				super().setOnline(False)
				super().setSetup(False)
				return

			file = open("/tmp/i2c_" + str(super().getAddress()) + "_in", "w")
			file.write(str(state))
			file.close()
