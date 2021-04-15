import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, idproveedor, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(idproveedor) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idproveedor, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(idproveedor) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(idproveedor, **k):

    @staticmethod
    def POST_DELETE(idproveedor, **k):
    '''

    def GET(self, idproveedor, **k):
        message = None # Error message
        idproveedor = config.check_secure_val(str(idproveedor)) # HMAC idproveedor validate
        result = config.model.get_proveedor(int(idproveedor)) # search  idproveedor
        result.idproveedor = config.make_secure_val(str(result.idproveedor)) # apply HMAC for idproveedor
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, idproveedor, **k):
        form = config.web.input() # get form data
        form['idproveedor'] = config.check_secure_val(str(form['idproveedor'])) # HMAC idproveedor validate
        result = config.model.delete_proveedor(form['idproveedor']) # get proveedor data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            idproveedor = config.check_secure_val(str(idproveedor))  # HMAC user validate
            idproveedor = config.check_secure_val(str(idproveedor))  # HMAC user validate
            result = config.model.get_proveedor(int(idproveedor)) # get idproveedor data
            result.idproveedor = config.make_secure_val(str(result.idproveedor)) # apply HMAC to idproveedor
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/proveedor') # render proveedor delete.html 
