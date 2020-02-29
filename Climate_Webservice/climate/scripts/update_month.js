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

/*var cities = {
         1 : "Amsterdam",
         2 : "Athens",
         3 : "Atlanta GA",
         4 : "Auckland",
         5 : "Austin TX",
         6 : "Bangkok",
         7 : "Barcelona",
         8 : "Beijing",
         9 : "Berlin",
         10 : "Bologna",
         11 : "Boston MA",
         12 : "Boulder CO",
         13 : "Brasilia",
         14 : "Brisbane",
         15 : "Brussels",
         16 : "Budapest",
         17 : "Buenos Aires",
         18 : "Calgary",
         19 : "Canberra",
         20 : "Cape Town",
         21 : "Chiang Mai",
         22 : "Chicago IL",
         23 : "Christchurch",
         24 : "Copenhagen",
         25 : "Dallas TX",
         26 : "Denver CO",
         27 : "Detroit MI",
         28 : "Dubai",
         29 : "Dublin",
         30 : "Granada",
         31 : "Halifax",
         32 : "Hanoi",
         33 : "Ho Chi Minh City",
         34 : "Hong Kong",
         35 : "Honolulu",
         36 : "Istanbul",
         37 : "Jakarta",
         38 : "Jerusalem",
         39 : "Johannesburg",
         40 : "Kansas City MO",
         41 : "Kolkata",
         42 : "Kuala Lumpur",
         43 : "Las Vegas NV",
         44 : "Lisbon",
         45 : "London",
         46 : "Los Angeles CA",
         47 : "Madrid",
         48 : "Marseille",
         49 : "Melbourne",
         50 : "Mexico City",
         51 : "Miami FL",
         52 : "Montreal",
         53 : "Moscow",
         54 : "Mumbai",
         55 : "New Delhi",
         56 : "New Orleans LA",
         57 : "New York City NY",
         58 : "Oakland CA",
         59 : "Orlando FL",
         60 : "Osaka",
         61 : "Oslo",
         62 : "Ottawa",
         63 : "Paris",
         64 : "Philadelphia PA",
         65 : "Phoenix AZ",
         66 : "Phuket",
         67 : "Portland OR",
         68 : "Porto",
         69 : "Prague",
         70 : "Quebec City",
         71 : "Reykjavik",
         72 : "Rio de Janeiro",
         73 : "Rome",
         74 : "Saint Petersburg",
         75 : "Salt Lake City UT",
         76 : "San Francisco CA",
         77 : "Santiago",
         78 : "Sao Paulo",
         79 : "Seattle WA",
         80 : "Seoul",
         81 : "Sevilla",
         82 : "Shanghai",
         83 : "Singapore",
         84 : "Sofia",
         85 : "Stockholm",
         86 : "Sydney",
         87 : "Taghazout",
         88 : "Tel Aviv",
         89 : "Tokyo",
         90 : "Toronto",
         91 : "Tucson AZ",
         92 : "Ubud Bali",
         93 : "Valencia",
         94 : "Vancouver",
         95 : "Venice",
         96 : "Vienna",
         97 : "Warsaw",
         98 : "Washington DC",
         99 : "Wellington",
         100 : "Zurich",
         101 : "Albuquerque NM",
         102 : "Vermont IL",
         103 : "Nashville TE",
         104 : "St. Louis MO",
         105 : "Minneapolis MN"
}*/

var monthABV = {
	1: "jan",
	2: "feb",
	3: "mar",
	4: "apr",
	5: "may",
	6: "jun",
	7: "jul",
	8: "aug",
	9: "sep",
	10:"oct",
	11:"nov",
	12:"dec"
}

var monthsList = {
	1: "January",
	2: "February",
	3: "March",
	4: "April",
	5: "May",
	6: "June",
	7: "July",
	8: "August",
	9: "September",
	10:"October",
	11:"November",
	12:"December"
}

var cityDiv = new Div();
putCityLabel = new Label();
putCityLabel.createLabel("City Select:", "putCityLabel");
cityDiv.createDiv("cityDiv");
cityDiv.addItem(putCityLabel);

var cityDropDiv = new Div();

putCityDrop = new Dropdown();
loadCities(putCityDrop, "cities");

//putCityDrop.createDropdown(cities, "cities");
cityDropDiv.createDiv("cityDropDiv");
//cityDropDiv.addItem(putCityDrop);

var monthDiv = new Div();
putMonthLabel = new Label();
putMonthLabel.createLabel("Month Select:", "putMonthLabel");
monthDiv.createDiv("monthDiv");
monthDiv.addItem(putMonthLabel);

var monthDropDiv = new Div();
putMonthDrop = new Dropdown();
putMonthDrop.createDropdown(monthsList, "months");
monthDropDiv.createDiv("monthDropDiv");
monthDropDiv.addItem(putMonthDrop);

var highDiv = new Div();
highDiv.createDiv("highDiv");
putHighLabel = new Label();
putHighLabel.createLabel("High:", "putHighLabel");
putHighText = new Textbox();
putHighText.createTextbox("putHighText");
highDiv.addItem(putHighLabel);
highDiv.addItem(putHighText);

var lowDiv = new Div();
lowDiv.createDiv("lowDiv");
putLowLabel = new Label();
putLowLabel.createLabel("Low:", "putLowLabel");
putLowText = new Textbox();
putLowText.createTextbox("putLowText");
lowDiv.addItem(putLowLabel);
lowDiv.addItem(putLowText);

var dryDiv = new Div();
dryDiv.createDiv("dryDiv");
putDryLabel = new Label();
putDryLabel.createLabel("Dry:", "putDryLabel");
putDryText = new Textbox();
putDryText.createTextbox("putDryText");
dryDiv.addItem(putDryLabel);
dryDiv.addItem(putDryText);

var snowDiv = new Div();
snowDiv.createDiv("snowDiv");
putSnowLabel = new Label();
putSnowLabel.createLabel("Snow:", "putSnowLabel");
putSnowText = new Textbox();
putSnowText.createTextbox("putSnowText");
snowDiv.addItem(putSnowLabel);
snowDiv.addItem(putSnowText);

var rainDiv = new Div();
rainDiv.createDiv("rainDiv");
putRainLabel = new Label();
putRainLabel.createLabel("Rain:", "putRainLabel");
putRainText = new Textbox();
putRainText.createTextbox("putRainText");
rainDiv.addItem(putRainLabel);
rainDiv.addItem(putRainText);



postCityButton = new Button();
postCityButton.createButton("UPDATE", "postCityButton");
postCityButton.addClickEventHandler(putMonth, [putCityDrop, putMonthDrop, putHighText, putLowText, putDryText, putSnowText, putRainText]);

//DIVS
var buttonDiv = new Div();
var boxButtonDiv = new Div();
var bigDiv = new Div();
var cityMenu = new Div();
var monthMenu = new Div();
var menuDiv = new Div();


cityMenu.createDiv("cityMenu");
cityMenu.addItem(cityDiv);
cityMenu.addItem(cityDropDiv);

monthMenu.createDiv("monthMenu");
monthMenu.addItem(monthDiv);
monthMenu.addItem(monthDropDiv);

menuDiv.createDiv("menuDiv");
menuDiv.addItem(cityMenu);
menuDiv.addItem(monthMenu);



buttonDiv.createDiv("buttonDiv");
buttonDiv.addItem(postCityButton);

boxButtonDiv.createDiv("boxButtonDiv");
bigDiv.createDiv("bigDiv");
boxButtonDiv.addItem(highDiv);
boxButtonDiv.addItem(lowDiv);
boxButtonDiv.addItem(dryDiv);
boxButtonDiv.addItem(snowDiv);
boxButtonDiv.addItem(rainDiv);
boxButtonDiv.addItem(buttonDiv);
bigDiv.addItem(menuDiv);
//bigDiv.addItem(cityDiv);
//bigDiv.addItem(cityDropDiv);
//bigDiv.addItem(monthDiv);
//bigDiv.addItem(monthDropDiv);
bigDiv.addItem(boxButtonDiv);

bigDiv.addToDocument();

function loadCities(drop, id){

	var cityLoad = new XMLHttpRequest();
	cityLoad.open("GET", baseURL, true);

	cityLoad.onload = function(e){
		console.log(cityLoad.responseText);
		var data = JSON.parse(cityLoad.responseText);
		data = data['cities'];
		var newData = {};
		
		for(i=0; i < data.length; i++){
			console.log(data[i]['cities']);
			newData[data[i]['id']] = data[i]['city'];
		}

		drop.createDropdown(newData, id);
		cityDropDiv.addItem(putCityDrop);
	}

	cityLoad.onerror = function(e){
		console.error(cityLoad.statusText);
	}

	cityLoad.send(null);
}


function convertMonth(args){
	var monthSelect = args.getSelected();
	return monthABV[monthSelect];
}


function convertCity(city){
	return city.getSelected();
}


function putMonth(args){
	console.log(args[0])
	var queMonth = convertMonth(args[1]);
	var cityID = convertCity(args[0]);
	var full_URL = baseURL.concat(cityID,"/",queMonth)
	var xhr1 = new XMLHttpRequest()
	var month = {"high": args[2].getText(), "low": args[3].getText(), "dryDays": args[4].getText(), "snowDays": args[5].getText(), "rainfall": args[6].getText()}
	var json = JSON.stringify(month);
	xhr1.open("PUT", full_URL, true);

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

