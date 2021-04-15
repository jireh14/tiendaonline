import web
import config
import json


class Api_categorias:
    def get(self, idcategorias):
        try:
            # http://0.0.0.0:8080/api_categorias?user_hash=12345&action=get
            if idcategorias is None:
                result = config.model.get_all_categorias()
                categorias_json = []
                for row in result:
                    tmp = dict(row)
                    categorias_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(categorias_json)
            else:
                # http://0.0.0.0:8080/api_categorias?user_hash=12345&action=get&idcategorias=1
                result = config.model.get_categorias(int(idcategorias))
                categorias_json = []
                categorias_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(categorias_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            categorias_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(categorias_json)

# http://0.0.0.0:8080/api_categorias?user_hash=12345&action=put&idcategorias=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_cat,descripcion_cat,status_cat):
        try:
            config.model.insert_categorias(nombre_cat,descripcion_cat,status_cat)
            categorias_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(categorias_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_categorias?user_hash=12345&action=delete&idcategorias=1
    def delete(self, idcategorias):
        try:
            config.model.delete_categorias(idcategorias)
            categorias_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(categorias_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_categorias?user_hash=12345&action=update&idcategorias=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, idcategorias, nombre_cat,descripcion_cat,status_cat):
        try:
            config.model.edit_categorias(idcategorias,nombre_cat,descripcion_cat,status_cat)
            categorias_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(categorias_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            categorias_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(categorias_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            idcategorias=None,
            nombre_cat=None,
            descripcion_cat=None,
            status_cat=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            idcategorias=user_data.idcategorias
            nombre_cat=user_data.nombre_cat
            descripcion_cat=user_data.descripcion_cat
            status_cat=user_data.status_cat
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(idcategorias)
                elif action == 'put':
                    return self.put(nombre_cat,descripcion_cat,status_cat)
                elif action == 'delete':
                    return self.delete(idcategorias)
                elif action == 'update':
                    return self.update(idcategorias, nombre_cat,descripcion_cat,status_cat)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
