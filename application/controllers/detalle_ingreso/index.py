import config
import hashlib
import app

class Index:
    
    def __init__(self):
        pass
    '''
    def GET(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_privilege = app.session.privilege # get the session_privilege 
            if session_privilege == 0: # admin user
                return self.GET_INDEX() # call GET_INDEX() function
            elif session_privilege == 1: # guess user
                raise config.web.seeother('/guess') # rendner guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INDEX():
    '''

    
    def GET(self):
        result = config.model.get_all_detalle_ingreso().list() # get detalle_ingreso table list
        for row in result:
            row.iddetalle_ingreso = config.make_secure_val(str(row.iddetalle_ingreso)) # apply HMAC to iddetalle_ingreso (primary key)
        return config.render.index(result) # render detalle_ingreso index.html
