module.exports = function (RED) {
    "use strict";

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var address = parseInt(10);

            var exec = require('child-process').exec;
            exec('/home/pi/bee/_tools/i2c/readByte.py', function callback(error, stdout, stderr) {
                msg = Object.assign({}, msg);

                msg.payload = stdout;
                node.send(msg);
            });
        });

        node.on("close", function () {

        });

    }
    RED.nodes.registerType("button", ButtonNode);
}
