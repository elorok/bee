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
		self.__address = val

	def getAddress(self): 
		return self.__address

	def setSetup(self, val):
		self.__setup = val

	def getSetup(self):
		return self.__setup

	def setOnline(self, val):
		self.__online = val
		
	def getOnline(self):
		return self.__online