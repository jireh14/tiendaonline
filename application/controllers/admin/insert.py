from . import config
import hashlib
import app

class Insert:
    
    def _init_(self):
        pass

    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
            session_admin = app.session.privilege  # get the session_privilege
            if session_admin == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_admin == 1: # guess user
                raise config.web.seeother('/') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_admin = app.session.privilege # get the session_privilege
            if session_admin == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif privilege == 1:
                raise config.web.seeother('/')
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():
        return config.render.insert() # render insert.html

    @staticmethod
    def POST_INSERT():
        form = config.web.input()  # get form data
        pwdhash = hashlib.md5(form.password + config.secret_key).hexdigest() # encrypt pwdhash
        user_hash = hashlib.md5(form.nombre_admin + config.secret_key).hexdigest() # encrypt user_hash

        # call model insert_users and try to insert new data
        config.model.insert_admin(
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
            user_hash,
            form['change_pwd'],
            form['status_admin']
            # always ask for change the default password
        )
        raise config.web.seeother('/') # render users index.html