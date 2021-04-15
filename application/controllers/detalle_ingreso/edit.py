import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, iddetalle_ingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(iddetalle_ingreso) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, iddetalle_ingreso, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(iddetalle_ingreso) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(iddetalle_ingreso, **k):

    @staticmethod
    def POST_EDIT(iddetalle_ingreso, **k):
        
    '''

    def GET(self, iddetalle_ingreso, **k):
        message = None # Error message
        iddetalle_ingreso = config.check_secure_val(str(iddetalle_ingreso)) # HMAC iddetalle_ingreso validate
        result = config.model.get_detalle_ingreso(int(iddetalle_ingreso)) # search for the iddetalle_ingreso
        result.iddetalle_ingreso = config.make_secure_val(str(result.iddetalle_ingreso)) # apply HMAC for iddetalle_ingreso
        return config.render.edit(result, message) # render detalle_ingreso edit.html

    def POST(self, iddetalle_ingreso, **k):
        form = config.web.input()  # get form data
        form['iddetalle_ingreso'] = config.check_secure_val(str(form['iddetalle_ingreso'])) # HMAC iddetalle_ingreso validate
        # edit user with new data
        result = config.model.edit_detalle_ingreso(
            form['iddetalle_ingreso'],form['idingreso_fk'],form['idproducto_fk'],form['cantidad_pro'],form['precio_in'],
        )
        if result == None: # Error on udpate data
            iddetalle_ingreso = config.check_secure_val(str(iddetalle_ingreso)) # validate HMAC iddetalle_ingreso
            result = config.model.get_detalle_ingreso(int(iddetalle_ingreso)) # search for iddetalle_ingreso data
            result.iddetalle_ingreso = config.make_secure_val(str(result.iddetalle_ingreso)) # apply HMAC to iddetalle_ingreso
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/detalle_ingreso') # render detalle_ingreso index.html
