/**
 * Scan I2C Devices
 *
 * @Autor: Stefan Lagger
 * @Version: 1.0
 * ******************************
 * Date		Vers.	Name			Comment / Change
 * 21.05.19 1.0		Stefan Lagger	First Edition
 */

#ifndef I2C_SCAN_H_
#define I2C_SCAN_H_

// GLOBAL VARIABLE
typedef struct {
	unsigned online : 1;		// 1= Slave is online
	void(*dataSync)(void);		// Read/Write Data
	void(*init)(void);			// Init Slave Device
} i2c_device_t;

i2c_device_t i2c_device[128];	// Address-Range 0..127

// FUNCTION PROTOTYPE
void i2c_scan(void);

#endif /* I2C_SCAN_H_ */