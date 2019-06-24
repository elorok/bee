import smbus

class Module:
	def __init__(self):
		self.setOnline(False)
		self.setSetup(False)

	def setup(self):
		self.setSetup(True)

	def checkOnline(self, addr):
		try:
			i2c = smbus.SMBus(1)
			result = i2c.read_byte(addr)
			self.setOnline(True)
		except:
			self.setOnline(False)
			self.setSetup(False)
			pass

	def setAddress(self, val):
		self.address = val

	def getAddress(self): 
		return self.address

	def setSetup(self, val):
		self.setup = val

	def getSetup(self):
		return self.setup

	def setOnline(self, val):
		self.online = val
		
	def getOnline(self):
		return self.online