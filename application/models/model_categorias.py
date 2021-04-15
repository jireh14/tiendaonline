import web
import config

db = config.db


def get_all_categorias():
    try:
        return db.select('categorias')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_categorias(idcategorias):
    try:
        return db.select('categorias', where='idcategorias=$idcategorias', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_categorias(idcategorias):
    try:
        return db.delete('categorias', where='idcategorias=$idcategorias', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_categorias(nombre_cat,descripcion_cat,status_cat):
    try:
        return db.insert('categorias',nombre_cat=nombre_cat,
descripcion_cat=descripcion_cat,
status_cat=status_cat)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_categorias(idcategorias,nombre_cat,descripcion_cat,status_cat):
    try:
        return db.update('categorias',idcategorias=idcategorias,
nombre_cat=nombre_cat,
descripcion_cat=descripcion_cat,
status_cat=status_cat,
                  where='idcategorias=$idcategorias',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
