import json

with open('climate.json') as json_file:
	data = json.load(json_file)
	for cityObj in data:
		print("\t %s : \"%s\"," % (cityObj['id'],cityObj['city']))

