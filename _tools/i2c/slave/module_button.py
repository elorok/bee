#!/usr/bin/python
import smbus
import sys

i2c = smbus.SMBus(1)

def init():
	print("Init Button Done");
