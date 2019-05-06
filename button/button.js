module.exports = function (RED) {
    "use strict";

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var address = parseInt(10);

            var exec = require('child_process').exec;
            exec('/home/pi/bee/_tools/i2c/readByte.py ' + address, function callback(error, stdout, stderr) {
                node.send(stdout);
            });
        });

        node.on("close", function () {

        });

    }
    RED.nodes.registerType("button", ButtonNode);
}
