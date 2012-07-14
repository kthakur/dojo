define([
    "dojo/_base/declare",
    "dijit/form/Button"
], function(declare, Button){
    return declare("classy.Button", Button, {
        label: "My Classy Button",
        onClick: function(evt){
            console.log("I was clicked!");
            this.inherited(arguments);
        }
    });
});