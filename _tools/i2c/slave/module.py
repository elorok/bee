import smbus

class Module:
	def __init__(self):
		self.online = False
		self.setup = False

	def setup(self):
		self.setup = True

	def checkOnline(self, addr):
		try:
			i2c = smbus.SMBus(1)
			result = i2c.read_byte(addr)
			module.setOnline(True)
		except:
			module.setOnline(False)
			module.setSetup(False)
			pass

	def setSetup(self, val):
		self.setup = val

	def getSetup(self):
		return self.setup

	def setOnline(self, val):
		self.online = val
		
	def getOnline(self):
		return self.online