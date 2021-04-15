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

def get_all_detalle_venta():
    try:
        return db.select('ventas_producto')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_detalle_venta(iddetalle_venta):
    try:
        return db.select('detalle_venta', where='iddetalle_venta=$iddetalle_venta', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_detalle_venta(iddetalle_venta):
    try:
        return db.delete('detalle_venta', where='iddetalle_venta=$iddetalle_venta', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_detalle_venta(idventa,idproducto,cantidad,subtotal):
    try:
        return db.insert('detalle_venta',idventa=idventa,
idproducto=idproducto,
cantidad=cantidad,
subtotal=subtotal)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_detalle_venta(iddetalle_venta,idventa,idproducto,cantidad,subtotal):
    try:
        return db.update('detalle_venta',iddetalle_venta=iddetalle_venta,
idventa=idventa,
idproducto=idproducto,
cantidad=cantidad,
subtotal=subtotal,
                  where='iddetalle_venta=$iddetalle_venta',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
