module.exports = function (RED) {
    "use strict";

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);

        this.readFrequency = config.readFrequency; 
        var node = this;

        node.on('input', function (msg) {
            var address = 10;

            var exec = require('child_process').exec;
            exec('/home/pi/bee/_tools/i2c/readByte.py ' + address, function callback(error, stdout, stderr) {
                msg.payload = node.readFrequency + stdout;
                node.send(msg);
            });
        });
    }
    RED.nodes.registerType("button", ButtonNode);
}
