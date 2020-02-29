import cherrypy
import json

from _climate_database import _climate_database

class ResetController(object):

    def __init__(self, cdb=None):
        if cdb is None:
            self.cdb = _climate_database()
        else:
            self.cdb = cdb

    def PUT(self):
        output = {'result':'success'}
        data = json.loads(cherrypy.request.body.read())
        try:
            self.cdb.load_climates('https://raw.githubusercontent.com/michaelx/climate/master/climate.json')
        except Exception as ex:
            output['result'] = 'error'
            output['message'] = str(ex)

        return json.dumps(output) 
