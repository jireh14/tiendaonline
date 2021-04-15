import web
import config
import json


class Api_admin:
    def get(self, nombre_admin):
        try:
            # http://0.0.0.0:8080/api_admin?user_hash=12345&action=get
            if nombre_admin is None:
                result = config.model.get_all_admin()
                admin_json = []
                for row in result:
                    tmp = dict(row)
                    admin_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(admin_json)
            else:
                # http://0.0.0.0:8080/api_admin?user_hash=12345&action=get&nombre_admin=1
                result = config.model.get_admin(int(nombre_admin))
                admin_json = []
                admin_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(admin_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            admin_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(admin_json)

# http://0.0.0.0:8080/api_admin?user_hash=12345&action=put&nombre_admin=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin,created):
        try:
            config.model.insert_admin(apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin,created)
            admin_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(admin_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_admin?user_hash=12345&action=delete&nombre_admin=1
    def delete(self, nombre_admin):
        try:
            config.model.delete_admin(nombre_admin)
            admin_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(admin_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_admin?user_hash=12345&action=update&nombre_admin=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, nombre_admin, apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin,created):
        try:
            config.model.edit_admin(nombre_admin,apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin,created)
            admin_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(admin_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            admin_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(admin_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            nombre_admin=None,
            apellidos_admin=None,
            num_cuenta=None,
            nombre_banco=None,
            tipo_tarjeta_admin=None,
            num_tarjeta=None,
            telefono_admin=None,
            correo_admin=None,
            password=None,
            privilege=None,
            user_hash=None,
            change_pwd=None,
            status_admin=None,
            created=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            nombre_admin=user_data.nombre_admin
            apellidos_admin=user_data.apellidos_admin
            num_cuenta=user_data.num_cuenta
            nombre_banco=user_data.nombre_banco
            tipo_tarjeta_admin=user_data.tipo_tarjeta_admin
            num_tarjeta=user_data.num_tarjeta
            telefono_admin=user_data.telefono_admin
            correo_admin=user_data.correo_admin
            password=user_data.password
            privilege=user_data.privilege
            user_hash=user_data.user_hash
            change_pwd=user_data.change_pwd
            status_admin=user_data.status_admin
            created=user_data.created
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(nombre_admin)
                elif action == 'put':
                    return self.put(apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin,created)
                elif action == 'delete':
                    return self.delete(nombre_admin)
                elif action == 'update':
                    return self.update(nombre_admin, apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin,created)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
