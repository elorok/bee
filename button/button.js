module.exports = function (RED) {
    "use strict";

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var fs = require('fs');

            fs.readFile('/tmp/i2c_10', 'utf8', function (error, contents) {
                if (error == null) {
                    node.status({ fill: "green", shape: "dot", text: "connected" });
                    msg.payload = contents;
                    node.send(msg);
                }
                else {
                    node.status({ fill: "red", shape: "dot", text: "disconnected" });
                    node.message(error);
                }
            })
        });
    }
    RED.nodes.registerType("button", ButtonNode);
}
