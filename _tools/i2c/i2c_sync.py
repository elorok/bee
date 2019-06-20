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
	# Module is offline
	if(not module.getOnline())
		module.setSetup(False)

	# Module is not initialized
	if(module.getOnline() and not module.getSetup())
		try:
			module.setup()
		except: 
			pass

	# Module is ready
	if(module.getOnline() and module.getSetup())
		print(str(module) + " is ready to sync.")


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