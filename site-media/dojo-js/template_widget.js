require(["dojo/_base/declare", "dijit/_Widget", "dijit/_Templated", "dijit/form/Button", "dojo/text!/site-media/dojo-widgets/template.html"], 
	function(declare, _Widget, _Templated, Button, template) {

		// Declare our widget
		return declare("demo.SomeWidget", [_Widget, _Templated], {
			//	get our template
			templateString: template,
			//templatePath: "//localhost:8000/site-media/dojo-widgets/template.html",
			
			widgetsInTemplate: true,
			//	some properties
			baseClass: "someWidgetBase",
			title: "",	//	we'll set this from the widget def
			//	hidden counter
			_counter: 1,
			_firstClicked: false,

			//	define an onClick handler
			onClick: function(){
				if(this._firstClicked){
					this.titleNode.innerHTML = this.title + " was clicked " + (++this._counter) + " times.";
				} else {
					this.titleNode.innerHTML = this.title + " was clicked!";
					this._firstClicked = true;
				}
			},
			postCreate: function(){
				this.titleNode.innerHTML = this.title;
			}
	});
});