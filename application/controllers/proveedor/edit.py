import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, idproveedor, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(idproveedor) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idproveedor, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(idproveedor) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(idproveedor, **k):

    @staticmethod
    def POST_EDIT(idproveedor, **k):
        
    '''

    def GET(self, idproveedor, **k):
        message = None # Error message
        idproveedor = config.check_secure_val(str(idproveedor)) # HMAC idproveedor validate
        result = config.model.get_proveedor(int(idproveedor)) # search for the idproveedor
        result.idproveedor = config.make_secure_val(str(result.idproveedor)) # apply HMAC for idproveedor
        return config.render.edit(result, message) # render proveedor edit.html

    def POST(self, idproveedor, **k):
        form = config.web.input()  # get form data
        form['idproveedor'] = config.check_secure_val(str(form['idproveedor'])) # HMAC idproveedor validate
        # edit user with new data
        result = config.model.edit_proveedor(
            form['idproveedor'],form['nombre_pro'],form['telefono_pro'],form['correo_pro'],form['status_prov'],
        )
        if result == None: # Error on udpate data
            idproveedor = config.check_secure_val(str(idproveedor)) # validate HMAC idproveedor
            result = config.model.get_proveedor(int(idproveedor)) # search for idproveedor data
            result.idproveedor = config.make_secure_val(str(result.idproveedor)) # apply HMAC to idproveedor
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/proveedor') # render proveedor index.html
