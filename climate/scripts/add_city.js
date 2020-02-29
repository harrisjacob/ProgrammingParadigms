//add.js
var baseURL = "http://student04.cse.nd.edu:51023/cities/"

//Set up inherited items
Label.prototype = new Item(); // label will inherit from item
Button.prototype = new Item();
Dropdown.prototype = new Item();
Image.prototype = new Item();
Div.prototype = new Item();
Textbox.prototype = new Item();
Switch.prototype = new Item();


postCityLabel = new Label();
postCityLabel.createLabel("City:", "postCityLabel");

postCityText = new Textbox();
postCityText.createTextbox("cityText");

postCountryLabel = new Label();
postCountryLabel.createLabel("Country:", "postCountryLabel");

postCountryText = new Textbox();
postCountryText.createTextbox("countryText");

postCityButton = new Button();
postCityButton.createButton("ADD", "postCityButton");
postCityButton.addClickEventHandler(postCity, [postCityText, postCountryText]);

//DIVS
var bigDiv = new Div();
var boxDiv = new Div();
var buttonDiv = new Div();
var boxButtonDiv = new Div();
var countryBoxDiv = new Div();

buttonDiv.createDiv("buttonDiv", "buttonDiv");
boxDiv.createDiv("boxDiv", "boxDiv");
boxButtonDiv.createDiv("boxButtonDiv", "boxButtonDiv");
bigDiv.createDiv("bigDiv", "bigDiv");
countryBoxDiv.createDiv("countryBoxDiv", "countryBoxDiv");


buttonDiv.addItem(postCityButton);
boxDiv.addItem(postCityLabel);
boxDiv.addItem(postCityText);
boxButtonDiv.addItem(boxDiv);
countryBoxDiv.addItem(postCountryLabel);
countryBoxDiv.addItem(postCountryText);
boxButtonDiv.addItem(countryBoxDiv);
boxButtonDiv.addItem(buttonDiv);
bigDiv.addItem(boxButtonDiv);

bigDiv.addToDocument();

function postCity(args){
	console.log(args[0].getText())
	var xhr1 = new XMLHttpRequest()
	var city = {"city" : args[0].getText(), "country" : args[1].getText()}
	var json = JSON.stringify(city);
	xhr1.open("POST", baseURL, true);

	xhr1.onload = function(e){
    if (xhr1.readyState == 4 && xhr1.status == 200){
		console.log(xhr1.statusText);
    }
  }
  xhr1.onerror = function(e){
    console.error(xhr1.statusText);
  }
  xhr1.send(json);
}

