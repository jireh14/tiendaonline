import web
import config

db = config.db


def get_all_usuario():
    try:
        return db.select('usuario')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_usuario(idusuario):
    try:
        return db.select('usuario', where='idusuario=$idusuario', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_usuario(idusuario):
    try:
        return db.delete('usuario', where='idusuario=$idusuario', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_usuario(nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user):
    try:
        return db.insert('usuario',nombre=nombre,
apellidos=apellidos,
correo_usuario=correo_usuario,
contrasena=contrasena,
calle_num=calle_num,
colonia=colonia,
codigo_postal=codigo_postal,
ciudad=ciudad,
estado=estado,
referencias=referencias,
fecha_reg_usu=fecha_reg_usu,
status_user=status_user)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_usuario(idusuario,nombre,apellidos,correo_usuario,contrasena,calle_num,colonia,codigo_postal,ciudad,estado,referencias,fecha_reg_usu,status_user):
    try:
        return db.update('usuario',idusuario=idusuario,
nombre=nombre,
apellidos=apellidos,
correo_usuario=correo_usuario,
contrasena=contrasena,
calle_num=calle_num,
colonia=colonia,
codigo_postal=codigo_postal,
ciudad=ciudad,
estado=estado,
referencias=referencias,
fecha_reg_usu=fecha_reg_usu,
status_user=status_user,
                  where='idusuario=$idusuario',
                  vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None
