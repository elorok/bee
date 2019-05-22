/**
 * Scan I2C Devices
 *
 * @Autor: Stefan Lagger
 * @Version: 1.0
 * ******************************
 * Date		Vers.	Name			Comment / Change
 * 21.05.19 1.0		Stefan Lagger	First Edition
 */

 // *** INCLUDES ***
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>
#include <stdlib.h>
#include <stdio.h>


/**
 * Scan Devices
 */
int i2c_scan(void) {
	int fp_i2c;
	
	// Open I2C Bus
	char *filename = (char*)"/dev/i2c-1";
	if ((fp_i2c = open(filename, O_RDWR)) < 0) {
		fprintf(stderr, "Failed to open the i2c bus.\n");
		return -1;
	}

	for (unsigned char address = 4; address <= 127; address++) {
		if (ioctl(fp_i2c, I2C_SLAVE, address) < 0) {
			fprintf(stderr, "Failed to address slave. Address: %i\n", address);
		}

		if (i2c_smbus_read_byte(fp_i2c) < 0) {
			printf("offline\n");
		}
		else {
			printf("online\n");
		}
	}

	return 0;
}