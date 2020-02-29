import json
import cherrypy
from _climate_database import _climate_database

class ClimateController(object):
	def __init__(self, cdb=None):
		if cdb is None:
			self.cdb = _climate_database()
		else:
			self.cdb = cdb
		self.months = {'jan':0, 'feb':1, 'mar':2, 'apr':3, 'may':4, 'jun':5, 'jul':6, 'aug':7, 'sep':8, 'oct':9, 'nov':10, 'dec':11}
		
		self.cdb.load_climates('https://raw.githubusercontent.com/michaelx/climate/master/climate.json')

	def GET_DICT(self):
		output = {'result':'success'}
		tmp_dict = {}
		tmp_list = []
		try:
			for city in self.cdb.climates:
				tmp_dict = city
				tmp_list.append(tmp_dict)
			output.update({'cities': tmp_list})
		except Exception as ex:
			output['result'] = error
			output['message'] = str(ex)
		return json.dumps(output)

	def GET_KEY(self, lid):
		output = {'result' : 'success'}
		key = int(lid)
		try:
			tmp_dict = self.cdb.get_city(key)
			if tmp_dict is not None:
				output.update({'city' : tmp_dict})
				tmp_dict = self.cdb.climates[key-1]
				output.update({'climate' : tmp_dict['monthlyAvg']})
			else:
				output['result'] = 'error'
				output['message'] = 'location id does not exist'
		except Exception as ex:
			output['result'] = error
			output['message'] = str(ex)
		return json.dumps(output)
	
	def GET_MONTH(self, lid, month):
		output = {'result' : 'success'}
		key = int(lid)
		nmonth = self.months[month]
		try:
			tmp_dict = self.cdb.get_city(key)
			if tmp_dict is not None:
				output.update({'city' : tmp_dict})
				tmp_dict = self.cdb.climates[key-1]
				output.update({'month' : month})
				output.update({'climate' : tmp_dict['monthlyAvg'][nmonth]})
		except Exception as ex:
			output['result'] = error
			output['message'] = str(ex)
		return json.dumps(output)


	def PUT_MONTH(self, lid, month):
		output = {'result':'success'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		imonth = self.months[month]
		try:
			for city in self.cdb.climates:
				if city['id'] == int(lid):
					city['monthlyAvg'][imonth] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT_HIGH(self, lid, month):
		output = {'result':'success'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		imonth = self.months[month]
		data = data['high']

		try:
			for city in self.cdb.climates:
				if city['id'] == int(lid):
					city['monthlyAvg'][imonth]['high'] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT_LOW(self, lid, month):
		output = {'result':'success'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		imonth = self.months[month]
		data = data['low']

		try:
			for city in self.cdb.climates:
				if city['id'] == int(lid):
					city['monthlyAvg'][imonth]['low'] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)
	
	def PUT_DRY_DAYS(self, lid, month):
		output = {'result':'success'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		imonth = self.months[month]
		data = data['dryDays']

		try:
			for city in self.cdb.climates:
				if city['id'] == int(lid):
					city['monthlyAvg'][imonth]['dryDays'] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT_SNOW_DAYS(self, lid, month):
		output = {'result':'success'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		imonth = self.months[month]
		data = data['snowDays']

		try:
			for city in self.cdb.climates:
				if city['id'] == int(lid):
					city['monthlyAvg'][imonth]['snowDays'] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def PUT_RAINFALL(self, lid, month):
		output = {'result':'success'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		imonth = self.months[month]
		data = data['rainfall']

		try:
			for city in self.cdb.climates:
				if city['id'] == int(lid):
					city['monthlyAvg'][imonth]['rainfall'] = data
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def POST_CITY(self): #user will send city and country
		output = {'result':'success'}
		data = cherrypy.request.body.read()
		data = json.loads(data)
		newEntry = {}

		try:
			cityCount = 0
			for city in self.cdb.climates:
				cityCount += 1
			cityCount+=1
			newEntry['city'] = data['city']
			newEntry['country'] = data['country']
			newEntry['id'] = cityCount
			
			monthList = []

			for i in range(12):
				newMonth = {}
				newMonth['high']=0
				newMonth['low'] =0
				newMonth['dryDays']=0
				newMonth['snowDays']=0
				newMonth['rainfall'] = 0
				monthList.append(newMonth)
			newEntry['monthlyAvg'] = monthList

			self.cdb.climates.append(newEntry)
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)
		return json.dumps(output)

	def DELETE(self):
		output = {'result':'succes'}
		try:
			self.cdb.climates.clear()
		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output) 

	def DELETE_LOC(self, lid):
		output = {'result':'success'}
		try:
			for i in range(len(self.cdb.climates)-1):
			#  print(self.cdb.climates[i]) 
				if int(self.cdb.climates[i]['id']) == int(lid):
					'''
					print(i)
					print(self.cdb.climates[i])
					print(self.cdb.climates[3])
					'''
					del self.cdb.climates[int(i)] 

		except Exception as ex:
			output['result'] = 'error'
			output['message'] = str(ex)

		return json.dumps(output) 

