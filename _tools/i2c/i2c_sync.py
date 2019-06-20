#!/usr/bin/python
from slave.module_button import Button
from slave.module_proximity import Proximity
from slave.module_led import Led
from slave.module import Module


modules = []
modules.append(Button())
modules.append(Proximity())
modules.append(Led())

for module in modules:
	try:
		module.setup()
	except:
		pass

	print(str(module) + "\nonline: " + str(module.getOnline()) + "\tsetup: " + str(module.getSetup()))

#bttn = Button()
#bttn.sync()

#prox = Proximity()
#try:
#	prox.setup()
#except: 
#	print("Cannot Setup Proximity")
#prox.sync()

#led = Led()
#led.sync()