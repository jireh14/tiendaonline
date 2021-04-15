import config
import hashlib
import app

class Edit:
    
    def __init__(self):
        pass

    '''
    def GET(self, idproducto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_EDIT(idproducto) # call GET_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self, idproducto, **k):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.POST_EDIT(idproducto) # call POST_EDIT function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_EDIT(idproducto, **k):

    @staticmethod
    def POST_EDIT(idproducto, **k):
        
    '''

    def GET(self, idproducto, **k):
        message = None # Error message
        idproducto = config.check_secure_val(str(idproducto)) # HMAC idproducto validate
        result = config.model.get_producto(int(idproducto)) # search for the idproducto
        result.idproducto = config.make_secure_val(str(result.idproducto)) # apply HMAC for idproducto
        categories = config.model.get_all_categorias().list()
        return config.render.edit(result, message, categories) # render producto edit.html

    def POST(self, idproducto, **k):
        form = config.web.input()  # get form data
        form['idproducto'] = config.check_secure_val(str(form['idproducto'])) # HMAC idproducto validate
        # edit user with new data
        result = config.model.edit_producto(
            form['idproducto'],form['idcategorias'],form['img_producto'],form['nom_producto'],form['precio_salida'],form['descripcion'],form['marca'],form['existencia'],form['status_prod'],
        )
        if result == None: # Error on udpate data
            idproducto = config.check_secure_val(str(idproducto)) # validate HMAC idproducto
            result = config.model.get_producto(int(idproducto)) # search for idproducto data
            result.idproducto = config.make_secure_val(str(result.idproducto)) # apply HMAC to idproducto
            message = "Error al editar el registro" # Error message
            return config.render.edit(result, message) # render edit.html again
        else: # update user data succefully
            raise config.web.seeother('/producto') # render producto index.html
