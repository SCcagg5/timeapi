from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',        ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                     )
    @app.route('/dispo/',    	['OPTIONS', 'POST', 'GET'], lambda x = None: call([dispo])                )
    @app.route('/add/',    	    ['OPTIONS', 'POST'],        lambda x = None: call([add])                )
    def base():
        return
