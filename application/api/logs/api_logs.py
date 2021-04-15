import web
import config
import json


class Api_logs:
    def get(self, id_log):
        try:
            # http://0.0.0.0:8080/api_logs?user_hash=12345&action=get
            if id_log is None:
                result = config.model.get_all_logs()
                logs_json = []
                for row in result:
                    tmp = dict(row)
                    logs_json.append(tmp)
                web.header('Content-Type', 'application/json')
                return json.dumps(logs_json)
            else:
                # http://0.0.0.0:8080/api_logs?user_hash=12345&action=get&id_log=1
                result = config.model.get_logs(int(id_log))
                logs_json = []
                logs_json.append(dict(result))
                web.header('Content-Type', 'application/json')
                return json.dumps(logs_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            logs_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logs_json)

# http://0.0.0.0:8080/api_logs?user_hash=12345&action=put&id_log=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=0
    def put(self, nombre_admin,ip,access):
        try:
            config.model.insert_logs(nombre_admin,ip,access)
            logs_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logs_json)
        except Exception as e:
            print "PUT Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_logs?user_hash=12345&action=delete&id_log=1
    def delete(self, id_log):
        try:
            config.model.delete_logs(id_log)
            logs_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logs_json)
        except Exception as e:
            print "DELETE Error {}".format(e.args)
            return None

# http://0.0.0.0:8080/api_logs?user_hash=12345&action=update&id_log=1&product=nuevo&description=nueva&stock=10&purchase_price=1&price_sale=3&product_image=default.jpg
    def update(self, id_log, nombre_admin,ip,access):
        try:
            config.model.edit_logs(id_log,nombre_admin,ip,access)
            logs_json = '[{200}]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logs_json)
        except Exception as e:
            print "GET Error {}".format(e.args)
            logs_json = '[]'
            web.header('Content-Type', 'application/json')
            return json.dumps(logs_json)

    def GET(self):
        user_data = web.input(
            user_hash=None,
            action=None,
            id_log=None,
            nombre_admin=None,
            ip=None,
            access=None,
        )
        try:
            user_hash = user_data.user_hash  # user validation
            action = user_data.action  # action GET, PUT, DELETE, UPDATE
            id_log=user_data.id_log
            nombre_admin=user_data.nombre_admin
            ip=user_data.ip
            access=user_data.access
            # user_hash
            if user_hash == '12345':
                if action is None:
                    raise web.seeother('/404')
                elif action == 'get':
                    return self.get(id_log)
                elif action == 'put':
                    return self.put(nombre_admin,ip,access)
                elif action == 'delete':
                    return self.delete(id_log)
                elif action == 'update':
                    return self.update(id_log, nombre_admin,ip,access)
            else:
                raise web.seeother('/404')
        except Exception as e:
            print "WEBSERVICE Error {}".format(e.args)
            raise web.seeother('/404')
