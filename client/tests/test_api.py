from _climate_database import _climate_database
import unittest

class TestClimateDatabase(unittest.TestCase):
    ''' unit tests for final project '''
    cdb = _climate_database()

    def reset_data(self):
        self.cdb.load_climates('https://raw.githubusercontent.com/michaelx/climate/master/climate.json')

    def test_get_cities_in_country(self):
        self.reset_data()
        location = self.cdb.get_cities_in_country('Mexico')
        self.assertEquals(location[0], 'Mexico City')

    def test_set_location(self):
        self.reset_data()
        jan = {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        feb = {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        mar = {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        apr= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        may= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        jun= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        jul= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        aug= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        sept= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        octo= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        nov= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        dec= {'high' : 1, 'low' : 2, 'dryDays' : 3, 'snowDays' : 4, 'rainfall' : 5}
        self.cdb.set_location('Wayzata', 'United States', jan, feb, mar, apr, may, jun, jul, aug, sept, octo, nov, dec)
        self.assertEquals(self.cdb.get_city(106), 'Wayzata')

    def test_delete_location(self):
        self.reset_data()
        self.cdb.delete_location(105)
        location = self.cdb.get_city(105)
        self.assertEquals(location, None)

    def test_get_city(self):
        self.reset_data()
        city = self.cdb.get_city(105)
        self.assertEquals(city, "Minneapolis MN")

    def test_dryest_location(self):
        self.reset_data()
        lid = self.cdb.dryest_location(1)
        self.assertEquals(lid, 41)

    def test_warmest_location(self):
        self.reset_data()
        lid = self.cdb.warmest_location(1)
        self.assertEquals(lid, 6)

    def test_coldest_location(self):
        self.reset_data()
        lid = self.cdb.coldest_location(1)
        self.assertEquals(lid, 62)

    def test_closest_temp(self):
        self.reset_data()
        month, lid = self.cdb.closest_temp(20)
        self.assertEquals(month, 7)
        self.assertEquals(lid, 1)


if __name__ == '__main__':
    unittest.main()
