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
#include "i2c_scan.h"
#include <stdio.h>


#define ADDR_LED	0x09

/**
 * Main-Routine
 */
void main(void) {
	i2c_scan();
}

