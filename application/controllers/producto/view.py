import config
import hashlib
import app


class View:

    def __init__(self):
        pass

    '''
    def GET(self, idproducto):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege
            if session_privilege == 0: # admin user
                return self.GET_VIEW(idproducto) # call GET_VIEW() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_VIEW(idproducto):
    '''

    def GET(self, idproducto):
        idproducto = config.check_secure_val(str(idproducto)) # HMAC idproducto validate
        result = config.model.get_producto(idproducto) # search for the idproducto data
        return config.render.view(result) # render view.html with idproducto data
