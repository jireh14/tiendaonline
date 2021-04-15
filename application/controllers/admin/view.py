import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    
    def GET(self, nombre_admin):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(nombre_admin) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(nombre_admin):
        nombre_admin = config.check_secure_val(str(nombre_admin)) # HMAC nombre_admin validate
        result = config.model.get_admin(nombre_admin) # search for the nombre_admin data
        return config.render.view(result) # render view.html with nombre_admin data


