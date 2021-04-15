import config
import hashlib
import app

class Insert:

    def __init__(self):
        pass

    '''
    def GET(self):
        if app.session.loggedin is True:
            # session_username = app.session.username
            session_username = app.session.privilege  # get the session_privilege
            if session_username == 0: # admin user
                return self.GET_INSERT() # call GET_INSERT() function
            elif session_username == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    def POST(self):
        if app.session.loggedin is True: # validate if the user is logged
            # session_username = app.session.username
            session_username = app.session.privilege # get the session_privilege
            if session_username == 0: # admin user
                return self.POST_INSERT() # call POST_EDIT function
            elif privilege == 1: # guess user
                raise config.web.seeother('/guess') # render guess.html
        else: # the user dont have logged
            raise config.web.seeother('/login') # render login.html

    @staticmethod
    def GET_INSERT():

    @staticmethod
    def POST_INSERT():
    '''

    def GET(self):
        result = config.model.get_all_categorias().list() # get producto table list
        return config.render.insert(result) # render producto insert.html

    def POST(self):
        form = config.web.input() # get form data

        # call model insert_producto and try to insert new data
        config.model.insert_producto(
            form['idcategorias'],form['img_producto'],form['nom_producto'],form['precio_salida'],form['descripcion'],form['marca'],form['existencia'],form['status_prod'],
        )
        raise config.web.seeother('/producto') # render producto index.html
