import web
import config

db = config.db


def get_all_proveedor():
    try:
        return db.select('proveedor')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_proveedor(idproveedor):
    try:
        return db.select('proveedor', where='idproveedor=$idproveedor', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_proveedor(idproveedor):
    try:
        return db.delete('proveedor', where='idproveedor=$idproveedor', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_proveedor(nombre_pro,telefono_pro,correo_pro,status_prov):
    try:
        return db.insert('proveedor',nombre_pro=nombre_pro,
telefono_pro=telefono_pro,
correo_pro=correo_pro,
status_prov=status_prov)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_proveedor(idproveedor,nombre_pro,telefono_pro,correo_pro,status_prov):
    try:
        return db.update('proveedor',idproveedor=idproveedor,
nombre_pro=nombre_pro,
telefono_pro=telefono_pro,
correo_pro=correo_pro,
status_prov=status_prov,
                  where='idproveedor=$idproveedor',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
