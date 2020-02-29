import unittest
import requests
import json

class TestClimate(unittest.TestCase):

	SITE_URL = 'http://student04.cse.nd.edu:51023'
	CITIES_URL = SITE_URL + '/cities/'
	RESET_URL = SITE_URL + '/reset/'

	def reset_data(self):
		m = {}
		r = requests.put(self.RESET_URL, data = json.dumps(m))

	def is_json(self, resp):
		try:
			json.loads(resp)
			return True
		except ValueError:
			return False

	def test_month_put(self):
		self.reset_data()
		city = 8
		month = 'feb'

		r = requests.get(self.CITIES_URL + str(city) + '/' + month)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['high'], 6)
		self.assertEqual(resp['climate']['low'], -5)

		m = {}
		m['high'] = 101
		m['low'] = 1
		m['dryDays'] = 101
		r = requests.put(self.CITIES_URL + str(city) + '/'+  month, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.CITIES_URL + str(city) + '/' + month)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['high'], m['high'])
		self.assertEqual(resp['climate']['low'], m['low'])
		self.assertEqual(resp['climate']['dryDays'], m['dryDays'])


	def test_high_put(self):
		self.reset_data()
		city = 10
		month = 'mar'
		TEST_GET_URL = self.CITIES_URL + str(city) + '/' + month
		TEST_PUT_URL = TEST_GET_URL + '/high'

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['high'], 16)
		
		m = {}
		m['high'] = 101
		r = requests.put(TEST_PUT_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['high'], m['high'])


	def test_low_put(self):
		self.reset_data()
		city = 12
		month = 'dec'
		TEST_GET_URL = self.CITIES_URL + str(city) + '/' + month
		TEST_PUT_URL = TEST_GET_URL + '/low'

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['low'], -11)

		m = {}
		m['low'] = 0
		r = requests.put(TEST_PUT_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['low'], m['low'])


	def test_dryDays_put(self):
		self.reset_data()
		city = 18
		month = 'apr'
		TEST_GET_URL = self.CITIES_URL + str(city) + '/' + month
		TEST_PUT_URL = TEST_GET_URL + '/dryDays'

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['dryDays'], 16)

		m = {}
		m['dryDays'] = 38
		r = requests.put(TEST_PUT_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['dryDays'], m['dryDays'])

	def test_snowDays_put(self):
		self.reset_data()
		city = 31
		month = 'may'
		TEST_GET_URL = self.CITIES_URL + str(city) + '/' + month
		TEST_PUT_URL = TEST_GET_URL + '/snowDays'

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['snowDays'], 0)

		m = {}
		m['snowDays'] = 38
		r = requests.put(TEST_PUT_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['snowDays'], m['snowDays'])

	def test_rainfall_put(self):
		self.reset_data()
		city = 45
		month = 'aug'
		TEST_GET_URL = self.CITIES_URL + str(city) + '/' + month
		TEST_PUT_URL = TEST_GET_URL + '/rainfall'

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['rainfall'], 48.4)

		m = {}
		m['rainfall'] = 3
		r = requests.put(TEST_PUT_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['rainfall'], m['rainfall'])


	def test_post_city(self):
		self.reset_data()
		TEST_GET_URL = self.CITIES_URL + str(106)

		m = {'city':'demoCity'}
		m['country'] = 'demoCountry'
		r = requests.post(self.CITIES_URL, data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'],'success')

		r = requests.get(TEST_GET_URL)
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['city'],m['city'])


	def test_climate_get(self):
		self.reset_data()
		lid = 2
		r = requests.get(self.CITIES_URL + str(lid))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['city'], 'Athens')

	def test_climate_month_get(self):
		self.reset_data()
		lid = 3 
		month = 'feb'
		r = requests.get(self.CITIES_URL + str(lid) + '/' +  str(month))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['climate']['rainfall'], 100.4)

	def test_climate_delete_location(self):
		self.reset_data()
		lid = 4
		m = {}
		r = requests.delete(self.CITIES_URL + str(lid), data = json.dumps(m))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'success')

		r = requests.get(self.CITIES_URL + str(lid))
		self.assertTrue(self.is_json(r.content.decode('utf-8')))
		resp = json.loads(r.content.decode('utf-8'))
		self.assertEqual(resp['result'], 'error')


if __name__ == "__main__":
	unittest.main()

