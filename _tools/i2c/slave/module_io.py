import smbus
import sys
from .module import Module

class Io(Module):
    def __init__(self):
        super().__init__()
        super().setAddress(0x0b)

    def sync(self):     
        # READ FILE
        try:
            file = open("/tmp/i2c_" + str(super().getAddress()) + "_out", "r")

            try:
                output = int(file.read())
                if output < 0 or output > 15:
                    print("Invalid Values in File /tmp/i2c_" + str(super().getAddress()) + "_out")
                    return

            except ValueError:
                print("Invalid Values in File /tmp/i2c_" + str(super().getAddress()) + "_out")
                return

            file.close()

        except IOError:
            print("File /tmp/i2c_" + str(super().getAddress()) + "_out not found.")
            output = 0


        # I2C SYNCHRONISATION
        try:
            i2c = smbus.SMBus(1)
            state = i2c.read_word_data(super().getAddress(), output)           
            digital = (state // 256) % 16
            analog1 = state * 4
            analog2 = state // 32736
            analog = (analog1 + analog2) % 512

        except IOError:
            super().setOnline(False)
            super().setSetup(False)
            return


        # WRITE FILE        
        file = open("/tmp/i2c_" + str(super().getAddress()) + "_in", "w")
        file.write(str(analog) + "\n" + str(digital))        
        file.close()