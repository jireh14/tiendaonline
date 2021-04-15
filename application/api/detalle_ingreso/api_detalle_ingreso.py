import web
import config
import json


class Api_detalle_ingreso:
    def get(self, iddetalle_ingreso):
        try:
            # http://0.0.0.0:8080/api_detalle_ingreso?user_hash=12345&action=get
            if iddetalle_ingreso is None:
                result = config.model.get_all_detalle_ingreso()
                detalle_ingreso_json = []
                for row in result:
                    tmp = dict(row)
                    detalle_ingreso_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(detalle_ingreso_json)
            else:
                # http://0.0.0.0:8080/api_detalle_ingreso?user_hash=12345&action=get&iddetalle_ingreso=1
                result = config.model.get_detalle_ingreso(int(iddetalle_ingreso))
                detalle_ingreso_json = []
                detalle_ingreso_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(detalle_ingreso_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            detalle_ingreso_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_ingreso_json)

# http://0.0.0.0:8080/api_detalle_ingreso?user_hash=12345&action=put&iddetalle_ingreso=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, idingreso_fk,idproducto_fk,cantidad_pro,precio_in):
        try:
            config.model.insert_detalle_ingreso(idingreso_fk,idproducto_fk,cantidad_pro,precio_in)
            detalle_ingreso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_ingreso_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_detalle_ingreso?user_hash=12345&action=delete&iddetalle_ingreso=1
    def delete(self, iddetalle_ingreso):
        try:
            config.model.delete_detalle_ingreso(iddetalle_ingreso)
            detalle_ingreso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_ingreso_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_detalle_ingreso?user_hash=12345&action=update&iddetalle_ingreso=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, iddetalle_ingreso, idingreso_fk,idproducto_fk,cantidad_pro,precio_in):
        try:
            config.model.edit_detalle_ingreso(iddetalle_ingreso,idingreso_fk,idproducto_fk,cantidad_pro,precio_in)
            detalle_ingreso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_ingreso_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            detalle_ingreso_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(detalle_ingreso_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            iddetalle_ingreso=None,
            idingreso_fk=None,
            idproducto_fk=None,
            cantidad_pro=None,
            precio_in=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            iddetalle_ingreso=user_data.iddetalle_ingreso
            idingreso_fk=user_data.idingreso_fk
            idproducto_fk=user_data.idproducto_fk
            cantidad_pro=user_data.cantidad_pro
            precio_in=user_data.precio_in
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(iddetalle_ingreso)
                elif action == 'put':
                    return self.put(idingreso_fk,idproducto_fk,cantidad_pro,precio_in)
                elif action == 'delete':
                    return self.delete(iddetalle_ingreso)
                elif action == 'update':
                    return self.update(iddetalle_ingreso, idingreso_fk,idproducto_fk,cantidad_pro,precio_in)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
