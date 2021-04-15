import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, idformapago, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idformapago) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idformapago, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idformapago) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(idformapago, **k):

    @staticmethod
    def POST_DELETE(idformapago, **k):
    '''

    def GET(self, idformapago, **k):
        message = None # Error message
        idformapago = config.check_secure_val(str(idformapago)) # HMAC idformapago validate
        result = config.model.get_formapago(int(idformapago)) # search  idformapago
        result.idformapago = config.make_secure_val(str(result.idformapago)) # apply HMAC for idformapago
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, idformapago, **k):
        form = config.web.input() # get form data
        form['idformapago'] = config.check_secure_val(str(form['idformapago'])) # HMAC idformapago validate
        result = config.model.delete_formapago(form['idformapago']) # get formapago data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idformapago = config.check_secure_val(str(idformapago))  # HMAC user validate
            idformapago = config.check_secure_val(str(idformapago))  # HMAC user validate
            result = config.model.get_formapago(int(idformapago)) # get idformapago data
            result.idformapago = config.make_secure_val(str(result.idformapago)) # apply HMAC to idformapago
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/formapago') # render formapago delete.html 
