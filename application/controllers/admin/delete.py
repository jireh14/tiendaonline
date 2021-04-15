import config
import app

class Delete:
    
    def __init__(self):
        pass

    def GET(self, nombre_admin, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(nombre_admin) # call GET_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, nombre_admin, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(nombre_admin) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(nombre_admin, **k):
        message = None # Error message
        nombre_admin = config.check_secure_val(str(nombre_admin)) # HMAC nombre_admin validate
        result = config.model.get_admin(nombre_admin) # search  nombre_admin
        result.nombre_admin = config.make_secure_val(str(result.nombre_admin)) # apply HMAC for nombre_admin
        return config.render.delete(result, message) # render delete.html with user data

    @staticmethod
    def POST_DELETE(nombre_admin, **k):
        form = config.web.input() # get form data
        nombre_admin = config.check_secure_val(str(form['nombre_admin'])) # HMAC user validate
        session_admin = app.session.nombre_admin # get session_username
        if nombre_admin != session_admin: # compare username with sesion_username
            result = config.model.delete_admin(nombre_admin) # call model delelete
            if result is None: # delete error
                message = "El registro no se puede borrar" # Error messate
                result = config.model.get_admin(nombre_admin) # get username data
                result.nombre_admin = config.make_secure_val(str(result.nombre_admin)) # apply HMAC to username
                return config.render.delete(result, message) # render delete.html again
            else: # user delete correctly
                raise config.web.seeother('/admin') # render index.html
        else: #  username and session_username its the same
            message = "No se puede elimiar el usuario activo" # Error message
            result = config.model.get_admin(nombre_admin) # get username data
            result.nombre_admin = config.make_secure_val(str(result.nombre_admin)) # apply HMAC to username
            return config.render.delete(result, message) # render delete.html