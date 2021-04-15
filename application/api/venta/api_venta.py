import web
import config
import json


class Api_venta:
    def get(self, idventa):
        try:
            # http://0.0.0.0:8080/api_venta?user_hash=12345&action=get
            if idventa is None:
                result = config.model.get_all_venta()
                venta_json = []
                for row in result:
                    tmp = dict(row)
                    venta_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(venta_json)
            else:
                # http://0.0.0.0:8080/api_venta?user_hash=12345&action=get&idventa=1
                result = config.model.get_venta(int(idventa))
                venta_json = []
                venta_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(venta_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            venta_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(venta_json)

# http://0.0.0.0:8080/api_venta?user_hash=12345&action=put&idventa=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, idusuario,total,idformapago,fecha_venta):
        try:
            config.model.insert_venta(idusuario,total,idformapago,fecha_venta)
            venta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(venta_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_venta?user_hash=12345&action=delete&idventa=1
    def delete(self, idventa):
        try:
            config.model.delete_venta(idventa)
            venta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(venta_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_venta?user_hash=12345&action=update&idventa=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idventa, idusuario,total,idformapago,fecha_venta):
        try:
            config.model.edit_venta(idventa,idusuario,total,idformapago,fecha_venta)
            venta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(venta_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            venta_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(venta_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idventa=None,
            idusuario=None,
            total=None,
            idformapago=None,
            fecha_venta=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idventa=user_data.idventa
            idusuario=user_data.idusuario
            total=user_data.total
            idformapago=user_data.idformapago
            fecha_venta=user_data.fecha_venta
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idventa)
                elif action == 'put':
                    return self.put(idusuario,total,idformapago,fecha_venta)
                elif action == 'delete':
                    return self.delete(idventa)
                elif action == 'update':
                    return self.update(idventa, idusuario,total,idformapago,fecha_venta)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
