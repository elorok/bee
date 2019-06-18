#!/usr/bin/python
from slave.module_button import Button
from slave.module_proximity import Proximity
from slave.module_led import Led


bttn = Button()
bttn.sync()

prox = Proximity()
prox.sync()

led = Led()
led.sync()