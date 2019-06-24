#!/usr/bin/python
from time import sleep
from slave.module_button import Button
from slave.module_proximity import Proximity
from slave.module_led import Led
from slave.module import Module


modules = []
modules.append(Button())
modules.append(Proximity())
modules.append(Led())

while(True):
	for module in modules:
		# Module is offline
		if not module.getOnline():
			module.checkOnline()
			module.setInit(False)

		# Module is not initialized
		if module.getOnline() and not module.getInit():
			try:
				module.init()
			except: 
				pass

		# Module is ready
		if module.getOnline() and module.getInit():
			print(str(module) + " is ready to sync.")

		sleep(0.1)	# 100ms