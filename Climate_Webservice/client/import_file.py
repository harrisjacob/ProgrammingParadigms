import json
import requests

data = requests.get("https://raw.githubusercontent.com/michaelx/climate/master/climate.json").json()

print("{}: January High: {}".format(data[0]["city"], data[0]["monthlyAvg"][0]["high"]))

#arr = json.loads("WeatherByCity.json")

#with open('climate.json', 'r') as json_file:
#	j_data = json_file.read()

#data = json.loads(j_data)
