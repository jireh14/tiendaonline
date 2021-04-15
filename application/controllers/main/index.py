from . import config
import app

class Index:
    
    def __init__(self):
        pass

    @staticmethod
    def GET():
        if app.session.loggedin is True:
            nombre_admin = app.session.nombre_admin
            privilege = app.session.privilege
            params = {}
            params['nombre_admin'] = nombre_admin
            params['privilege'] = privilege
            if privilege == 0:
                return config.render.admin(params)
            elif privilege == 1:
                return config.render.guess(params)
        else:
            params = {}
            params['nombre_admin'] = 'anonymous'
            params['privilege'] = '-1'
            return config.render.index(params)