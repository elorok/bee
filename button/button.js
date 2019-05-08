module.exports = function (RED) {
    "use strict";

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var address = 10;

            var exec = require('child_process').exec;
            exec('/home/pi/bee/_tools/i2c/readByte.py ' + address, function callback(error, stdout, stderr) {
                if (error == null) {
                    node.status({ fill: "green", shape: "dot", text: "connected" });
                    msg.payload = stdout;
                    node.send(msg);
                }
                else {
                    node.status({ fille: "red", shape: "dot", text: "disconnected" });
                    node.error(stderr);
                }
            });
        });
    }
    RED.nodes.registerType("button", ButtonNode);
}
