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
                var pwm = parseInt(msg.payload); 

                fs.writeFile('/tmp/i2c_12_out', pwm.toString(10), function (error) {
                    if (error) throw error;
                })
                
                //Test Gianni 30-SEP-2020
                var parts = msg.payload.split(","); //split @comma
                parts[1] = parseInt(parts[1], 16);
                
                a_file = open('/tmp/testing', 'r');
                lines = a_file.readlines();
                a_file.close();
                
                del lines[(parts[0]-1)]
                
                new_file = open('/tmp/testing', 'w+');
                for line in lines:
                    new_file.write(line);
                
                new_file.close();
                
                var line = 0;
                var char = 0;
                
                file = open('/tmp/testing', 'w');
                while line <= 6:
                    if line == parts[0]:
                        file.write(parts[1].toString(10) + "\n");
                        break;
                    char = file.read(1);
                    if char == '\n':
                        line = line + 1;
                
//              only for testing  fs.writeFile('/tmp/testing', parts[0].toString(10) + "\n" + parts[1].toString(10), function (error) {
//                  if (error) throw error;
//              })
                
            } catch (error) {
                node.error(error);
            }
        });
    }
    RED.nodes.registerType("servo", ServoNode);
}
