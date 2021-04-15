import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, idusuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(idusuario) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idusuario, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(idusuario) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(idusuario, **k):

    @staticmethod
    def POST_EDIT(idusuario, **k):
        
    '''

    def GET(self, idusuario, **k):
        message = None # Error message
        idusuario = config.check_secure_val(str(idusuario)) # HMAC idusuario validate
        result = config.model.get_usuario(int(idusuario)) # search for the idusuario
        result.idusuario = config.make_secure_val(str(result.idusuario)) # apply HMAC for idusuario
        return config.render.edit(result, message) # render usuario edit.html

    def POST(self, idusuario, **k):
        form = config.web.input()  # get form data
        form['idusuario'] = config.check_secure_val(str(form['idusuario'])) # HMAC idusuario validate
        # edit user with new data
        result = config.model.edit_usuario(
            form['idusuario'],form['nombre'],form['apellidos'],form['correo_usuario'],form['contrasena'],form['calle_num'],form['colonia'],form['codigo_postal'],form['ciudad'],form['estado'],form['referencias'],form['fecha_reg_usu'],form['status_user'],
        )
        if result == None: # Error on udpate data
            idusuario = config.check_secure_val(str(idusuario)) # validate HMAC idusuario
            result = config.model.get_usuario(int(idusuario)) # search for idusuario data
            result.idusuario = config.make_secure_val(str(result.idusuario)) # apply HMAC to idusuario
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/usuario') # render usuario index.html
