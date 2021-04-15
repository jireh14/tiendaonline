import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, idformapago, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(idformapago) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idformapago, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(idformapago) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(idformapago, **k):

    @staticmethod
    def POST_EDIT(idformapago, **k):
        
    '''

    def GET(self, idformapago, **k):
        message = None # Error message
        idformapago = config.check_secure_val(str(idformapago)) # HMAC idformapago validate
        result = config.model.get_formapago(int(idformapago)) # search for the idformapago
        result.idformapago = config.make_secure_val(str(result.idformapago)) # apply HMAC for idformapago
        return config.render.edit(result, message) # render formapago edit.html

    def POST(self, idformapago, **k):
        form = config.web.input()  # get form data
        form['idformapago'] = config.check_secure_val(str(form['idformapago'])) # HMAC idformapago validate
        # edit user with new data
        result = config.model.edit_formapago(
            form['idformapago'],form['efectivo'],form['banco'],form['nom_titular'],form['num_cuenta'],form['num_tarjeta'],form['fecha_ven'],form['nip'],
        )
        if result == None: # Error on udpate data
            idformapago = config.check_secure_val(str(idformapago)) # validate HMAC idformapago
            result = config.model.get_formapago(int(idformapago)) # search for idformapago data
            result.idformapago = config.make_secure_val(str(result.idformapago)) # apply HMAC to idformapago
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/formapago') # render formapago index.html
