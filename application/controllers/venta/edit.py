import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, idventa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(idventa) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idventa, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(idventa) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(idventa, **k):

    @staticmethod
    def POST_EDIT(idventa, **k):
        
    '''

    def GET(self, idventa, **k):
        message = None # Error message
        idventa = config.check_secure_val(str(idventa)) # HMAC idventa validate
        result = config.model.get_venta(int(idventa)) # search for the idventa
        result.idventa = config.make_secure_val(str(result.idventa)) # apply HMAC for idventa
        return config.render.edit(result, message) # render venta edit.html

    def POST(self, idventa, **k):
        form = config.web.input()  # get form data
        form['idventa'] = config.check_secure_val(str(form['idventa'])) # HMAC idventa validate
        # edit user with new data
        result = config.model.edit_venta(
            form['idventa'],form['idusuario'],form['total'],form['idformapago'],
        )
        if result == None: # Error on udpate data
            idventa = config.check_secure_val(str(idventa)) # validate HMAC idventa
            result = config.model.get_venta(int(idventa)) # search for idventa data
            result.idventa = config.make_secure_val(str(result.idventa)) # apply HMAC to idventa
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/venta') # render venta index.html
