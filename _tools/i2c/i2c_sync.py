#!/usr/bin/python
from slave.module_button import Button
from slave.module_proximity import Proximity
from slave.module_led import Led
from slave.module import Module


modules = Module(["a","b","c"])
print("laenge: " + str(len(modules)))

bttn = Button()
bttn.sync()

prox = Proximity()
try:
	prox.setup()
except: 
	print("Cannot Setup Proximity")
prox.sync()

led = Led()
led.sync()