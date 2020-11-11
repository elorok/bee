module.exports = function (RED) {
    "use strict";

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);

        var node = this;

        node.on('input', function (msg) {
            var fs = require('fs');

            try {
                var fd_in;  //filedescripter InputFile
                fd_in = fs.openSync('/tmp/i2c_10_in', 'r');
                fs.readFile(fd_in, 'utf8', function (error, contents) {
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
            } finally {
                if(fd_in){
                    fs.closeSync(fd_in);
                }
            }
        });
    }
    RED.nodes.registerType("button", ButtonNode);
}
