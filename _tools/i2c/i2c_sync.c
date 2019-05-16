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
#include "i2c_writeBuffer.h"
#include <stdio.h>


#define ADDR_LED	0x09

/**
 * Main-Routine
 */
void main(void) {
	unsigned char dataLED[3]; 
	dataLED[0] = 0xff; 
	dataLED[1] = 0x55;
	dataLED[2] = 0x21;


	i2c_writeBuffer(ADDR_LED, &dataLED, 3);
}

