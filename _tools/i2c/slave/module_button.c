/**
 * I2C Module Button
 *
 * @Autor: Stefan Lagger
 * @Version: 1.0
 * ******************************
 * Date		Vers.	Name			Comment / Change
 * 22.05.19 1.0		Stefan Lagger	First Edition
 */

 // *** INCLUDES ***
#include <stdlib.h>
#include <stdio.h>
#include "module_button.h"
#include "../i2c_readBuffer.h"
#include "../i2c_scan.h"


// *** DEFINES ***
#define I2C_ADDR	10
#define DATA_SIZE	1

/**
 * Scan Devices
 */
void module_button_init(void) {
	
}

/**
 * Sync Data
 */
void module_button_dataSync(void) {
	unsigned char data;
	i2c_readBuffer(I2C_ADDR, data, 1);
	printf("Button: %i\n", data);
}