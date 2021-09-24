module.exports = function (RED) {
	"use strict";

	function TemperatureNode(config) {
		RED.nodes.createNode(this, config);
		this.address = config.address;
		var node = this;

		node.on('input', function (msg) {
			var fs = require('fs');

			//***Read State and Data***
			var fd_in;  //filedescripter inputFile
			try {
				fd_in = fs.openSync('/tmp/i2c_' + this.address + '_in', 'r');
				var contents = fs.readFileSync(fd_in, 'utf8');
				if (contents == "<offline>") {
					node.status({ fill: "red", shape: "dot", text: "disconnected" });
				} else if (contents == "<online>") {
					node.status({ fill: "green", shape: "dot", text: "connected" });
				} else {
					node.status({ fill: "green", shape: "dot", text: "connected" });

					var msgT = { payload: contents.split("\n")[0] };    // Temperature
					var msgH = { payload: contents.split("\n")[1] };    // Humidity
					var msgP = { payload: contents.split("\n")[2] };    // Pressure
					node.send([msgT, msgH, msgP]);
				}
			} catch (error) {
				node.status({ fill: "red", shape: "dot", text: "disconnected" });
				node.error(error);
			} finally{
				if(fd_in){
					fs.closeSync(fd_in);
				}
			}
		});
	}
	RED.nodes.registerType("temperature", TemperatureNode);
}
