module.exports = function(RED) {
    function UpperCaseNode(config) {
        RED.nodes.createNode(this,config);
        var node = this;
        node.on('input', function(msg) {
            msg.payload = msg.payload.toUpperCase();
            node.send(msg);
        });
    }
    RED.nodes.registerType("upper-case",UpperCaseNode);
}
