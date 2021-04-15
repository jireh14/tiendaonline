import web
import config

db = config.db

def get_all_producto():
    try:
        return db.select('producto')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None

def get_all_detalle_ingreso():
    try:
        return db.select('compras_producto')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_detalle_ingreso(iddetalle_ingreso):
    try:
        return db.select('detalle_ingreso', where='iddetalle_ingreso=$iddetalle_ingreso', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_detalle_ingreso(iddetalle_ingreso):
    try:
        return db.delete('detalle_ingreso', where='iddetalle_ingreso=$iddetalle_ingreso', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_detalle_ingreso(idingreso_fk,idproducto_fk,cantidad_pro,precio_in):
    try:
        return db.insert('detalle_ingreso',idingreso_fk=idingreso_fk,
idproducto_fk=idproducto_fk,
cantidad_pro=cantidad_pro,
precio_in=precio_in)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_detalle_ingreso(iddetalle_ingreso,idingreso_fk,idproducto_fk,cantidad_pro,precio_in):
    try:
        return db.update('detalle_ingreso',iddetalle_ingreso=iddetalle_ingreso,
idingreso_fk=idingreso_fk,
idproducto_fk=idproducto_fk,
cantidad_pro=cantidad_pro,
precio_in=precio_in,
                  where='iddetalle_ingreso=$iddetalle_ingreso',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
