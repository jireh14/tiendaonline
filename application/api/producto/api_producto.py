import web
import config
import json


class Api_producto:
    def get(self, idproducto):
        try:
            # http://0.0.0.0:8080/api_producto?user_hash=12345&action=get
            if idproducto is None:
                result = config.model.get_all_producto()
                producto_json = []
                for row in result:
                    tmp = dict(row)
                    producto_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(producto_json)
            else:
                # http://0.0.0.0:8080/api_producto?user_hash=12345&action=get&idproducto=1
                result = config.model.get_producto(int(idproducto))
                producto_json = []
                producto_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(producto_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            producto_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)

# http://0.0.0.0:8080/api_producto?user_hash=12345&action=put&idproducto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod):
        try:
            config.model.insert_producto(idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod)
            producto_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_producto?user_hash=12345&action=delete&idproducto=1
    def delete(self, idproducto):
        try:
            config.model.delete_producto(idproducto)
            producto_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_producto?user_hash=12345&action=update&idproducto=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idproducto, idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod):
        try:
            config.model.edit_producto(idproducto,idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod)
            producto_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            producto_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(producto_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idproducto=None,
            idcategorias=None,
            img_producto=None,
            nom_producto=None,
            precio_salida=None,
            descripcion=None,
            marca=None,
            existencia=None,
            status_prod=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idproducto=user_data.idproducto
            idcategorias=user_data.idcategorias
            img_producto=user_data.img_producto
            nom_producto=user_data.nom_producto
            precio_salida=user_data.precio_salida
            descripcion=user_data.descripcion
            marca=user_data.marca
            existencia=user_data.existencia
            status_prod=user_data.status_prod
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idproducto)
                elif action == 'put':
                    return self.put(idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod)
                elif action == 'delete':
                    return self.delete(idproducto)
                elif action == 'update':
                    return self.update(idproducto, idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
