module.exports = function (RED) {
	"use strict";

	function LEDNode(config) {
		RED.nodes.createNode(this, config);

		var node = this;

		node.on('input', function (msg) {
			var fs = require('fs');

			// *** Read State ***
			var fd_in;  //filedescripter inputFile
			try {
				fd_in = fs.openSync('/tmp/i2c_9_in', 'r');
				var contents = fs.readFileSync(fd_in, 'utf8');
				if (contents == "<online>") {
					node.status({ fill: "green", shape: "dot", text: "connected" });
				} else {
					node.status({ fill: "red", shape: "dot", text: "disconnected" });
				}
			} catch (error) {
				node.status({ fill: "red", shape: "dot", text: "disconnected" });
				node.error(error);
			}finally{
				if(fd_in){
					fs.closeSync(fd_in);
				}
			}

			// *** Write Data ***
			try {
				var fd_out;  //filedescripter outputFile
				var red = parseInt(msg.payload.substring(0, 2), 16);
				var green = parseInt(msg.payload.substring(2, 4), 16);
				var blue = parseInt(msg.payload.substring(4, 6), 16);

				fd_out = fs.openSync('/tmp/i2c_9_out', 'w');
				fs.writeFile(fd_out, red.toString(10) + "\n" + green.toString(10) + "\n" + blue.toString(10));
			} catch (error) {
				node.error(error);
			}finally{
				if(fd_out){
					fs.closeSync(fd_out);
				}
			}
		});
	}
	RED.nodes.registerType("led", LEDNode);
}
