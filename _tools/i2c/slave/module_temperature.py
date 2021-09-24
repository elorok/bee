from smbus2 import SMBus, i2c_msg
import sys
from .module import Module

class Temperature(Module):
		_dig_T1 = 0
		_dig_T2 = 0
		_dig_T3 = 0
		_dig_P1 = 0
		_dig_P2 = 0
		_dig_P3 = 0
		_dig_P4 = 0
		_dig_P5 = 0
		_dig_P6 = 0
		_dig_P7 = 0
		_dig_P8 = 0
		_dig_P9 = 0
		_dig_H1 = 0
		_dig_H2 = 0
		_dig_H3 = 0
		_dig_H4 = 0
		_dig_H5 = 0
		_dig_H6 = 0
		_temp = 0
		_hum = 0
		_pres = 0

		def __init__(self, addr):
			super().__init__()
			super().setAddress(addr)

		@staticmethod
		def __toSigned(v, n):
			if(v >= (2**n / 2)):
				v = 0-2**n + v
			return v


		def setup(self):
			try:
				with SMBus(1) as bus:
					bus.write_byte_data(super().getAddress(), 224, 182)	# Resets sensor
					bus.write_byte_data(super().getAddress(), 245, 0)	# filter, interface, tStandby
					bus.write_byte_data(super().getAddress(), 242, 1)	# Sets hum oversampling
					bus.write_byte_data(super().getAddress(), 244, 39)	# Sets press and temp oversampling and mode

					_calib_data = bus.read_i2c_block_data(super().getAddress(), 136, 26)

					self._dig_T1 = _calib_data[0] + (_calib_data[1]<<8)
					self._dig_T2 = Temperature.__toSigned(_calib_data[2] + (_calib_data[3]<<8), 16)
					self._dig_T3 = Temperature.__toSigned(_calib_data[4] + (_calib_data[5]<<8), 16)
					self._dig_P1 = _calib_data[6] + (_calib_data[7]<<8)
					self._dig_P2 = Temperature.__toSigned(_calib_data[8] + (_calib_data[9]<<8), 16)
					self._dig_P3 = Temperature.__toSigned(_calib_data[10] + (_calib_data[11]<<8), 16)
					self._dig_P4 = Temperature.__toSigned(_calib_data[12] + (_calib_data[13]<<8), 16)
					self._dig_P5 = Temperature.__toSigned(_calib_data[14] + (_calib_data[15]<<8), 16)
					self._dig_P6 = Temperature.__toSigned(_calib_data[16] + (_calib_data[17]<<8), 16)
					self._dig_P7 = Temperature.__toSigned(_calib_data[18] + (_calib_data[19]<<8), 16)
					self._dig_P8 = Temperature.__toSigned(_calib_data[20] + (_calib_data[21]<<8), 16)
					self._dig_P9 = Temperature.__toSigned(_calib_data[22] + (_calib_data[23]<<8), 16)
					self._dig_H1 = _calib_data[25]

					_calib_data = bus.read_i2c_block_data(super().getAddress(), 225, 7)

					self._dig_H2 = Temperature.__toSigned(_calib_data[0] + (_calib_data[1]<<8), 16)
					self._dig_H3 = _calib_data[2]
					self._dig_H4 = Temperature.__toSigned((_calib_data[3]<<4) + (_calib_data[4] & 0xf), 12)
					self._dig_H5 = Temperature.__toSigned((_calib_data[4]>>4) + (_calib_data[5]<<4), 12)
					self._dig_H6 = Temperature.__toSigned(_calib_data[6], 8)


					super().setSetup(True)
			except:
				super().setSetup(False)
				raise


		def sync(self):
			try:
				with SMBus(1) as bus:
					# Temperature
					adc_t_l = bus.read_i2c_block_data(super().getAddress(), 250, 3)
					adc_t = (adc_t_l[0]<<12) + (adc_t_l[1]<<4) + (adc_t_l[2]>>4)
					var1 = ((adc_t / 16384.0) - (self._dig_T1 / 1024.0)) * (self._dig_T2)
					var2 = (adc_t / 131072.0) - (self._dig_T1/8192.0) * (((adc_t/131072.0) - (self._dig_T1/8192.0)) * (self._dig_T3))
					t_fine = var1 + var2
					self._temp = t_fine / 5120.0

					# Humidity
					adc_h_l = bus.read_i2c_block_data(super().getAddress(), 253, 2)
					adc_h = (adc_h_l[0]<<8) + adc_h_l[1]
					hum = t_fine - 76800.0
					hum = (adc_h - (self._dig_H4 * 64.0 + self._dig_H5 / 16384.0 * hum)) * (self._dig_H2 / 65536.0 * (1.0 + self._dig_H6 / 67108864.0 * hum * (1.0 + self._dig_H3 / 67108864.0 * hum)))
					hum = hum * (1.0 - self._dig_H1 * hum / 524288.0)
					if(hum > 100.0):
						hum = 100.0
					elif(hum < 0.0):
						hum = 0.0
					self._hum = hum

					# Pressure
					adc_p_l = bus.read_i2c_block_data(super().getAddress(), 247, 3)
					adc_p = (adc_p_l[0]<<12) + (adc_p_l[1]<<4) + (adc_p_l[2]>>4)
					var1 = (t_fine / 2.0) - 64000.0
					var2 = var1 * var1 * self._dig_P6 / 32768.0
					var2 = var2 + var1 * self._dig_P5 * 2.0
					var2 = (var2 / 4.0) + (self._dig_P4 * 65536.0)
					var1 = (self._dig_P3 * var1 * var1 / 524288.0 + self._dig_P2 * var1) / 524288.0
					var1 = (1.0 + var1 / 32768.0) * self._dig_P1
					if(var1 == 0.0):
						self._pres = 0.0
					else:
						pres = 1048576.0 - adc_p
						pres = (pres - (var2 / 4096.0)) * 6250.0 / var1
						var1 = self._dig_P9 * pres * pres / 2147483648.0
						var2 = pres * self._dig_P8 / 32768.0
						self._pres = pres + (var1 + var2 + self._dig_P7) / 16.0


			except IOError:
				super().setOnline(False)
				super().setSetup(False)
				return


			file = open("/tmp/i2c_" + str(super().getAddress()) + "_in", "w")
			file.write(str(self._temp) + "\n" + str(self._hum) + "\n" + str(self._pres))
			file.close()
