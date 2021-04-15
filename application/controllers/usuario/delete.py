import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, idusuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idusuario) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idusuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idusuario) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(idusuario, **k):

    @staticmethod
    def POST_DELETE(idusuario, **k):
    '''

    def GET(self, idusuario, **k):
        message = None # Error message
        idusuario = config.check_secure_val(str(idusuario)) # HMAC idusuario validate
        result = config.model.get_usuario(int(idusuario)) # search  idusuario
        result.idusuario = config.make_secure_val(str(result.idusuario)) # apply HMAC for idusuario
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, idusuario, **k):
        form = config.web.input() # get form data
        form['idusuario'] = config.check_secure_val(str(form['idusuario'])) # HMAC idusuario validate
        result = config.model.delete_usuario(form['idusuario']) # get usuario data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idusuario = config.check_secure_val(str(idusuario))  # HMAC user validate
            idusuario = config.check_secure_val(str(idusuario))  # HMAC user validate
            result = config.model.get_usuario(int(idusuario)) # get idusuario data
            result.idusuario = config.make_secure_val(str(result.idusuario)) # apply HMAC to idusuario
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/usuario') # render usuario delete.html 
