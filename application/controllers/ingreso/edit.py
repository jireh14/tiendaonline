import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, idingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(idingreso) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(idingreso) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(idingreso, **k):

    @staticmethod
    def POST_EDIT(idingreso, **k):
        
    '''

    def GET(self, idingreso, **k):
        message = None # Error message
        idingreso = config.check_secure_val(str(idingreso)) # HMAC idingreso validate
        result = config.model.get_ingreso(int(idingreso)) # search for the idingreso
        result.idingreso = config.make_secure_val(str(result.idingreso)) # apply HMAC for idingreso
        proveedors = config.model.get_all_proveedores().list() # get ingreso table list
        return config.render.edit(result, message, proveedors) # render ingreso edit.html

    def POST(self, idingreso, **k):
        form = config.web.input()  # get form data
        form['idingreso'] = config.check_secure_val(str(form['idingreso'])) # HMAC idingreso validate
        # edit user with new data
        result = config.model.edit_ingreso(
            form['idingreso'],form['idproveedor'],form['fecha_ingreso'],form['tipo_comprobante'],form['serie_comprobante'],form['numero_comprobante'],form['total'],
        )
        if result == None: # Error on udpate data
            idingreso = config.check_secure_val(str(idingreso)) # validate HMAC idingreso
            result = config.model.get_ingreso(int(idingreso)) # search for idingreso data
            result.idingreso = config.make_secure_val(str(result.idingreso)) # apply HMAC to idingreso
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/ingreso') # render ingreso index.html
