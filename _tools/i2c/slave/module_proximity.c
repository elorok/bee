/**
 * I2C Module Proximity
 *
 * @Autor: Stefan Lagger
 * @Version: 1.0
 * ******************************
 * Date		Vers.	Name			Comment / Change
 * 12.06.19 1.0		Stefan Lagger	First Edition
 */

 // *** INCLUDES ***
#include <stdlib.h>
#include <stdio.h>
#include "module_proximity.h"
#include "../i2c_readCommandBuffer.h"


// *** DEFINES ***
#define I2C_ADDR	81
#define DATA_SIZE	4

/**
 * Scan Devices
 */
void module_proximity_init(void) {
	i2c_device[I2C_ADDR].init = module_proximity_init;
	i2c_device[I2C_ADDR].dataSync = module_proximity_dataSync;
}

/**
 * Sync Data
 */
void module_proximity_dataSync(void) {
	unsigned char data[DATA_SIZE];
	i2c_readCommandBuffer(I2C_ADDR, 0, data, DATA_SIZE);
	for(unsigned int i = 0; i <= DATA_SIZE -1; i++)
		printf("Proximity: %i\n", data[i]);


	FILE *fp;

	// Open File
	fp = fopen("/tmp/i2c/81", "w+");


	// Write to File
	if (fp != NULL) {
		for(unsigned int i = 0; i <= DATA_SIZE -1; i++)
			fprintf(fp, "%i\n", data[i]);
	}

	// Close File
	fclose(fp);
}