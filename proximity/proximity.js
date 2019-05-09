module.exports = function (RED) {
    "use strict";

    function ProximityNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        var address = 81;
        var exec = require('child_process').exec;

        // Init Sensor
        exec('/home/pi/bee/_tools/i2c/writeCommandWord.py ' + address + ' 0 0');    // Enable Ambilight Sensor
        exec('/home/pi/bee/_tools/i2c/writeCommandWord.py ' + address + ' 3 2250');    // Setup Proximity Sensor
        exec('/home/pi/bee/_tools/i2c/writeCommandWord.py ' + address + ' 4 1888');    // 

        node.on('input', function (msg) {
            exec('/home/pi/bee/_tools/i2c/readCommandWord.py ' + address + ' 8', function callback(error, stdout, stderr) {   // Read Register Proximity
                if (error == null) {
                    node.status({ fill: "green", shape: "dot", text: "connected" });
                    msg.payload = stdout;
                    node.send([msg,null]);
                }
                else {
                    node.status({ fill: "red", shape: "dot", text: "disconnected" });
                    node.error(stderr);
                }
            });

            exec('/home/pi/bee/_tools/i2c/readCommandWord.py ' + address + ' 9', function callback(error, stdout, stderr) {   // Read Register Ambilight
                if (error == null) {
                    msg.payload = stdout;
                    node.send([null,msg]);
                }
                else {
                    node.error(stderr);
                }
            });
        });
    }
    RED.nodes.registerType("button", ButtonNode);
}
