import web
import config
import json


class Api_ingreso:
    def get(self, idingreso):
        try:
            # http://0.0.0.0:8080/api_ingreso?user_hash=12345&action=get
            if idingreso is None:
                result = config.model.get_all_ingreso()
                ingreso_json = []
                for row in result:
                    tmp = dict(row)
                    ingreso_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(ingreso_json)
            else:
                # http://0.0.0.0:8080/api_ingreso?user_hash=12345&action=get&idingreso=1
                result = config.model.get_ingreso(int(idingreso))
                ingreso_json = []
                ingreso_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(ingreso_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            ingreso_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ingreso_json)

# http://0.0.0.0:8080/api_ingreso?user_hash=12345&action=put&idingreso=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total):
        try:
            config.model.insert_ingreso(idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total)
            ingreso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ingreso_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_ingreso?user_hash=12345&action=delete&idingreso=1
    def delete(self, idingreso):
        try:
            config.model.delete_ingreso(idingreso)
            ingreso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ingreso_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_ingreso?user_hash=12345&action=update&idingreso=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idingreso, idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total):
        try:
            config.model.edit_ingreso(idingreso,idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total)
            ingreso_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ingreso_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            ingreso_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(ingreso_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idingreso=None,
            idproveedor=None,
            fecha_ingreso=None,
            tipo_comprobante=None,
            serie_comprobante=None,
            numero_comprobante=None,
            total=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idingreso=user_data.idingreso
            idproveedor=user_data.idproveedor
            fecha_ingreso=user_data.fecha_ingreso
            tipo_comprobante=user_data.tipo_comprobante
            serie_comprobante=user_data.serie_comprobante
            numero_comprobante=user_data.numero_comprobante
            total=user_data.total
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idingreso)
                elif action == 'put':
                    return self.put(idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total)
                elif action == 'delete':
                    return self.delete(idingreso)
                elif action == 'update':
                    return self.update(idingreso, idproveedor,fecha_ingreso,tipo_comprobante,serie_comprobante,numero_comprobante,total)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
