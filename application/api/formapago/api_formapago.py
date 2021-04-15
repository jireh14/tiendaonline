import web
import config
import json


class Api_formapago:
    def get(self, idformapago):
        try:
            # http://0.0.0.0:8080/api_formapago?user_hash=12345&action=get
            if idformapago is None:
                result = config.model.get_all_formapago()
                formapago_json = []
                for row in result:
                    tmp = dict(row)
                    formapago_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(formapago_json)
            else:
                # http://0.0.0.0:8080/api_formapago?user_hash=12345&action=get&idformapago=1
                result = config.model.get_formapago(int(idformapago))
                formapago_json = []
                formapago_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(formapago_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            formapago_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(formapago_json)

# http://0.0.0.0:8080/api_formapago?user_hash=12345&action=put&idformapago=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip):
        try:
            config.model.insert_formapago(efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip)
            formapago_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(formapago_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_formapago?user_hash=12345&action=delete&idformapago=1
    def delete(self, idformapago):
        try:
            config.model.delete_formapago(idformapago)
            formapago_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(formapago_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_formapago?user_hash=12345&action=update&idformapago=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idformapago, efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip):
        try:
            config.model.edit_formapago(idformapago,efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip)
            formapago_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(formapago_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            formapago_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(formapago_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idformapago=None,
            efectivo=None,
            banco=None,
            nom_titular=None,
            num_cuenta=None,
            num_tarjeta=None,
            fecha_ven=None,
            nip=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idformapago=user_data.idformapago
            efectivo=user_data.efectivo
            banco=user_data.banco
            nom_titular=user_data.nom_titular
            num_cuenta=user_data.num_cuenta
            num_tarjeta=user_data.num_tarjeta
            fecha_ven=user_data.fecha_ven
            nip=user_data.nip
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idformapago)
                elif action == 'put':
                    return self.put(efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip)
                elif action == 'delete':
                    return self.delete(idformapago)
                elif action == 'update':
                    return self.update(idformapago, efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
