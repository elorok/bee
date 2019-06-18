#!/usr/bin/python
from slave.module_button import Button
from slave.module_proximity import Proximity


bttn = Button()
bttn.sync()

prox = Proximity()
prox.sync()