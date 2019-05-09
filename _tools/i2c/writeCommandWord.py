#!/usr/bin/python
import smbus
import sys

i2c = smbus.SMBus(1)

sys.stdout.write(str(i2c.read_word_data(int(sys.argv[1]),int(sys.argv[2])))