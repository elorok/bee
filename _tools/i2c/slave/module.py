class Module:
	online = False
	setup = False

	
	def __init__(self):
		pass


	def setup(self):
		pass


	def setSetup(self, val):
		self.setup = val

	def getSetup(self):
		return self.setup

	def setOnline(self, val):
		self.online = val
		
	def getOnline(self):
		return self.online