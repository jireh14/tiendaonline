CREATE DATABASE web_admin;

USE web_admin;

CREATE TABLE admin(
    nombre_admin varchar(70) NOT NULL PRIMARY KEY,
    apellidos_admin varchar(150) NOT NULL,
    num_cuenta VARCHAR(18) NOT NULL,
    nombre_banco VARCHAR(60) NULL,
    tipo_tarjeta_admin VARCHAR(45) NULL,
    num_tarjeta VARCHAR(18) NOT NULL,
    telefono_admin VARCHAR(15) NULL,
    correo_admin VARCHAR(100) NOT NULL,
    password varchar(32) NOT NULL,
    privilege integer NOT NULL DEFAULT -1,
    user_hash varchar(32) NOT NULL,
    change_pwd integer NOT NULL DEFAULT 1,
    status_admin integer NOT NULL DEFAULT 1,
    created timestamp NOT NULL
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE sessions(
    session_id char(128) UNIQUE NOT NULL,
    atime timestamp NOT NULL default current_timestamp,
    data text
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

CREATE TABLE logs( 
    id_log integer NOT NULL PRIMARY KEY AUTO_INCREMENT,
    nombre_admin varchar(20) NOT NULL,
    ip varchar(16) NOT NULL,
    access timestamp NOT NULL,
    FOREIGN KEY (nombre_admin) REFERENCES admin(nombre_admin)
)ENGINE=InnoDB DEFAULT CHARSET=latin1;

INSERT INTO admin (nombre_admin, apellidos_admin, num_cuenta, nombre_banco, tipo_tarjeta_admin, num_tarjeta, telefono_admin,correo_admin, password, privilege, user_hash, change_pwd, status_admin )
VALUES ('Administrador','Yanet islas','123456789012','HSBC','DEBITO','123456789012','7751234567','admin@gmail.com', 'admin',0,'admin',0,1);

INSERT INTO admin (nombre_admin, apellidos_admin, num_cuenta, nombre_banco, tipo_tarjeta_admin, num_tarjeta, telefono_admin,correo_admin, password, privilege, user_hash, change_pwd, status_admin )
VALUES ('JirehA','Jireh Castillo','123456779015','HSBC','DEBITO','123456779015','7751292878','jireh@gmail.com', 'admin',0,'admin',0,1);

SELECT * FROM admin;
SELECT * FROM sessions;

CREATE TABLE IF NOT EXISTS usuario(
  idusuario INT NOT NULL AUTO_INCREMENT,
  nombre VARCHAR(100) NOT NULL,
  apellidos VARCHAR(100) NOT NULL,
  correo_usuario VARCHAR(100) NOT NULL,
  contrasena VARCHAR(100) NOT NULL,
  calle_num VARCHAR(60) NOT NULL,
  colonia VARCHAR(50) NOT NULL,
  codigo_postal VARCHAR(5) NOT NULL,
  ciudad VARCHAR(50) NOT NULL,
  estado VARCHAR(60) NOT NULL,
  referencias MEDIUMTEXT NULL,
  fecha_reg_usu TIMESTAMP NOT NULL,
  status_user TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (idusuario))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS categorias(
  idcategorias INT NOT NULL AUTO_INCREMENT,
  nombre_cat VARCHAR(50) NOT NULL,
  descripcion_cat MEDIUMTEXT NULL,
  status_cat TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (idcategorias))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS proveedor(
  idproveedor INT NOT NULL AUTO_INCREMENT,
  nombre_pro VARCHAR(100) NOT NULL,
  telefono_pro VARCHAR(15) NOT NULL,
  correo_pro VARCHAR(100) NOT NULL,
  status_prov TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (idproveedor))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS producto(
  idproducto INT NOT NULL AUTO_INCREMENT,
  idcategorias INT NOT NULL,
  img_producto VARCHAR(100) NOT NULL,
  nom_producto VARCHAR(100) NOT NULL,
  precio_salida FLOAT NOT NULL,
  descripcion MEDIUMTEXT NULL,
  marca VARCHAR(50) NULL,
  existencia INT NOT NULL,
  status_prod TINYINT NOT NULL DEFAULT 1,
  PRIMARY KEY (idproducto),
  CONSTRAINT idcategorias
    FOREIGN KEY (idcategorias)
    REFERENCES categorias (idcategorias)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS formapago(
  idformapago INT NOT NULL AUTO_INCREMENT,
  efectivo TINYINT NOT NULL,
  banco VARCHAR(60) NULL,
  nom_titular VARCHAR(100) NULL,
  num_cuenta VARCHAR(18) NULL,
  num_tarjeta VARCHAR(18) NULL,
  fecha_ven TIMESTAMP NOT NULL,
  nip VARCHAR(5) NULL,
  PRIMARY KEY (idformapago))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS venta(
  idventa INT NOT NULL AUTO_INCREMENT,
  idusuario INT NOT NULL,
  total FLOAT NOT NULL,
  idformapago INT NOT NULL,
  fecha_venta TIMESTAMP NOT NULL,
  PRIMARY KEY (idventa),
  CONSTRAINT idusuario
    FOREIGN KEY (idusuario)
    REFERENCES usuario (idusuario)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT idformapago
    FOREIGN KEY (idformapago)
    REFERENCES formapago (idformapago)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS detalle_venta(
  iddetalle_venta INT NOT NULL AUTO_INCREMENT,
  idventa INT NOT NULL,
  idproducto INT NOT NULL,
  cantidad INT NOT NULL,
  subtotal FLOAT NOT NULL,
  PRIMARY KEY (iddetalle_venta),
  CONSTRAINT idventa
    FOREIGN KEY (idventa)
    REFERENCES venta (idventa)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT idproducto
    FOREIGN KEY (idproducto)
    REFERENCES producto (idproducto)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


CREATE TABLE IF NOT EXISTS ingreso(
  idingreso INT NOT NULL AUTO_INCREMENT,
  idproveedor INT NOT NULL,
  fecha_ingreso TIMESTAMP NOT NULL,
  tipo_comprobante VARCHAR(100) NOT NULL,
  serie_comprobante VARCHAR(100) NULL,
  numero_comprobante VARCHAR(100) NULL,
  total FLOAT NOT NULL,
  PRIMARY KEY (idingreso),
  CONSTRAINT idproveedor
    FOREIGN KEY (idproveedor)
    REFERENCES proveedor (idproveedor)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS detalle_ingreso(
  iddetalle_ingreso INT AUTO_INCREMENT PRIMARY KEY,
  idingreso_fk INT NOT NULL,
  idproducto_fk INT NOT NULL,
  cantidad_pro INT NULL,
  precio_in FLOAT NOT NULL,
  CONSTRAINT idingreso_fk
    FOREIGN KEY (idingreso_fk)
    REFERENCES ingreso (idingreso),
  CONSTRAINT idproducto_fk
    FOREIGN KEY (idproducto_fk)
    REFERENCES producto (idproducto)
	 )ENGINE = InnoDB;
	 
CREATE trigger ALTAS AFTER INSERT on detalle_ingreso
for each row 
UPDATE producto set existencia = existencia + new.cantidad_pro where idproducto = new.idproducto_fk;


CREATE trigger BAJAS AFTER INSERT on detalle_venta
for each row 
UPDATE producto set existencia = existencia - new.cantidad where idproducto = new.idproducto;


/*CREATE USER 'admin'@'localhost' IDENTIFIED BY 'admin.2021';
GRANT ALL PRIVILEGES ON web_admin.* TO 'admin'@'localhost';
FLUSH PRIVILEGES;
*/

create view pc as
select producto.idproducto, producto.idcategorias, producto.img_producto, producto.nom_producto, producto.precio_salida, 
		producto.descripcion, producto.marca, producto.existencia, producto.status_prod,
		categorias.nombre_cat 
		FROM producto
		INNER JOIN categorias on producto.idcategorias = categorias.idcategorias;
		
select * from pc;

create view compras_prov as
select ingreso.idingreso, ingreso.idproveedor, ingreso.fecha_ingreso, 
			ingreso.tipo_comprobante, ingreso.serie_comprobante, ingreso.numero_comprobante, 
			ingreso.total, proveedor.nombre_pro
			FROM ingreso
			INNER JOIN proveedor on ingreso.idproveedor = proveedor.idproveedor;

create view compras_producto as
select detalle_ingreso.iddetalle_ingreso, detalle_ingreso.idingreso_fk, detalle_ingreso.idproducto_fk,
detalle_ingreso.cantidad_pro, detalle_ingreso.precio_in,
producto.nom_producto
from detalle_ingreso
inner join producto on detalle_ingreso.idproducto_fk = producto.idproducto;


create view ventas_producto as
select detalle_venta.iddetalle_venta, detalle_venta.idventa, detalle_venta.idproducto, detalle_venta.cantidad,
detalle_venta.subtotal, producto.nom_producto, producto.precio_salida
from detalle_venta
inner join producto on detalle_venta.idproducto=producto.idproducto;