import config
import hashlib
import app

class Delete:
    
    def __init__(self):
        pass

    '''
    def GET(self, iddetalle_ingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_DELETE(iddetalle_ingreso) # call GET_DELETE function
            elif privsession_privilegeilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, iddetalle_ingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege
            if session_privilege == 0: # admin user
                return self.POST_DELETE(iddetalle_ingreso) # call POST_DELETE function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_DELETE(iddetalle_ingreso, **k):

    @staticmethod
    def POST_DELETE(iddetalle_ingreso, **k):
    '''

    def GET(self, iddetalle_ingreso, **k):
        message = None # Error message
        iddetalle_ingreso = config.check_secure_val(str(iddetalle_ingreso)) # HMAC iddetalle_ingreso validate
        result = config.model.get_detalle_ingreso(int(iddetalle_ingreso)) # search  iddetalle_ingreso
        result.iddetalle_ingreso = config.make_secure_val(str(result.iddetalle_ingreso)) # apply HMAC for iddetalle_ingreso
        return config.render.delete(result, message) # render delete.html with user data

    def POST(self, iddetalle_ingreso, **k):
        form = config.web.input() # get form data
        form['iddetalle_ingreso'] = config.check_secure_val(str(form['iddetalle_ingreso'])) # HMAC iddetalle_ingreso validate
        result = config.model.delete_detalle_ingreso(form['iddetalle_ingreso']) # get detalle_ingreso data
        if result is None: # delete error
            message = "El registro no se puede borrar" # Error messate
            iddetalle_ingreso = config.check_secure_val(str(iddetalle_ingreso))  # HMAC user validate
            iddetalle_ingreso = config.check_secure_val(str(iddetalle_ingreso))  # HMAC user validate
            result = config.model.get_detalle_ingreso(int(iddetalle_ingreso)) # get iddetalle_ingreso data
            result.iddetalle_ingreso = config.make_secure_val(str(result.iddetalle_ingreso)) # apply HMAC to iddetalle_ingreso
            return config.render.delete(result, message) # render delete.html again
        else:
            raise config.web.seeother('/detalle_ingreso') # render detalle_ingreso delete.html 
