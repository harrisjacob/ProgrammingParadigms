import cherrypy

from climate import ClimateController
from reset import ResetController
from options import OptionsController
from _climate_database import _climate_database

def start_service():
	dispatcher = cherrypy.dispatch.RoutesDispatcher()

	cdb_o = _climate_database()
	climateController = ClimateController(cdb=cdb_o)
	resetController = ResetController(cdb=cdb_o)
	optionsController = OptionsController()

	dispatcher.connect('get_all_cities', '/cities/', controller=climateController, action='GET_DICT', conditions=dict(method=['GET']))
	dispatcher.connect('get_city', '/cities/:lid', controller=climateController, action='GET_KEY', conditions=dict(method=['GET']))
	dispatcher.connect('get_city_month', '/cities/:lid/:month', controller=climateController, action='GET_MONTH', conditions=dict(method=['GET']))
	dispatcher.connect('put_month','/cities/:lid/:month', controller = climateController, action = 'PUT_MONTH', conditions = dict(method=['PUT']))
	dispatcher.connect('put_high','/cities/:lid/:month/high', controller = climateController, action = 'PUT_HIGH', conditions = dict(method=['PUT']))
	dispatcher.connect('put_high','/cities/:lid/:month/low', controller = climateController, action = 'PUT_LOW', conditions = dict(method=['PUT']))
	dispatcher.connect('put_dry_days','/cities/:lid/:month/dryDays', controller = climateController, action = 'PUT_DRY_DAYS', conditions = dict(method=['PUT']))
	dispatcher.connect('put_snow_days','/cities/:lid/:month/snowDays', controller = climateController, action = 'PUT_SNOW_DAYS', conditions = dict(method=['PUT']))
	dispatcher.connect('put_rainfall','/cities/:lid/:month/rainfall', controller = climateController, action = 'PUT_RAINFALL', conditions = dict(method=['PUT']))	
	dispatcher.connect('put_city','/cities/', controller = climateController, action = 'POST_CITY', conditions = dict(method=['POST']))	

	
	dispatcher.connect('delete_all', '/cities/', controller=climateController, action='DELETE', conditions=dict(method=['DELETE']))
	dispatcher.connect('delete_location', '/cities/:lid', controller=climateController, action='DELETE_LOC', conditions=dict(method=['DELETE']))
	
	
	dispatcher.connect('reset','/reset/', controller = resetController, action = 'PUT', conditions = dict(method=['PUT']))

	#CORS
	dispatcher.connect('city_CORS', '/cities/:lid', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('city_month_CORS', '/cities/:lid/:month', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('high_CORS', '/cities/:lid/:month/high', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('low_CORS', '/cities/:lid/:month/low', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('dryDays_CORS', '/cities/:lid/:month/dryDays', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('snowDays_CORS', '/cities/:lid/:month/snowDays', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))
	dispatcher.connect('rainfall_CORS', '/cities/:lid/:month/rainfall', controller=optionsController, action='OPTIONS', conditions=dict(method=['OPTIONS']))


	conf = {
		'global' : {
			'server.thread_pool' : 5,
			'server.socket_host' : 'student04.cse.nd.edu',
			'server.socket_port' : 51023,
		},
		'/' : {
			'request.dispatch' : dispatcher,
			'tools.CORS.on'    : True
		}
	}

	cherrypy.config.update(conf)
	app = cherrypy.tree.mount(None, config=conf)
	cherrypy.quickstart(app)

def CORS():
	cherrypy.response.headers["Access-Control-Allow-Origin"] = "*"
	cherrypy.response.headers["Access-Control-Allow-Methods"] = "GET, PUT, POST, DELETE, OPTIONS"
	cherrypy.response.headers["Access-Control-Allow-Credentials"] = "true"


if __name__ == '__main__':
	cherrypy.tools.CORS = cherrypy.Tool('before_finalize', CORS)
	start_service()

