module.exports = function (RED) {
    var I2C = require('i2c-bus');

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);
        var node = this;

        node.port = I2C.openSync(1);

        node.on('input', function (msg) {
            var address = parseInt(10); 
            var command = parseInt(1);
            var buffcount = parseInt(node.count);
            this.status({});

            node.port.readByte(address, command, funktion(err, size, res){
                if(err) {
                    node.error(err, msg);
                    return null;
                }
                else {
                    var payload; 

                    if(node.count == 1) {
                        payload = res[0];
                    }
                    else {
                        payload = res; 
                    }
                }
            }); 

            msg.payload = msg.payload.toLowerCase();
            node.send(msg);
        });

        node.on("close", function () {
            node.port.closeSync();
        });

    }
    RED.nodes.registerType("button", ButtonNode);
}
