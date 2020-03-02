module.exports = function (RED) {
    "use strict";

    function IONode(config) {
        IO.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var fs = require('fs');

            try {
                fs.readFile('/tmp/i2c_11_in', 'utf8', function (error, contents) {
                    if (error == null) {
                        if (contents == "<offline>") {
                            node.status({ fill: "red", shape: "dot", text: "disconnected" });
                        } else if (contents == "<online>") {
                            node.status({ fill: "green", shape: "dot", text: "connected" });
                        } else {
                            node.status({ fill: "green", shape: "dot", text: "connected" });
                            msg.payload = contents;
                            node.send(msg);
                        }
                    }
                    else {
                        node.status({ fill: "red", shape: "dot", text: "disconnected" });
                        node.error(error);
                    }
                })
            } catch (error) {
                node.status({ fill: "red", shape: "dot", text: "disconnected" });
                node.error(error);
            }

            // *** Write Data ***
            try {
                var digital = parseInt(msg.payload, 16);

                fs.writeFile('/tmp/i2c_11_out', digital.toString(10), function (error) {
                    if (error) throw error;
                })
            } catch (error) {
                node.error(error);
            }
        });
    }
    RED.nodes.registerType("io", IoNode)
}