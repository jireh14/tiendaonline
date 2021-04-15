import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, idventa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idventa) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idventa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idventa) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(idventa, **k):

    @staticmethod
    def POST_DELETE(idventa, **k):
    '''

    def GET(self, idventa, **k):
        message = None # Error message
        idventa = config.check_secure_val(str(idventa)) # HMAC idventa validate
        result = config.model.get_venta(int(idventa)) # search  idventa
        result.idventa = config.make_secure_val(str(result.idventa)) # apply HMAC for idventa
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, idventa, **k):
        form = config.web.input() # get form data
        form['idventa'] = config.check_secure_val(str(form['idventa'])) # HMAC idventa validate
        result = config.model.delete_venta(form['idventa']) # get venta data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idventa = config.check_secure_val(str(idventa))  # HMAC user validate
            idventa = config.check_secure_val(str(idventa))  # HMAC user validate
            result = config.model.get_venta(int(idventa)) # get idventa data
            result.idventa = config.make_secure_val(str(result.idventa)) # apply HMAC to idventa
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/venta') # render venta delete.html 
