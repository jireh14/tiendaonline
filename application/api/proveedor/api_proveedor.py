import web
import config
import json


class Api_proveedor:
    def get(self, idproveedor):
        try:
            # http://0.0.0.0:8080/api_proveedor?user_hash=12345&action=get
            if idproveedor is None:
                result = config.model.get_all_proveedor()
                proveedor_json = []
                for row in result:
                    tmp = dict(row)
                    proveedor_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(proveedor_json)
            else:
                # http://0.0.0.0:8080/api_proveedor?user_hash=12345&action=get&idproveedor=1
                result = config.model.get_proveedor(int(idproveedor))
                proveedor_json = []
                proveedor_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(proveedor_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            proveedor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proveedor_json)

# http://0.0.0.0:8080/api_proveedor?user_hash=12345&action=put&idproveedor=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_pro,telefono_pro,correo_pro,status_prov):
        try:
            config.model.insert_proveedor(nombre_pro,telefono_pro,correo_pro,status_prov)
            proveedor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proveedor_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_proveedor?user_hash=12345&action=delete&idproveedor=1
    def delete(self, idproveedor):
        try:
            config.model.delete_proveedor(idproveedor)
            proveedor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proveedor_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_proveedor?user_hash=12345&action=update&idproveedor=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idproveedor, nombre_pro,telefono_pro,correo_pro,status_prov):
        try:
            config.model.edit_proveedor(idproveedor,nombre_pro,telefono_pro,correo_pro,status_prov)
            proveedor_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proveedor_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            proveedor_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(proveedor_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idproveedor=None,
            nombre_pro=None,
            telefono_pro=None,
            correo_pro=None,
            status_prov=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idproveedor=user_data.idproveedor
            nombre_pro=user_data.nombre_pro
            telefono_pro=user_data.telefono_pro
            correo_pro=user_data.correo_pro
            status_prov=user_data.status_prov
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idproveedor)
                elif action == 'put':
                    return self.put(nombre_pro,telefono_pro,correo_pro,status_prov)
                elif action == 'delete':
                    return self.delete(idproveedor)
                elif action == 'update':
                    return self.update(idproveedor, nombre_pro,telefono_pro,correo_pro,status_prov)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
