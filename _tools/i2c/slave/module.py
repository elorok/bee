import smbus

class Module:
	def __init__(self):
		self.setOnline(False)
		self.setSetup(False)

	def setup(self):
		self.setSetup(True)

	def checkOnline(self):
		try:
			i2c = smbus.SMBus(1)
			result = i2c.read_byte(self.getAddress())
			self.setOnline(True)
		except:
			self.setOnline(False)
			self.setSetup(False)
			file = open("/tmp/i2c_" + str(self.getAddress()), "w")
			file.write("<offline>")
			file.close()

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