/**
 * I2C Synchronizer
 * Read/Write Data from/to I2C Slaves. 
 * Synchroizes the Data from the Filesystem and I2C Slaves. 
 *
 * @Autor: Stefan Lagger
 * @Version: 1.0
 * ******************************
 * Date		Vers.	Name			Comment / Change
 * 15.05.19 1.0		Stefan Lagger	First Edition
 */

 // *** INCLUDES ***
// I2C
#include "i2c_writeBuffer.h"
#include "i2c_readBuffer.h"
#include "i2c_scan.h"

// SLAVES
#include "slave/module_button.h"

// GENERAL
#include <stdio.h>
#include <stdlib.h>


#define ADDR_LED	0x09

/**
 * Main-Routine
 */
void main(void) {
	i2c_device->init = module_button_init;
	i2c_device->dataSync = module_button_dataSync; 

	i2c_scan();

	unsigned char buffer[127];

	for (unsigned char address = 4; address <= 127; address++) {
		if (i2c_device[address].online) {
			printf("%i\t", address);
			i2c_device[address].dataSync();
		}
	}
}
