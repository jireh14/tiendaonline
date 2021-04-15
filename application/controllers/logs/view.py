from . import config
import app


class View:
    
    def __init__(self):
        pass

    def GET(self, nombre_admin):
        if app.session.loggedin is True:
            # username = app.session.username
            privilege = app.session.privilege
            if privilege == 0:
                return self.GET_VIEW(nombre_admin)
            elif privilege == 1:
                raise config.web.seeother('/guess')
        else:
            raise config.web.seeother('/login')

    @staticmethod
    def GET_VIEW(nombre_admin):
        nombre_admin = config.check_secure_val(str(nombre_admin))
        result = config.model_admin.get_admin(nombre_admin)
        print result
        return config.render.view(result)
