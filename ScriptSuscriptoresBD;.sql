CREATE DATABASE suscriptoresdb;
SHOW DATABASES;
use suscriptoresdb;

CREATE TABLE suscriptores (
  telefono_celular VARCHAR(10) PRIMARY KEY,
  nombre VARCHAR(50) NOT NULL,
  apellido_materno VARCHAR(50) DEFAULT '',
  apellido_paterno VARCHAR(50) DEFAULT '',
  edad INT
);

INSERT INTO suscriptores (telefono_celular, nombre, apellido_materno, apellido_paterno, edad)
VALUES ('1234567890', 'Carlos', 'Beltrán', 'Bernal', 27);

SELECT * FROM suscriptores;

SELECT * FROM suscriptores WHERE telefono_celular = '1234567890';

UPDATE suscriptores
SET nombre = 'Eduardo', apellido_paterno = 'Martínez', edad = 30
WHERE telefono_celular = '1234567890';

DELETE FROM suscriptores
WHERE telefono_celular = '1234567890';

-- Procedimiento para Insertar un suscriptor
DELIMITER //
CREATE PROCEDURE InsertarSuscriptor(
    IN p_telefono_celular VARCHAR(10),
    IN p_nombre VARCHAR(50),
    IN p_apellido_materno VARCHAR(50),
    IN p_apellido_paterno VARCHAR(50),
    IN p_edad INT
)
BEGIN
    INSERT INTO suscriptores (telefono_celular, nombre, apellido_materno, apellido_paterno, edad)
    VALUES (p_telefono_celular, p_nombre, p_apellido_materno, p_apellido_paterno, p_edad);
END //
DELIMITER ;

-- Procedimiento para Consultar todos los suscriptores
DELIMITER //
CREATE PROCEDURE ConsultarSuscriptores()
BEGIN
    SELECT * FROM suscriptores;
END //
DELIMITER ;

-- Procedimiento para Consultar un suscriptor por telefono_celular
DELIMITER //
CREATE PROCEDURE ConsultarSuscriptor(
    IN p_telefono_celular VARCHAR(10)
)
BEGIN
    SELECT * FROM suscriptores WHERE telefono_celular = p_telefono_celular;
END //
DELIMITER ;

-- Procedimiento para Actualizar un suscriptor
DELIMITER //
CREATE PROCEDURE ActualizarSuscriptor(
    IN p_telefono_celular VARCHAR(10),
    IN p_nombre VARCHAR(50),
    IN p_apellido_materno VARCHAR(50),
    IN p_apellido_paterno VARCHAR(50),
    IN p_edad INT
)
BEGIN
    UPDATE suscriptores
    SET nombre = p_nombre, apellido_materno = p_apellido_materno, apellido_paterno = p_apellido_paterno, edad = p_edad
    WHERE telefono_celular = p_telefono_celular;
END //
DELIMITER ;

-- Procedimiento para Eliminar un suscriptor
DELIMITER //
CREATE PROCEDURE EliminarSuscriptor(
    IN p_telefono_celular VARCHAR(10)
)
BEGIN
    DELETE FROM suscriptores WHERE telefono_celular = p_telefono_celular;
END //
DELIMITER ;
