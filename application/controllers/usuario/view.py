import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, idusuario):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(idusuario) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(idusuario):
    '''

    def GET(self, idusuario):
        idusuario = config.check_secure_val(str(idusuario)) # HMAC idusuario validate
        result = config.model.get_usuario(idusuario) # search for the idusuario data
        return config.render.view(result) # render view.html with idusuario data
