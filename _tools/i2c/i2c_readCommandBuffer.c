/**
 * Send Command and Read Buffer from I2C
 *
 * @Autor: Stefan Lagger
 * @Version: 1.0
 * ******************************
 * Date		Vers.	Name			Comment / Change
 * 18.06.19 1.0		Stefan Lagger	First Edition
 */

 // *** INCLUDES ***
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>
#include <stdlib.h>
#include <stdio.h>


/**
 * Receive Buffer
 * param address: I2C Slave address
 * param command: Command to I2C Slave
 * param buffer: Buffer for received data
 * param length: Number of Bytes to receive
 */
int i2c_readCommandBuffer(unsigned char address, unsigned char command, unsigned char *buffer, unsigned int length) {
	int fp_i2c;

	// Open I2C Bus
	char *filename = (char*)"/dev/i2c-1";
	if ((fp_i2c = open(filename, O_RDWR)) < 0) {
		fprintf(stderr, "Failed to open the i2c bus.\n");
		return -1;
	}

	if (ioctl(fp_i2c, I2C_SLAVE, address) < 0) {
		fprintf(stderr, "Failed to address slave.\n");
		return -2;
	}

	// Send Command
	i2c_smbus_read_byte_data(address, command, buffer, length);

	/*if (write(fp_i2c, &command, 1) != 1) {
		fprintf(stderr, "Failed to write to i2c bus.\n");
		return -3;
	}

	// Read Bytes
	if (read(fp_i2c, buffer, length) != length) {
		fprintf(stderr, "Failed to read from i2c bus.\n");
		return -4;
	}*/

	close(fp_i2c);

	return 0;
}