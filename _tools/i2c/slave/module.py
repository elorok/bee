class Module:
	def __init__(self, name):
		self.name = name

	def sync(self):
		print("Ich bin vererbt")

	def __len__(self):
		return len(self.name)