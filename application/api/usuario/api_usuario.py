import web
import config
import json


class Api_usuario:
    def get(self, idusuario):
        try:
            # http://0.0.0.0:8080/api_usuario?user_hash=12345&action=get
            if idusuario is None:
                result = config.model.get_all_usuario()
                usuario_json = []
                for row in result:
                    tmp = dict(row)
                    usuario_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(usuario_json)
            else:
                # http://0.0.0.0:8080/api_usuario?user_hash=12345&action=get&idusuario=1
                result = config.model.get_usuario(int(idusuario))
                usuario_json = []
                usuario_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(usuario_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuario_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)

# http://0.0.0.0:8080/api_usuario?user_hash=12345&action=put&idusuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user):
        try:
            config.model.insert_usuario(nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user)
            usuario_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuario?user_hash=12345&action=delete&idusuario=1
    def delete(self, idusuario):
        try:
            config.model.delete_usuario(idusuario)
            usuario_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_usuario?user_hash=12345&action=update&idusuario=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idusuario, nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user):
        try:
            config.model.edit_usuario(idusuario,nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user)
            usuario_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            usuario_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(usuario_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idusuario=None,
            nombre=None,
            apellidos=None,
            correo_usuario=None,
            contrasena=None,
            calle_num=None,
            colonia=None,
            codigo_postal=None,
            ciudad=None,
            estado=None,
            referencias=None,
            fecha_reg_usu=None,
            status_user=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idusuario=user_data.idusuario
            nombre=user_data.nombre
            apellidos=user_data.apellidos
            correo_usuario=user_data.correo_usuario
            contrasena=user_data.contrasena
            calle_num=user_data.calle_num
            colonia=user_data.colonia
            codigo_postal=user_data.codigo_postal
            ciudad=user_data.ciudad
            estado=user_data.estado
            referencias=user_data.referencias
            fecha_reg_usu=user_data.fecha_reg_usu
            status_user=user_data.status_user
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idusuario)
                elif action == 'put':
                    return self.put(nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user)
                elif action == 'delete':
                    return self.delete(idusuario)
                elif action == 'update':
                    return self.update(idusuario, nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
