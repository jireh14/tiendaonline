import web
import config

db = config.db


def get_all_logs():
    try:
        return db.select('logs')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def insert_logs(nombre_admin,ip):
    try:
        return db.insert('logs',nombre_admin=nombre_admin, ip=ip)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None

