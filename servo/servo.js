module.exports = function (RED) {
    "use strict";

    function ServoNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var fs = require('fs');

            // *** Read State ***
            try {
                fs.readFile('/tmp/i2c_12_in', 'utf8', function (error, contents) {
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
                //if file is empty --> write 0 in each line
                if os.stat('tmp/testing'.st_size == 0:
                    fs.writeFile('tmp/testing', "0\n0\n0\n0\n0\n0", function (error){
                        if (error) throw error;
                })
                
                var pwm = parseInt(msg.payload); 

                fs.writeFile('/tmp/i2c_12_out', pwm.toString(10), function (error) {
                    if (error) throw error;
                })
                
                //Test Gianni 30-SEP-2020
                var parts = msg.payload.split(","); //split at comma
                parts[1] = parseInt(parts[1], 16);

                fs.writeFile('/tmp/testing', parts[0].toString(10) + "\n" + parts[1].toString(10), function (error) {
                    if (error) throw error;
                })
                
            } catch (error) {
                node.error(error);
            }
        });
    }
    RED.nodes.registerType("servo", ServoNode);
}
