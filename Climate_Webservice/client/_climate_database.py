
import json
import requests

class _climate_database:

    def __init__(self):
        self.climates = {}
        self.months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
        self.cities = set()
        self.countries = set()

    def load_climates(self, climate_url):
        self.climates = requests.get(climate_url).json()
    
    
    def get_city(self, lid):
        for location in self.climates:
            if location['id'] == lid:
                return location['city']
        return None

    def print_climates(self): # show the data for every city
        for climate in self.climates:
            print('\n', climate['city'], ', ', climate['country'], ':\n')
            num = 0 
            for month in climate['monthlyAvg']:
                print('Month: ', self.months[num])
                print('High: ', month['high'], ' degrees Celsius')
                print('Low: ', month['low'], ' degrees Celsius')
                print('Dry Days: ', month['dryDays'], ' days')
                print('Snow Days: ', month['snowDays'], ' days')
                print('Rainfall: ', month['rainfall'], ' inches', '\n')
                num = num + 1
                
    def print_climate_city(self, city): #show the data for a given city
        found = False
        for location in self.climates:
            if city.lower() in location['city'].lower():
                found = True
                print('\n', location['city'], ', ', location['country'], ':\n')
                num = 0 
                for month in location['monthlyAvg']:
                    print('Month: ', self.months[num])
                    print('High: ', month['high'], ' degrees Celsius')
                    print('Low: ', month['low'], ' degrees Celsius')
                    print('Dry Days: ', month['dryDays'], ' days')
                    print('Snow Days: ', month['snowDays'], ' days')
                    print('Rainfall: ', month['rainfall'], ' inches', '\n')
                    num = num + 1
        if found == False:
            print('City not Found\n')

            
    def get_cities_in_country(self, country): # search for all of the cities listed in a given country
        cities = []
        for location in self.climates:
            if country.lower() in location['country'].lower():
                #print(location['city'])
                cities.append(location['city'])
        if len(cities) != 0:
            return cities
        else:
            return None

    def update_cities(self): # list all of the cities in the data
        for city in self.climates:
            self.cities.add(city['city'])
        return self.cities

    def update_countries(self): # list all of the countries in the data
        for country in self.climates:
            self.countries.add(country['country'])
        return self.countries
            

    def set_location(self, city, country, jan, feb, mar, apr, may, jun, jul, aug, sept, octo, nov, dec): # add a new location's information, or update if already exists; each month is a list of the proper data points
        info = {
                'id' : len(self.climates)+1, # increase the total number of entries
                'city' : city,
                'country' : country,
                'monthlyAvg' : [jan, feb, mar, apr, may, jun, jul, aug, sept, octo, nov, dec]
                }
        self.climates.append(info)
        #print(info)




    def delete_location(self, lid): # delete a locaiton by location id
        for count,location in enumerate(self.climates):
            #print(location['id'])
            if lid == location['id']:
                del self.climates[count]
            

    def dryest_location(self, month): # gives the least rainfall in a given month
        lid = -1 # storing the location id with the lowest rainfall in the month
        rainfall = 10000 # rainfall in inches
        for location in self.climates:
            if location['monthlyAvg'][month-1]['rainfall'] < rainfall: # if rainfall in the month is less than the stored value
                lid = location['id']
                rainfall = location['monthlyAvg'][month-1]['rainfall']
        return lid

    def warmest_location(self, month): # highest average high 
        lid = -1
        temp = -3000 # highest temp 
        for location in self.climates:
            if location['monthlyAvg'][month-1]['high'] > temp:
                lid = location['id']
                temp = location['monthlyAvg'][month-1]['high']
        return lid

    def coldest_location(self, month): # lowest average low 
        lid = -1
        temp = 3000 # highest temp 
        for location in self.climates:
            if location['monthlyAvg'][month-1]['low'] < temp:
                lid = location['id']
                temp = location['monthlyAvg'][month-1]['low']
        return lid
   
    def closest_temp(self, high): # finds the location with the closest high temp and lowest id, and gives the month to visit it
        diff = 10000000 # minimum difference in desired temp
        lid = -1
        month = -1
        for location in self.climates:
            num = 1 # keeping track of what month it is
            for m in location['monthlyAvg']:
                if abs(m['high'] - high) < diff:
                    month = num
                    lid = location['id']
                    diff = abs(m['high']-high)
                num = num +1

        return month, lid




if __name__ == '__main__':	
    cdb = _climate_database()
    cdb.load_climates('https://raw.githubusercontent.com/michaelx/climate/master/climate.json')
    '''cdb.print_climates()
    cdb.print_climate_city('Minneapolis')
    print(cdb.get_cities_in_country('United States'))
    print(cdb.update_cities())
    print(cdb.update_countries())
    

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

    cdb.set_location('Wayzata', 'United States', jan, feb, mar, apr, may, jun, jul, aug, sept, octo, nov, dec)
    cdb.print_climate_city('minneapolis')
    cdb.delete_location(105)
    cdb.print_climate_city('minneapolis')
    
    print(cdb.dryest_location(1))
    print(cdb.warmest_location(1))
    print(cdb.coldest_location(1))
    print(cdb.closest_temp(-3))
    '''

    print(cdb.warmest_location(1))
    print(cdb.coldest_location(1))
    print(cdb.closest_temp(20))

