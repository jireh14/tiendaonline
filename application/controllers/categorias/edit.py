import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, idcategorias, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(idcategorias) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idcategorias, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(idcategorias) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(idcategorias, **k):

    @staticmethod
    def POST_EDIT(idcategorias, **k):
        
    '''

    def GET(self, idcategorias, **k):
        message = None # Error message
        idcategorias = config.check_secure_val(str(idcategorias)) # HMAC idcategorias validate
        result = config.model.get_categorias(int(idcategorias)) # search for the idcategorias
        result.idcategorias = config.make_secure_val(str(result.idcategorias)) # apply HMAC for idcategorias
        return config.render.edit(result, message) # render categorias edit.html

    def POST(self, idcategorias, **k):
        form = config.web.input()  # get form data
        form['idcategorias'] = config.check_secure_val(str(form['idcategorias'])) # HMAC idcategorias validate
        # edit user with new data
        result = config.model.edit_categorias(
            form['idcategorias'],form['nombre_cat'],form['descripcion_cat'],form['status_cat'],
        )
        if result == None: # Error on udpate data
            idcategorias = config.check_secure_val(str(idcategorias)) # validate HMAC idcategorias
            result = config.model.get_categorias(int(idcategorias)) # search for idcategorias data
            result.idcategorias = config.make_secure_val(str(result.idcategorias)) # apply HMAC to idcategorias
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/categorias') # render categorias index.html
