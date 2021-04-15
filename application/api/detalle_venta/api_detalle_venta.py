import web
import config
import json


class Api_detalle_venta:
    def get(self, iddetalle_venta):
        try:
            # http://0.0.0.0:8080/api_detalle_venta?user_hash=12345&action=get
            if iddetalle_venta is None:
                result = config.model.get_all_detalle_venta()
                detalle_venta_json = []
                for row in result:
                    tmp = dict(row)
                    detalle_venta_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(detalle_venta_json)
            else:
                # http://0.0.0.0:8080/api_detalle_venta?user_hash=12345&action=get&iddetalle_venta=1
                result = config.model.get_detalle_venta(int(iddetalle_venta))
                detalle_venta_json = []
                detalle_venta_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(detalle_venta_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            detalle_venta_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_venta_json)

# http://0.0.0.0:8080/api_detalle_venta?user_hash=12345&action=put&iddetalle_venta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, idventa,idproducto,cantidad,subtotal):
        try:
            config.model.insert_detalle_venta(idventa,idproducto,cantidad,subtotal)
            detalle_venta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_venta_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_detalle_venta?user_hash=12345&action=delete&iddetalle_venta=1
    def delete(self, iddetalle_venta):
        try:
            config.model.delete_detalle_venta(iddetalle_venta)
            detalle_venta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_venta_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_detalle_venta?user_hash=12345&action=update&iddetalle_venta=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, iddetalle_venta, idventa,idproducto,cantidad,subtotal):
        try:
            config.model.edit_detalle_venta(iddetalle_venta,idventa,idproducto,cantidad,subtotal)
            detalle_venta_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_venta_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            detalle_venta_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_venta_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            iddetalle_venta=None,
            idventa=None,
            idproducto=None,
            cantidad=None,
            subtotal=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            iddetalle_venta=user_data.iddetalle_venta
            idventa=user_data.idventa
            idproducto=user_data.idproducto
            cantidad=user_data.cantidad
            subtotal=user_data.subtotal
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(iddetalle_venta)
                elif action == 'put':
                    return self.put(idventa,idproducto,cantidad,subtotal)
                elif action == 'delete':
                    return self.delete(iddetalle_venta)
                elif action == 'update':
                    return self.update(iddetalle_venta, idventa,idproducto,cantidad,subtotal)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
