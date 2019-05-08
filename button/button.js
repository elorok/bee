module.exports = function (RED) {
    "use strict";

    var pollState = function () {
        var address = 10; 

        var exec = require('child_process').exec;
        exec('/home/pi/bee/_tools/i2c/readByte.py ' + address, function callback(error, stdout, stderr) {
            msg.payload = stdout;
            node.send(msg);
        });

        timeout = setTimeout(pollState, this.readFrequency);
    }

    function ButtonNode(config) {
        RED.nodes.createNode(this, config);

        this.readFrequency = config.readFrequency; 
        var node = this;

        this.timeout = setTimeout(pollState, this.readFrequency);

        /*node.on('input', function (msg) {
            var address = 10;

            var exec = require('child_process').exec;
            exec('/home/pi/bee/_tools/i2c/readByte.py ' + address, function callback(error, stdout, stderr) {
                msg.payload = stdout;
                node.send(msg);
            });
        });*/
    }
    RED.nodes.registerType("button", ButtonNode);
}
