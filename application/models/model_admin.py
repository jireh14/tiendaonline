import web
from . import config

db = config.db

def validate_admin(nombre_admin, password):
    try:
        # select * from admin where nombre_admin=$nombre_admin and password=$password;
        return db.select('admin', 
            where='nombre_admin=$nombre_admin and password=$password', vars=locals())[0]
    except Exception as e:
        print(("Model get all Error {}".format(e.args)))
        print(("Model get all Message {}".format(e.message)))
        return None
        
def get_all_admin():
    try:
        return db.select('admin')
    except Exception as e:
        print "Model get all Error {}".format(e.args)
        print "Model get all Message {}".format(e.message)
        return None


def get_admin(nombre_admin):
    try:
        return db.select('admin', where='nombre_admin=$nombre_admin', vars=locals())[0]
    except Exception as e:
        print "Model get Error {}".format(e.args)
        print "Model get Message {}".format(e.message)
        return None


def delete_admin(nombre_admin):
    try:
        return db.delete('admin', where='nombre_admin=$nombre_admin', vars=locals())
    except Exception as e:
        print "Model delete Error {}".format(e.args)
        print "Model delete Message {}".format(e.message)
        return None


def insert_admin(nombre_admin,apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin):
    try:
        db.insert('admin',
            nombre_admin=nombre_admin,
            apellidos_admin=apellidos_admin,
            num_cuenta=num_cuenta,
            nombre_banco=nombre_banco,
            tipo_tarjeta_admin=tipo_tarjeta_admin,
            num_tarjeta=num_tarjeta,
            telefono_admin=telefono_admin,
            correo_admin=correo_admin,
            password=password,
            privilege=privilege,
            user_hash=user_hash,
            change_pwd=change_pwd,
            status_admin=status_admin)
    except Exception as e:
        print "Model insert Error {}".format(e.args)
        print "Model insert Message {}".format(e.message)
        return None


def edit_admin(nombre_admin,apellidos_admin,num_cuenta,nombre_banco,tipo_tarjeta_admin,num_tarjeta,telefono_admin,correo_admin,password,privilege,user_hash,change_pwd,status_admin):
    try:
        return db.update('admin',
            nombre_admin=nombre_admin,
            apellidos_admin=apellidos_admin,
            num_cuenta=num_cuenta,
            nombre_banco=nombre_banco,
            tipo_tarjeta_admin=tipo_tarjeta_admin,
            num_tarjeta=num_tarjeta,
            telefono_admin=telefono_admin,
            correo_admin=correo_admin,
            password=password,
            privilege=privilege,
            user_hash=user_hash,
            change_pwd=change_pwd,
            status_admin=status_admin,
            
            where='nombre_admin=$nombre_admin',
            vars=locals())
    except Exception as e:
        print "Model update Error {}".format(e.args)
        print "Model updateMessage {}".format(e.message)
        return None

def update_password(nombre_admin, password, change_pwd):
    try:
        # update users set username=$username, password=$password, change_pwd=$change_pwd where username=$username;
        return db.update('admin',
            nombre_admin=nombre_admin,
            password=password,
            change_pwd = change_pwd,

            where='nombre_admin=$nombre_admin',
            vars=locals())
    except Exception as e:
        print("Model update Error {}".format(e.args))
        print("Model updateMessage {}".format(e.message))
        return None