module.exports = function (RED) {
    "use strict";

    function ProximityNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var fs = require('fs');

            try {
                fs.readFile('/tmp/i2c_81_in', 'utf8', function (error, contents) {
                    if (error == null) {
                        if (contents == "<offline>") {
                            node.status({ fill: "red", shape: "dot", text: "disconnected" });
                        } else if (contents == "<online>") {
                            node.status({ fill: "green", shape: "dot", text: "connected" });
                        } else {
                            node.status({ fill: "green", shape: "dot", text: "connected" });

                            msg.payload = contents.split("\n")[0];
                            node.send([msg, null]);
                            msg.payload = contents.split("\n")[1];
                            node.send([null, msg]);
                        }
                    } else {
                        node.status({ fill: "red", shape: "dot", text: "disconnected" });
                        node.error(error);
                    }
                })
            } catch (error) {
                node.status({ fill: "red", shape: "dot", text: "disconnected" });
                node.error(error);
            }
        });
    }
    RED.nodes.registerType("proximity", ProximityNode);
}
