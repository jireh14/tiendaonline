import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, iddetalle_ingreso):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(iddetalle_ingreso) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(iddetalle_ingreso):
    '''

    def GET(self, iddetalle_ingreso):
        iddetalle_ingreso = config.check_secure_val(str(iddetalle_ingreso)) # HMAC iddetalle_ingreso validate
        result = config.model.get_detalle_ingreso(iddetalle_ingreso) # search for the iddetalle_ingreso data
        return config.render.view(result) # render view.html with iddetalle_ingreso data
