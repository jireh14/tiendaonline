
import web
import config

ssl = False #activate ssl certificate 

urls = (
    '/', 'application.controllers.main.index.Index',
    '/login', 'application.controllers.main.login.Login',
    '/logout', 'application.controllers.main.logout.Logout',
    
    '/admin', 'application.controllers.admin.index.Index',
    '/admin/view/(.+)', 'application.controllers.admin.view.View',
    '/admin/edit/(.+)', 'application.controllers.admin.edit.Edit',
    '/admin/delete/(.+)', 'application.controllers.admin.delete.Delete',
    '/admin/insert', 'application.controllers.admin.insert.Insert',

    '/proveedor', 'application.controllers.proveedor.index.Index',
    '/proveedor/view/(.+)', 'application.controllers.proveedor.view.View',
    '/proveedor/edit/(.+)', 'application.controllers.proveedor.edit.Edit',
    '/proveedor/delete/(.+)', 'application.controllers.proveedor.delete.Delete',
    '/proveedor/insert', 'application.controllers.proveedor.insert.Insert',
    
    '/categorias', 'application.controllers.categorias.index.Index',
    '/categorias/view/(.+)', 'application.controllers.categorias.view.View',
    '/categorias/edit/(.+)', 'application.controllers.categorias.edit.Edit',
    '/categorias/delete/(.+)', 'application.controllers.categorias.delete.Delete',
    '/categorias/insert', 'application.controllers.categorias.insert.Insert',

    '/producto', 'application.controllers.producto.index.Index',
    '/producto/view/(.+)', 'application.controllers.producto.view.View',
    '/producto/edit/(.+)', 'application.controllers.producto.edit.Edit',
    '/producto/delete/(.+)', 'application.controllers.producto.delete.Delete',
    '/producto/insert', 'application.controllers.producto.insert.Insert',

    '/ingreso', 'application.controllers.ingreso.index.Index',
    '/ingreso/view/(.+)', 'application.controllers.ingreso.view.View',
    '/ingreso/edit/(.+)', 'application.controllers.ingreso.edit.Edit',
    '/ingreso/delete/(.+)', 'application.controllers.ingreso.delete.Delete',
    '/ingreso/insert', 'application.controllers.ingreso.insert.Insert',

    '/detalle_ingreso', 'application.controllers.detalle_ingreso.index.Index',
    '/detalle_ingreso/view/(.+)', 'application.controllers.detalle_ingreso.view.View',
    '/detalle_ingreso/edit/(.+)', 'application.controllers.detalle_ingreso.edit.Edit',
    '/detalle_ingreso/delete/(.+)', 'application.controllers.detalle_ingreso.delete.Delete',
    '/detalle_ingreso/insert', 'application.controllers.detalle_ingreso.insert.Insert',

    '/venta', 'application.controllers.venta.index.Index',
    '/venta/view/(.+)', 'application.controllers.venta.view.View',
    '/venta/edit/(.+)', 'application.controllers.venta.edit.Edit',
    '/venta/delete/(.+)', 'application.controllers.venta.delete.Delete',
    '/venta/insert', 'application.controllers.venta.insert.Insert',

    '/detalle_venta', 'application.controllers.detalle_venta.index.Index',
    '/detalle_venta/view/(.+)', 'application.controllers.detalle_venta.view.View',
    '/detalle_venta/edit/(.+)', 'application.controllers.detalle_venta.edit.Edit',
    '/detalle_venta/delete/(.+)', 'application.controllers.detalle_venta.delete.Delete',
    '/detalle_venta/insert', 'application.controllers.detalle_venta.insert.Insert',

    '/logs', 'application.controllers.logs.index.Index',
    '/logs/printer', 'application.controllers.logs.printer.Printer',
    '/logs/view/(.+)', 'application.controllers.logs.view.View',

    #'/api_table_name/?', 'application.api.table_name.api_table_name.Api_table_name',
)

app = web.application(urls, globals())

if ssl is True:
    from web.wsgiserver import CherryPyWSGIServer
    CherryPyWSGIServer.ssl_certificate = "ssl/server.crt"
    CherryPyWSGIServer.ssl_private_key = "ssl/server.key"

if web.config.get('_session') is None:
    db = config.db
    store = web.session.DBStore(db, 'sessions')
    session = web.session.Session(
        app,
        store,
        initializer={
        'login': 0,
        'privilege': -1,
        'admin': 'anonymous',
        'loggedin': False,
        'count': 0
        }
        )
    web.config._session = session
    web.config.session_parameters['cookie_name'] = 'Ventas'
    web.config.session_parameters['timeout'] = 2000
    web.config.session_parameters['expired_message'] = 'Session expired'
    web.config.session_parameters['ignore_expiry'] = False
    web.config.session_parameters['ignore_change_ip'] = False
    web.config.session_parameters['secret_key'] = 'fLjUfxqXtfNoIldA0A0J'
else:
    session = web.config._session


class Count:
    def GET(self):
        session.count += 1
        return str(session.count)


def InternalError(): 
    raise config.web.seeother('/')


def NotFound():
    raise config.web.seeother('/')

if __name__ == "__main__":
    db.printing = False # hide db transactions
    web.config.debug = False # hide debug print
    web.config.db_printing = False # hide db transactions
    app.internalerror = InternalError
    app.notfound = NotFound
    app.run()
