//main.js
var baseURL = "http://student04.cse.nd.edu:51023/cities/"

//Set up inherited items
Label.prototype = new Item(); // label will inherit from item
Button.prototype = new Item();
Dropdown.prototype = new Item();
Image.prototype = new Item();
Div.prototype = new Item();
Textbox.prototype = new Item();
Switch.prototype = new Item();
/*
var cities = {
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

//Get Return Labels

/*
newSwitch = new Switch();
newSwitch.createSwitch("id1");
newSwitch.addToDocument();
*/

getCityTitle = new Label();
getCityTitle.createLabel("City:", "getCityLabel");
//getCityTitle.addToDocument();

getCityResp = new Label();
getCityResp.createLabel("", "getCityResp");
//getCityResp.addToDocument();

getMonthTitle = new Label();
getMonthTitle.createLabel("Month:","getMonthTitle");
//getMonthTitle.addToDocument();

getMonthResp = new Label();
getMonthResp.createLabel("","getMonthResp");
//getMonthResp.addToDocument();

getHighTitle = new Label();
getHighTitle.createLabel("High:","getHighTitle");
//getHighTitle.addToDocument();

getHighResp = new Label();
getHighResp.createLabel("","getHighResp");
//getHighResp.addToDocument();

getLowTitle = new Label();
getLowTitle.createLabel("Label:","getLowTitle");
//getLowTitle.addToDocument();

getLowResp = new Label();
getLowResp.createLabel("","getLowResp");
//getLowResp.addToDocument();

getDDTitle = new Label();
getDDTitle.createLabel("Dry Days:","getDDTitle");
//getDDTitle.addToDocument();

getDDResp = new Label();
getDDResp.createLabel("","getDDResp");
//getDDResp.addToDocument();

getSDTitle = new Label();
getSDTitle.createLabel("Snow Days:","getSDTitle");
//getSDTitle.addToDocument();

getSDResp = new Label();
getSDResp.createLabel("","getSDResp");
//getSDResp.addToDocument();

getRainTitle = new Label();
getRainTitle.createLabel("Rainfall:","getRainTitle");
//getRainTitle.addToDocument();

getRainResp = new Label();
getRainResp.createLabel("","getRainResp");
//getRainResp.addToDocument();


//Get Set Query

getCityLabel = new Label();
getCityLabel.createLabel("City Select:", "getCityLabel");
//getCityLabel.addToDocument();







//loadCities();






//var tempV = loadCities();
cityDrop = new Dropdown();
loadCities(cityDrop, "cities");
//cityDrop.createDropdown(loadCities(), "cities");
//cityDrop.addToDocument();

getMonthLabel = new Label();
getMonthLabel.createLabel("Month Select:", "getMonthLabel");
//getMonthLabel.addToDocument();

monthDrop = new Dropdown();
monthDrop.createDropdown(monthsList, "months");
//monthDrop.addToDocument();

getMonthButton = new Button();
getMonthButton.createButton("GO", "getMonthButton");
//getMonthButton.addToDocument();
var drops = [cityDrop, monthDrop]
getMonthButton.addClickEventHandler(fetchMonth, drops);


//DIVS
var hugeDiv = new Div();
var getCityDiv = new Div();
var getMonthDiv = new Div();
var displayDiv = new Div();
var buttonDiv = new Div();

var cityCont = new Div();
var monthCont = new Div();
var highCont = new Div();
var lowCont = new Div();
var dryCont = new Div();
var snowCont = new Div();
var rainCont = new Div();


/* divs to request the information */

cityCont.createDiv("cityCont");
monthCont.createDiv("monthCont");
highCont.createDiv("highCont");
lowCont.createDiv("lowCont");
dryCont.createDiv("dryCont");
snowCont.createDiv("snowCont");
rainCont.createDiv("rainCont");

buttonDiv.createDiv("buttonDiv");
buttonDiv.addItem(getMonthButton);

getMonthDiv.createDiv("getMonthDiv");

getCityDiv.createDiv("getCityDiv");

getCityDiv.addItem(getCityLabel);
//getCityDiv.addItem(cityDrop);
getMonthDiv.addItem(getMonthLabel);
getMonthDiv.addItem(monthDrop);
/* divs to display the information */
var cityDiv = new Div();
var dispCityDiv = new Div(); // any Div with disp means this is the one that'll have the display text

var monthDiv = new Div();
var dispMonthDiv = new Div();

var highDiv = new Div();
var dispHighDiv = new Div();

var lowDiv = new Div();
var dispLowDiv = new Div();

var dryDiv = new Div();
var dispDryDiv = new Div();

var snowDiv = new Div();
var dispSnowDiv = new Div();

var rainDiv = new Div();
var dispRainDiv = new Div();


cityDiv.createDiv("cityDiv");
cityDiv.addItem(getCityTitle);
dispCityDiv.createDiv("dispCityDiv");
dispCityDiv.addItem(getCityResp);

monthDiv.createDiv("monthDiv");
monthDiv.addItem(getMonthTitle);
dispMonthDiv.createDiv("dispMonthDiv");
dispMonthDiv.addItem(getMonthResp);

highDiv.createDiv("highDiv");
highDiv.addItem(getHighTitle);
dispHighDiv.createDiv("dispHighDiv");
dispHighDiv.addItem(getHighResp);

lowDiv.createDiv("lowDiv");
lowDiv.addItem(getLowTitle);
dispLowDiv.createDiv("dispLowDiv");
dispLowDiv.addItem(getLowResp);

dryDiv.createDiv("dryDiv");
dryDiv.addItem(getDDTitle);
dispDryDiv.createDiv("dispDryDiv");
dispDryDiv.addItem(getDDResp);

snowDiv.createDiv("snowDiv");
snowDiv.addItem(getSDTitle);
dispSnowDiv.createDiv("dispSnowDiv");
dispSnowDiv.addItem(getSDResp);

rainDiv.createDiv("rainDiv");
rainDiv.addItem(getRainTitle);
dispRainDiv.createDiv("dispRainDiv");
dispRainDiv.addItem(getRainResp);

displayDiv.createDiv("displayDiv");
cityCont.addItem(cityDiv);
cityCont.addItem(dispCityDiv);
monthCont.addItem(monthDiv);
monthCont.addItem(dispMonthDiv);
highCont.addItem(highDiv);
highCont.addItem(dispHighDiv);
lowCont.addItem(lowDiv);
lowCont.addItem(dispLowDiv);
dryCont.addItem(dryDiv);
dryCont.addItem(dispDryDiv);
snowCont.addItem(snowDiv);
snowCont.addItem(dispSnowDiv);
rainCont.addItem(rainDiv);
rainCont.addItem(dispRainDiv);

displayDiv.addItem(cityCont);
displayDiv.addItem(monthCont);
displayDiv.addItem(highCont);
displayDiv.addItem(lowCont);
displayDiv.addItem(snowCont);
displayDiv.addItem(rainCont);

hugeDiv.createDiv("hugeDiv", "hugeDiv");
hugeDiv.addItem(getCityDiv);
hugeDiv.addItem(getMonthDiv);
hugeDiv.addItem(buttonDiv);
hugeDiv.addItem(displayDiv);
hugeDiv.addToDocument();




function loadCities(dropObj, id){

	var cityLoad = new XMLHttpRequest();

	cityLoad.open("GET", baseURL, true);

	cityLoad.onload = function(e){
		//console.log(cityLoad.responseText);
		var data = JSON.parse(cityLoad.responseText)['cities'];
		var newData = {};
		for(i = 0; i < data.length; i++){
			newData[data[i]['id']] = data[i]['city']
			//console.log(data[i]['id'], data[i]['city']);
		}
		console.log(newData[1]);
		dropObj.createDropdown(newData, id);
		getCityDiv.addItem(cityDrop);
		//return newData;
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


function fetchMonth(args){
	
	var queMonth = convertMonth(args[1]);
	
	var cityID = convertCity(args[0]);
	
	var getFullMonth = new XMLHttpRequest();

	getFullMonth.open("GET", baseURL.concat(cityID,"/",queMonth), true);

	getFullMonth.onload = function(e){
		console.log(getFullMonth.responseText);
		var CityMonth = JSON.parse(getFullMonth.responseText);
		setCityMonthGet(CityMonth, args[1]);
			
	}

	getFullMonth.onerror = function(e){
		console.error(getFullMonth.statusText);
	}

	getFullMonth.send(null);

}

function setCityMonthGet(data, Month){

	if(data["result"]!="success"){
		console.log("JSON Failure");
		return;
	}
	
	getCityResp.setText(data["city"]);
	getMonthResp.setText(monthsList[Month.getSelected()]);
	getHighResp.setText(data["climate"]["high"]);
	getLowResp.setText(data["climate"]["low"]);
	getDDResp.setText(data["climate"]["dryDays"]);
	getSDResp.setText(data["climate"]["snowDays"]);
	getRainResp.setText(data["climate"]["rainfall"]);
	
}

