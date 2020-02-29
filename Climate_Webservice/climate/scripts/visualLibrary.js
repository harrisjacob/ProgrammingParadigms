//visualLibrary.js


function Button(){
        this.createButton = function(text, id){
                this.item = document.createElement("button");//creates a button item
                this.item.setAttribute("id", id);//set the id of the item
                var itemText = document.createTextNode(text);//creates a text object
                this.item.appendChild(itemText);//add the text object to the button
        }

        this.addClickEventHandler = function(handler, args){
                this.item.onmouseup = function() {
                        handler(args);//this function is executed when a button is clicked
                };
        }
}


function Label() {
        this.createLabel = function(text, id){
                this.item = document.createElement("p");//create a label object
                this.item.setAttribute("id",id);//set the label id
                this.setText(text);//call the setText function
        }
        this.setText = function(text){
                	this.item.innerHTML = text;//sets the text of a label object
        }
}


function Dropdown(){
        this.createDropdown = function(dict, id){
                this.item = document.createElement("SELECT");//create a dropdown object
                this.item.setAttribute("id",id);//set the id of the new object

                for (var key in dict){//iterate through items in dictionary
                        listItem = document.createElement("option");//creates an object
                        listItem.setAttribute("value", key);//sets the key of each entry
                        listItem.innerHTML = dict[key];//gets the corresponding value for display
                        this.item.appendChild(listItem);
                }
	}

	this.getSelected = function(){
		return this.item[this.item.selectedIndex].value;
        }

	this.setAble = function(state){
		this.item.disabled = state;
	}
}

function Image(){
	this.createImage = function(src, id){
		this.item = document.createElement("img");
		this.item.setAttribute("id",id);
		this.item.setAttribute("src",src);
	}
}


function Item(){
        this.addToDocument = function(){
                document.body.appendChild(this.item);
        }
}

	
function Div(){
	Div.prototype = new Item();
	this.createDiv = function(id, className){
		this.item = document.createElement("div");
		this.item.setAttribute("id", id);
		this.item.setAttribute("class",className);
	}

	this.addItem = function(childItem){
		this.item.appendChild(childItem.item);
	}
}

/*
function Table(){
	Table.prototype = new Div();
	this.createTable = function(id){
		var container = new Div();
		var gCTD = new Div();//getCityTitleDiv
		var gCRD = new Div();//getCityRespDiv
		var gMTD = new Div();//getMonthTitleDiv
		var gMRD = new Div();
		var gHTD = new Div();//getHighTitleDiv
		var gHRD = new Div();
		var gLTD = new Div();//getLowTitleDiv
		var gLRD = new Div();
		var gDDTD = new Div();//getDryDaysTitleDiv
		var gDDRD = new Div();
		var gSDTD = new Div();//getSnowDaysTitleDiv
		var gSDRD = new Div();
		var gRTD = new Div();//getRainfallTitleDiv
		var gRRD = new Div();


		var City = new Div();
		var Month = new Div();
		var High = new Div();
		var Low = new Div();
		var dryDays = new Div();
		var snowDays = new Div();
		var rainfall = new Div();


		container.createDiv(id.concat("-container"));
		gCTD.createDiv(id.concat("-CityTitle"));
		gCRD.createDiv(id.concat("-CityResp"));
		gMTD.createDiv(id.concat("-MonthTitle"));
		gMRD.createDiv(id.concat("-MonthResp"));
		gHTD.createDiv(id.concat("-HighTitle"));
		gHRD.createDiv(id.concat("-HighResp"));
		gLTD.createDiv(id.concat("-LowTitle"));
		gLRD.createDiv(id.concat("-LowResp"));
		gDDTD.createDiv(id.concat("-dryDaysTitle"));
		gDDRD.createDiv(id.concat("-dryDaysResp"));
		gSDTD.createDiv(id.concat("-snowDaysTitle"));
		gSDRD.createDiv(id.concat("-snowDaysResp"));
		gRTD.createDiv(id.concat("-rainfallTitle"));
		gRRD.createDiv(id.concat("-rainfallResp"));

		City.createDiv(id.concat("-City"));
		Month.createDiv(id.concat("-Month"));
		High.createDiv(id.concat("-High"));
		Low.createDiv(id.concat("-Low"));
		dryDays.createDiv(id.concat("-dryDays"));
		snowDays.createDiv(id.concat("-snowDays"));
		rainfall.createDiv(id.concat("-rainfall"));


		City.addItem(gCTD);
		City.addItem(gCRD);
		Month.addItem(gMTD);
		Month.addItem(gMRD);
		High.addItem(gHTD);
		High.addItem(gHRD);
		Low.addItem(gLTD);
		Low.addItem(gLRD);
		dryDays.addItem(gDDTD);
		dryDays.addItem(gDDRD);
		snowDays.addItem(gSDTD);
		snowDays.addItem(gSDRD);
		rainfall.addItem(gRTD);
		rainfall.addItem(gRRD);
		
		container.addItem(City);
		container.addItem(Month);
		container.addItem(High);
		container.addItem(Low);
		container.addItem(dryDays);
		container.addItem(snowDays);
		container.addItem(rainfall);

		this.item = container;
	}
}
*/

function Textbox(){
	this.createTextbox = function(id){
		this.item = document.createElement("input");
		this.item.setAttribute("id",id);
	}
	
	this.getText = function(){
		return this.item.value;
	}

}

function Switch(){
	this.createSwitch = function(id){
		this.item = document.createElement("input");
		this.item.setAttribute("id",id);
		this.item.setAttribute("type","checkbox");
		this.item.setAttribute("class","slider");
	}

}
