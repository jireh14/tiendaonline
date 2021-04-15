from . import config
import hashlib
import app


class Edit:

    def _init_(self):
        pass

    def GET(self, nombre_admin, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(nombre_admin) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, nombre_admin, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(nombre_admin) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(nombre_admin, **k):
        message = None # Error message
        nombre_admin = config.check_secure_val(str(nombre_admin)) # HMAC user validate
        result = config.model.get_admin(nombre_admin) # search for the user
        result.nombre_admin = config.make_secure_val(str(result.nombre_admin)) # apply HMAC for username
        return config.render.edit(result, message) # render edit.html
    
    @staticmethod
    def POST_EDIT(nombre_admin, **k):
        form = config.web.input() # get form data
        nombre_admin = config.check_secure_val(str(nombre_admin)) # HMAC user validate
        admin = config.model.get_admin(nombre_admin)  # search for the user
        pwd = admin.password # get database user password

        if pwd == form.password: # compare the database user password with form new password
            pwdhash = pwd # its the same password
        else: # has a new password
            pwdhash = hashlib.md5(form.password + config.secret_key).hexdigest() # encrypt the new password

        nombre_admin = hashlib.md5(form.nombre_admin + config.secret_key).hexdigest() # create a new user_hash

        form.nombre_admin = config.check_secure_val(str(form.nombre_admin)) # validate HMAC username

        # edit user with new data
        result = config.model.edit_admin(
            form['nombre_admin'],
            form['apellidos_admin'],
            form['num_cuenta'],
            form['nombre_banco'],
            form['tipo_tarjeta_admin'],
            form['num_tarjeta'],
            form['telefono_admin'],
            form['correo_admin'],
            pwdhash,
            form['privilege'],
            form['user_hash'],
            form['change_pwd'],
            form['status_admin']
        )
        if result == None: # Error on udpate values
            nombre_admin = config.check_secure_val(str(nombre_admin)) # validate HMAC username
            result = config.model.get_admin(nombre_admin) # search for username data
            result.nombre_admin = config.make_secure_val(str(result.nombre_admin)) # apply HMAC to username
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/admin') # render users index.html