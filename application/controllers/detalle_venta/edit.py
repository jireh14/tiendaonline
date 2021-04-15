import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, iddetalle_venta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(iddetalle_venta) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, iddetalle_venta, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(iddetalle_venta) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(iddetalle_venta, **k):

    @staticmethod
    def POST_EDIT(iddetalle_venta, **k):
        
    '''

    def GET(self, iddetalle_venta, **k):
        message = None # Error message
        iddetalle_venta = config.check_secure_val(str(iddetalle_venta)) # HMAC iddetalle_venta validate
        result = config.model.get_detalle_venta(int(iddetalle_venta)) # search for the iddetalle_venta
        result.iddetalle_venta = config.make_secure_val(str(result.iddetalle_venta)) # apply HMAC for iddetalle_venta
        return config.render.edit(result, message) # render detalle_venta edit.html

    def POST(self, iddetalle_venta, **k):
        form = config.web.input()  # get form data
        form['iddetalle_venta'] = config.check_secure_val(str(form['iddetalle_venta'])) # HMAC iddetalle_venta validate
        # edit user with new data
        result = config.model.edit_detalle_venta(
            form['iddetalle_venta'],form['idventa'],form['idproducto'],form['cantidad'],form['subtotal'],
        )
        if result == None: # Error on udpate data
            iddetalle_venta = config.check_secure_val(str(iddetalle_venta)) # validate HMAC iddetalle_venta
            result = config.model.get_detalle_venta(int(iddetalle_venta)) # search for iddetalle_venta data
            result.iddetalle_venta = config.make_secure_val(str(result.iddetalle_venta)) # apply HMAC to iddetalle_venta
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/detalle_venta') # render detalle_venta index.html
