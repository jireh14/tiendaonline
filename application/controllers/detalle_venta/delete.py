import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, iddetalle_venta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(iddetalle_venta) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, iddetalle_venta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(iddetalle_venta) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(iddetalle_venta, **k):

    @staticmethod
    def POST_DELETE(iddetalle_venta, **k):
    '''

    def GET(self, iddetalle_venta, **k):
        message = None # Error message
        iddetalle_venta = config.check_secure_val(str(iddetalle_venta)) # HMAC iddetalle_venta validate
        result = config.model.get_detalle_venta(int(iddetalle_venta)) # search  iddetalle_venta
        result.iddetalle_venta = config.make_secure_val(str(result.iddetalle_venta)) # apply HMAC for iddetalle_venta
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, iddetalle_venta, **k):
        form = config.web.input() # get form data
        form['iddetalle_venta'] = config.check_secure_val(str(form['iddetalle_venta'])) # HMAC iddetalle_venta validate
        result = config.model.delete_detalle_venta(form['iddetalle_venta']) # get detalle_venta data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            iddetalle_venta = config.check_secure_val(str(iddetalle_venta))  # HMAC user validate
            iddetalle_venta = config.check_secure_val(str(iddetalle_venta))  # HMAC user validate
            result = config.model.get_detalle_venta(int(iddetalle_venta)) # get iddetalle_venta data
            result.iddetalle_venta = config.make_secure_val(str(result.iddetalle_venta)) # apply HMAC to iddetalle_venta
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/detalle_venta') # render detalle_venta delete.html 
