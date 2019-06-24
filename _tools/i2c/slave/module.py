import smbus

class Module:
	def __init__(self):
		self.setOnline(False)
		self.setInit(False)

	def setup(self):
		self.setInit(True)

	def checkOnline(self, addr):
		try:
			i2c = smbus.SMBus(1)
			result = i2c.read_byte(addr)
			self.setOnline(True)
		except:
			self.setOnline(False)
			self.setInit(False)
			pass

	def setAddress(self, val):
		self.address = val

	def getAddress(self): 
		return self.address

	def setInit(self, val):
		self.init = val

	def getInit(self):
		return self.init

	def setOnline(self, val):
		self.online = val
		
	def getOnline(self):
		return self.online