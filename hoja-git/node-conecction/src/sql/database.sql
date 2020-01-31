CREATE DATABASE formulario_gg;
USE formulario_gg;
CREATE TABLE formulario(
id_persona INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Cedula INT(100),
date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DESCRIBE formulario;
INSERT INTO formulario(Cedula) values('1026304241');
SELECT * FROM formulario;
-------------------------------------------------
CREATE DATABASE formulario_gg;
USE formulario_gg;
CREATE TABLE formulario(
id_persona INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Cedula INT(100),
date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DESCRIBE formulario;
INSERT INTO formulario(Cedula) values('1026304241');
SELECT * FROM formulario;
-----------------------------------------------------
CREATE DATABASE formulario_gg;
USE formulario_gg;
CREATE TABLE formulario(
id_persona INT NOT NULL  AUTO_INCREMENT,
Cedula INT(100),
Nombre VARCHAR(20),
Apellido VARCHAR(20),
Administrador BOOLEAN(20), 
Usuario VARCHAR(20),
Password VARCHAR(20),
PRIMARY KEY (id_persona),
FOREIGN KEY (Cargo_id)   REFERENCES Cargo    (id_Cargo),
date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
DESCRIBE formulario;
SELECT * FROM formulario;
--------------------------------------
CREATE DATABASE formulario_gg;
USE formulario_gg;
CREATE TABLE producto(
id_producto INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
Codigo VARCHAR (50),
Producto VARCHAR(20),
Tipo VARCHAR(20),
Cantidad INT,
Valor VARCHAR(20),
date_created TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);