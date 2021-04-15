import web
import config

db = config.db


def get_all_categorias():
    try:
        return db.select('categorias')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)

def get_all_producto():
    try:
        return db.select('pc')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_producto(idproducto):
    try:
        return db.select('producto', where='idproducto=$idproducto', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_producto(idproducto):
    try:
        return db.delete('producto', where='idproducto=$idproducto', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_producto(idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod):
    try:
        return db.insert('producto',idcategorias=idcategorias,
img_producto=img_producto,
nom_producto=nom_producto,
precio_salida=precio_salida,
descripcion=descripcion,
marca=marca,
existencia=existencia,
status_prod=status_prod)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_producto(idproducto,idcategorias,img_producto,nom_producto,precio_salida,descripcion,marca,existencia,status_prod):
    try:
        return db.update('producto',idproducto=idproducto,
idcategorias=idcategorias,
img_producto=img_producto,
nom_producto=nom_producto,
precio_salida=precio_salida,
descripcion=descripcion,
marca=marca,
existencia=existencia,
status_prod=status_prod,
                  where='idproducto=$idproducto',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
