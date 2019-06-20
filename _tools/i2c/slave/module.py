class Module:
	online = False
	setup = False

	def __init__(self, name):
		self.name = name

	def __len__(self):
		return len(self.name)