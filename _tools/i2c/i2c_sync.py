#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO
from slave.module_button import Button
from slave.module_proximity import Proximity
from slave.module_led import Led
from slave.module import Module


GPIO.setmode(GPIO.BCM)

modules = []
modules.append(Button())
modules.append(Proximity())
modules.append(Led())


while(True):
	GPIO.setmode(2, GPIO.IN)	# SDA
	GPIO.setmode(3, GPIO.IN)	# SCL

	print("SDA: " + str(GPIO.input(2) + " SCL: " + str(GPIO.input(3)))

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

		print("O: " + str(module.getOnline()) + " S: " + str(module.getSetup()) + " " + str(module))

	sleep(0.1)	# 100ms