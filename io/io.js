module.exports = function (RED) {
    "use strict";

    function IoNode(config) {
        RED.nodes.createNode(this, config);

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
                            var msgA = { payload: contents.split("\n")[0] };    // Analog
                            var msgD = contents.split("\n")[1];    // payload
                            var msgD0 = { payload: Math.round(msgD % 2) };
                            var msgD1 = { payload: Math.round(msgD / 2 % 2) };
                            var msgD2 = { payload: Math.round(msgD / 4 % 2) };
                            var msgD3 = { payload: Math.round(msgD / 8 % 2) };
                            node.send([msgA, msgD0, msgD1, msgD2, msgD3]);
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
                var payload = msg.payload;
                var topic = parseInt(msg.topic, 16);
                                
                fs.readFile('/tmp/i2c_11_out', 'utf8', function (error, output) {
                    if (error) throw error;
                


                switch(topic){
                    case 0:
                        if (payload == true)
                        {
                            output = (output |1<<0);  
                        }
                        else if (payload == false)
                        {
                            output = (output & ~(1<<0));
                        }
                       break;
                    case 1:
                        if (payload == true)
                        {
                            output = (output |1<<1);  
                        }
                        else if (payload == false)
                        {
                            output = (output & ~(1<<1));
                        }
                        break;
                    case 2:
                        if (payload == true) {
                            output = (output | 1 << 2);
                        }
                        else if (payload == false) {
                            output = (output & ~(1 << 2));
                        }
                        break;
                    case 3:
                        if (payload == true) {
                            output = (output | 1 << 3);
                        }
                        else if (payload == false) {
                            output = (output & ~(1 << 3));
                        }
                        break;
                    default:
                        break;
                }

                output = output.toString(10);
                if (output != null && output != "") {
                    fs.writeFile('/tmp/i2c_11_out', output, function (error) {
                        if (error) throw error;
                    })
                }

                })
            } catch (error) {
                node.error(error);
            }
        });
    }
    RED.nodes.registerType("io", IoNode)
}