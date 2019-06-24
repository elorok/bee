#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO
from slave.module_button import Button
from slave.module_proximity import Proximity
from slave.module_led import Led
from slave.module import Module


modules = []
modules.append(Button())
modules.append(Proximity())
modules.append(Led())

GPIO.setmode(GPIO.BCM)

while(True):

	print("SDA: " + str(GPIO.input(2)))
	print("SCL: " + str(GPIO.input(3)))

	for module in modules:
		# Module is offline
		if not module.getOnline():
			module.checkOnline()
			module.setSetup(False)

		# Module is not initialized
		if module.getOnline() and not module.getSetup():
			try:
				module.setup()
			except: 
				pass

		# Module is ready
		if module.getOnline() and module.getSetup():
			module.sync()


	sleep(0.1)	# 100ms