from .routesfunc import *

def setuproute(app, call):
    @app.route('/test/',        ['OPTIONS', 'POST', 'GET'], lambda x = None: call([])                     )
    @app.route('/reserve/',    	['OPTIONS', 'POST'],        lambda x = None: call([reserve, dispo])       )
    @app.route('/dispo/',    	['OPTIONS', 'POST'],        lambda x = None: call([dispo])                )
    def base():
        return
