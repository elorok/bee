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
                //check if there are 6 lines (6 PWMs)
                import java.util.Scanner;
                
                int linesCount = 0;
                Scanner fileScanner = null;
                file selectedFile = '/tmp/i2c_12_out';
                fileScanner = new Scanner(selectedFile);
                
                while (fileScanner.hasNextLine()){
                    linesCount++;
                    String line = fileScanner.nextLine();
                }
                
                
                var pwm = parseInt(msg.payload); 

                fs.writeFile('/tmp/testing', linesCount.toString(10), function (error) {
                    if (error) throw error;
                })

                var parts = msg.payload.split(","); //split at comma
                parts[1] = parseInt(parts[1], 16);

                fs.writeFile('/tmp/i2c_12_out', parts[0].toString(10) + "\n" + parts[1].toString(10), function (error) {
                    if (error) throw error;
                })
            } catch (error){
                node.error(error);
            }
        });
    }
    RED.nodes.registerType("servo", ServoNode);
}
