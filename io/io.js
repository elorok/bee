module.exports = function (RED) {
	"use strict";

	function IoNode(config) {
		RED.nodes.createNode(this, config);

		var node = this;

		node.on('input', function (msg) {
			var fs = require('fs');
            
			// *** Read State and Data ***
			var fd_in;  //filedescripter inputFile
			try {
				fd_in = fs.openSync('/tmp/i2c_11_in', 'r');
				var contents = fs.readFileSync(fd_in, 'utf8');                  
				if (contents == "<offline>") {
					node.status({ fill: "red", shape: "dot", text: "disconnected" });
				} else if (contents == "<online>") {
					node.status({ fill: "green", shape: "dot", text: "connected" });
				} else {
					node.status({ fill: "green", shape: "dot", text: "connected" });
					var msgA = { payload: contents.split("\n")[0] };    // Analog
					var msgD = contents.split("\n")[1];                 // digital
					var msgD0 = { payload: Math.round(msgD % 2) };
					var msgD1 = { payload: Math.round(msgD / 2 % 2) };
					var msgD2 = { payload: Math.round(msgD / 4 % 2) };
					var msgD3 = { payload: Math.round(msgD / 8 % 2) };
					node.send([msgA, msgD0, msgD1, msgD2, msgD3]);
				}
			} catch (error) {
				node.status({ fill: "red", shape: "dot", text: "disconnected" });
				node.error(error);
            } finally {
				if(fd_in){
					fs.closeSync(fd_in);
				}
			}

			// *** Write Data ***
			var fd_out;  //filedescripter outputFile
			try {
				var payload = msg.payload;
				var topic = parseInt(msg.topic, 16);
				var output;

				const lockFilePath = "/tmp/.i2c_11_out.lock";
				while (fs.existsSync(lockFilePath)) {
                    ;
				}
				var fd_lock = fs.openSync(lockFilePath, 'w');
                
				fd_out = fs.openSync('/tmp/i2c_11_out', 'a+');
				var content = fs.readFileSync(fd_out, 'utf8');
				output = parseInt(content);

				switch (topic) {
					case 0:
						if (payload == true) {
							output = (output | 1 << 0);
						}
						else if (payload == false) {
							output = (output & ~(1 << 0));
						}
						break;
					case 1:
						if (payload == true) {
							output = (output | 1 << 1);
						}
						else if (payload == false) {
							output = (output & ~(1 << 1));
						}
						break;
					case 2:
						if (payload == true) {
							output = (output | 1 << 2);
						}
						else if (payload == false) {
							output = (output & ~(1 << 2));
						}
						break;
					case 3:
						if (payload == true) {
							output = (output | 1 << 3);
						}
						else if (payload == false) {
							output = (output & ~(1 << 3));
						}
						break;
					default:
						break;
				}

				output = output.toString(10);
				if (output != null && output != "") {
					fs.writeFileSync('/tmp/i2c_11_out', output);
				}
				fs.unlinkSync(lockFilePath);                
			} catch (error) {
				node.error(error);
			} finally {
				if(fd_out){
					fs.closeSync(fd_out);
				}
			}
		});
	}
    RED.nodes.registerType("io", IoNode)   
}
