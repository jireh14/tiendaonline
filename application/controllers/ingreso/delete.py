import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, idingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idingreso) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idingreso) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(idingreso, **k):

    @staticmethod
    def POST_DELETE(idingreso, **k):
    '''

    def GET(self, idingreso, **k):
        message = None # Error message
        idingreso = config.check_secure_val(str(idingreso)) # HMAC idingreso validate
        result = config.model.get_ingreso(int(idingreso)) # search  idingreso
        result.idingreso = config.make_secure_val(str(result.idingreso)) # apply HMAC for idingreso
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, idingreso, **k):
        form = config.web.input() # get form data
        form['idingreso'] = config.check_secure_val(str(form['idingreso'])) # HMAC idingreso validate
        result = config.model.delete_ingreso(form['idingreso']) # get ingreso data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idingreso = config.check_secure_val(str(idingreso))  # HMAC user validate
            idingreso = config.check_secure_val(str(idingreso))  # HMAC user validate
            result = config.model.get_ingreso(int(idingreso)) # get idingreso data
            result.idingreso = config.make_secure_val(str(result.idingreso)) # apply HMAC to idingreso
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/ingreso') # render ingreso delete.html 
