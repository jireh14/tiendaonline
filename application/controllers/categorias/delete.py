import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, idcategorias, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idcategorias) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idcategorias, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idcategorias) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(idcategorias, **k):

    @staticmethod
    def POST_DELETE(idcategorias, **k):
    '''

    def GET(self, idcategorias, **k):
        message = None # Error message
        idcategorias = config.check_secure_val(str(idcategorias)) # HMAC idcategorias validate
        result = config.model.get_categorias(int(idcategorias)) # search  idcategorias
        result.idcategorias = config.make_secure_val(str(result.idcategorias)) # apply HMAC for idcategorias
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, idcategorias, **k):
        form = config.web.input() # get form data
        form['idcategorias'] = config.check_secure_val(str(form['idcategorias'])) # HMAC idcategorias validate
        result = config.model.delete_categorias(form['idcategorias']) # get categorias data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idcategorias = config.check_secure_val(str(idcategorias))  # HMAC user validate
            idcategorias = config.check_secure_val(str(idcategorias))  # HMAC user validate
            result = config.model.get_categorias(int(idcategorias)) # get idcategorias data
            result.idcategorias = config.make_secure_val(str(result.idcategorias)) # apply HMAC to idcategorias
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/categorias') # render categorias delete.html 
