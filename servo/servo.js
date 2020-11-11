module.exports = function (RED) { "use strict";

	function ServoNode(config) {
		RED.nodes.createNode(this, config);

		var node = this;

	        node.on('input', function (msg) {
			var fs = require('fs');

			// *** Read State ***
			try {
				fs.readFile('/tmp/i2c_12_in', 'utf8', function (error, contents) {
					if (error == null) {
						if (contents != "<offline>") {
							node.status({ fill: "green", shape: "dot", text: "connected" });
						} else {
							node.status({ fill: "red", shape: "dot", text: "disconnected" });
						}
					} else {
						node.status({ fill: "red", shape: "dot", text: "disconnected" });
						node.error(stderr);
					}
				})
			} catch (error) {
				node.status({ fill: "red", shape: "dot", text: "disconnected" });
				node.error(error);
			}


		        // *** Write Data ***
			//count lines in file
			try {
				var fd_out;	//filedescripter i2c_12_out
				var isError = lockFile('/tmp/i2c_12_out.LOCKED', 1000, 10000);
				if(!isError){
					node.log("Error aufgetreten. isError: " + isError);
					throw isError;
				}
				var tokens = msg.payload.split(',');	//split Number of Servo and PWM-Value
				var numberServo = parseInt(tokens[0], 10);	//number 1...6
				var pwm = parseInt(tokens[1], 16);		//value 0...255

				//legal Number of Servo?
				if((numberServo >= 1)&&(numberServo <= 6))
				{
					var content_old;	//data from File
					var content_new = '';	//data for file
					var index = 0;		//for parsing
					var numberNewLines;	//number of new Lines
					var position = 1;	//linenumber
					var beginnWriteSpace = 0;	//here beginns the new Data
					var endWriteSpace;		//here ends the new Data

					//check (and repair) pwm-valiues
					if(pwm > 255) pwm = 255;
					if(pwm < 0) pwm = 0;

					//check if File exists, read/create content
					if(fs.existsSync('/tmp/i2c_12_out')){
						fd_out = fs.openSync('/tmp/i2c_12_out', 'r');
						content_old = fs.readFileSync('/tmp/i2c_12_out', 'utf8');
						fs.closeSync(fd_out);
					}
					else{
						content_old = '0\n0\n0\n0\n0\n0\n';
					}

					//get beginn/endWriteSpace
					while(position < numberServo){
						beginnWriteSpace = content_old.indexOf('\n', index);
							position += 1;
							index = beginnWriteSpace + 1;
					}
					if(numberServo != 1) beginnWriteSpace += 1;	//character after \n

					endWriteSpace = content_old.indexOf('\n', index);

					//write old part
					for(index = 0; index < beginnWriteSpace; index += 1){
						var c = content_old[index];
						content_new += c;
					}
					//write new Data
					content_new += pwm;

					//write rest of data
					position = numberServo;

					for(index = endWriteSpace; position <= 6; index += 1){
						var c = content_old[index];
							content_new += c;
							if(c == '\n'){
								 position += 1;
							}
					}

					//write to file
					fd_out = fs.openSync('/tmp/i2c_12_out', 'w');
					fs.writeSync(fd_out, content_new);
					fs.closeSync(fd_out);
					var error = unlockingFile('/tmp/i2c_12_out.LOCKED');
					if (error) throw error;
				}
			} catch (error){
				node.error(error);
		       	}
		});
	}
	RED.nodes.registerType("servo", ServoNode);

	//***functions***

	/**
	* create a lockfile
	* @param:	file		adress of lockfile ('/folder/file.lock)
	* @param:	pollPeriod	intervall in [ms]
	* @param:	maxTime		if file is older than this time, delete it [ms]
	* @return:	succes		1 = success, errCode = 0 =error
	*/
	function lockFile(file, pollPeriod, maxTime){
		var fs = require('fs');
		var fd_lock;
		var isLocked = 0;	//1 = locked
		if(file == 0 || pollPeriod == 0 || maxTime == 0){
			console.error("servo.js\tinvalid Data for 'lockFile()'");
			isLocked = "invalid data for 'lockingFile()' in servo.js";
		}
		else {
			while(!isLocked){
				try{
					fd_lock = fs.openSync(file, 'wx');
					fs.writeSync(fd_lock, '');
					isLocked = 1;
				} catch (err){
					isLocked = 0;
					if(fs.existsSync(file)){
						var stats = fs.statSync(file);
						var mtime = stats.mtime.getTime();
						if((Date.now() - mtime) > maxTime){
							fs.unlink(file, function(error){
								if (error) isLocked = error;
							});
						}
					}
				}
			}
		}
		return isLocked;
	}

	/**
	* Delete a lockfile
	* @param: 	file		adress of lockfile
	*/
	function unlockingFile(file){
		var fs = require('fs');
		var deleted;
		try{
			fs.unlinkSync(file);
			deleted = 0;
		} catch (error){
			deleted = error;
		}
		return deleted;
	}
}
