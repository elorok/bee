module.exports = function (RED) {
    "use strict";

    function LEDNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var fs = require('fs');

            // *** Read State ***
            try {
                fs.readFile('/tmp/i2c_9_in', 'utf8', function (error, contents) {
                    if (error == null) {
                        if (contents != "<offline>") {
                            node.status({ fill: "green", shape: "dot", text: "connected" });
                        } else {
                            node.status({ fill: "red", shape: "dot", text: "disconnected" });
                        }
                    } else {
                        node.status({ fill: "red", shape: "dot", text: "disconnected" });
                        node.error(stderr);
                    }
                })
            } catch (error) {
                node.status({ fill: "red", shape: "dot", text: "disconnected" });
                node.error(error);
            }


            // *** Write Data ***
            try {
                red = new BigNumber(msg.payload.substring(0, 2), 16);
                green = new BigNumber(msg.payload.substring(2, 4), 16);
                blue = new BigNumber(msg.payload.substring(4, 6), 16);


                fs.writeFile('/tmp/i2c_9_out', str(red) + "\n" + str(green) + "\n" + str(blue), function (error) {
                    if (error) throw error;
                })
            } catch (error) {
                node.error(error);
            }
        });
    }
    RED.nodes.registerType("led", LEDNode);
}
