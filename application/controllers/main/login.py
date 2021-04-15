from . import config
import app
import hashlib
import web


class Login:
    def __init__(self):
        pass

    @staticmethod
    def GET(*a):
        message = None
        return config.render.login(message)

    @staticmethod
    def POST(*a):
        i = config.web.input()
        pwdhash = hashlib.md5(i.password + config.secret_key).hexdigest()
        check = config.model.validate_admin(i.nombre_admin, pwdhash)
        if check:
            app.session.loggedin = True
            app.session.nombre_admin = check['nombre_admin']
            app.session.privilege = check['privilege']
            change_pwd = check['change_pwd']

            print "Force pwd" + str(change_pwd)

            ip = web.ctx['ip']

            res = config.model_logs.insert_logs(check['nombre_admin'], ip)

            if check['status_admin'] == 0:
                message = "Usuario desactivado!!!!"
                return config.render.login(message)

            elif change_pwd == 1:
                print 'cambiar pwd'
                raise config.web.seeother('/admin/change_pwd')
            else:
                raise config.web.seeother('/')
        else:
            message = "Usuario o contrasena incorrectos!!!!"
            return config.render.login(message)
