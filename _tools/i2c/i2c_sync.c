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
#include "i2c_scan.h"

// SLAVES
#include "slave/module_button.h"
#include "slave/module_proximity.h"

// GENERAL
#include <stdio.h>
#include <stdlib.h>


/**
 * Main-Routine
 */
void main(void) {
	module_button_init();
	module_proximity_init();


	i2c_scan();

	unsigned char buffer[127];

	for (unsigned char address = 4; address <= 127; address++) {
		if (i2c_device[address].online && i2c_device[address].dataSync != 0) {
			printf("%i\t", address);
			i2c_device[address].dataSync();
		}
	}*/
}
