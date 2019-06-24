module.exports = function (RED) {
    "use strict";

    function ProximityNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var fs = require('fs');

            try {
                fs.readFile('/tmp/i2c_81', 'utf8', function (error, contents) {
                    if (error == null) {
                        if (contents != "<offline>") {
                            node.status({ fill: "green", shape: "dot", text: "connected" });

                            msg.payload = contents.split(/\r?\n/);
                            node.send(msg);
                            /*msg.payload = contents;
                            node.send([null, msg]);*/
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

            /*
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
            });*/
        });
    }
    RED.nodes.registerType("proximity", ProximityNode);
}
