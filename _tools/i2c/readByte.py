#!/usr/bin/python
import smbus
import sys

i2c = smbus.SMBus(1)

print(i2c.read_byte(int(sys.argv[1])))