import web
import config

db = config.db


def get_all_formapago():
    try:
        return db.select('formapago')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_formapago(idformapago):
    try:
        return db.select('formapago', where='idformapago=$idformapago', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_formapago(idformapago):
    try:
        return db.delete('formapago', where='idformapago=$idformapago', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_formapago(efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip):
    try:
        return db.insert('formapago',efectivo=efectivo,
banco=banco,
nom_titular=nom_titular,
num_cuenta=num_cuenta,
num_tarjeta=num_tarjeta,
fecha_ven=fecha_ven,
nip=nip)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_formapago(idformapago,efectivo,banco,nom_titular,num_cuenta,num_tarjeta,fecha_ven,nip):
    try:
        return db.update('formapago',idformapago=idformapago,
efectivo=efectivo,
banco=banco,
nom_titular=nom_titular,
num_cuenta=num_cuenta,
num_tarjeta=num_tarjeta,
fecha_ven=fecha_ven,
nip=nip,
                  where='idformapago=$idformapago',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
