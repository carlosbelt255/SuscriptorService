import pymysql
import json

# Configuración de conexión a la base de datos MySQL en AWS RDS
connection = pymysql.connect(
    host="suscriptoresdb.chq2iu6kycyy.us-east-2.rds.amazonaws.com",
    user="admin",
    password="C27cda6970_",
    db="suscriptoresdb",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

# Manejador principal para la función Lambda
def lambda_handler(event, context):
    # Obtiene el método HTTP del evento recibido
    http_method = event["httpMethod"]
    
    # Inicializa la respuesta para almacenar el resultado de la operación
    response = {}
    try:
        # Lógica según el tipo de operación CRUD
        if http_method == "POST":
            # Si solo se proporciona `telefono_celular`, se hace una consulta en lugar de crear un suscriptor
            body = json.loads(event["body"])
            if "telefono_celular" in body.get("suscriptor", {}) and len(body["suscriptor"]) == 1:
                # Consultar un suscriptor específico
                response = read_suscriptor(event)
            else:
                # Validación de datos de entrada para creación de suscriptor
                validation_response = validate_input(event)
                if validation_response:  # Si hay errores de validación, retornar la respuesta de error
                    return validation_response
                # Crear un nuevo suscriptor
                response = create_suscriptor(event)
        
        elif http_method == "GET":
            # Obtener todos los suscriptores
            response = read_all_suscriptores()
        
        elif http_method == "PUT":
            # Validación de datos de entrada para actualización
            validation_response = validate_input(event, is_update=True)
            if validation_response:  # Si hay errores de validación, retornar la respuesta de error
                return validation_response
            # Actualizar un suscriptor existente
            response = update_suscriptor(event)
        
        elif http_method == "DELETE":
            # Eliminar un suscriptor específico
            response = delete_suscriptor(event)
        
        else:
            # Manejo para métodos HTTP no soportados
            response = {
                "statusCode": 400,
                "body": json.dumps({"message": "Método HTTP no soportado"})
            }
    except Exception as e:
        # Manejo de errores generales en la ejecución de la función Lambda
        response = {
            "statusCode": 500,
            "body": json.dumps({"message": str(e)})
        }

    return response

# Validación de datos de entrada para creación o actualización de suscriptores
def validate_input(event, is_update=False):
    body = json.loads(event["body"])
    suscriptor = body.get("suscriptor", {})
    info_nombre = suscriptor.get("info_nombre", {})
    nombre = info_nombre.get("nombre")
    apellido_materno = info_nombre.get("apellido_materno", "")
    apellido_paterno = info_nombre.get("apellido_paterno", "")
    edad = suscriptor.get("edad")
    
    # Definir el teléfono celular según si es creación o actualización
    telefono_celular = body.get("telefono_celular") if is_update else suscriptor.get("telefono_celular")

    # Lista de errores de validación
    errores = []
    if not isinstance(nombre, str):
        errores.append("El nombre es obligatorio y debe ser un string.")
    if not isinstance(apellido_materno, str) or not isinstance(apellido_paterno, str):
        errores.append("Los apellidos deben ser strings.")
    if not isinstance(edad, int):
        errores.append("La edad debe ser un número entero.")
    if not isinstance(telefono_celular, str) or len(telefono_celular) != 10:
        errores.append("El telefono_celular debe ser un string de 10 dígitos.")
    
    if errores:
        # Si hay errores, retornar una respuesta de error con el detalle
        return {
            "statusCode": 400,
            "body": json.dumps({"errors": errores})
        }
    
    return None  # Indica que la validación pasó sin errores

# Función para crear un nuevo suscriptor en la base de datos
def create_suscriptor(event):
    body = json.loads(event["body"])["suscriptor"]
    info_nombre = body["info_nombre"]
    telefono_celular = body["telefono_celular"]
    nombre = info_nombre["nombre"]
    apellido_materno = info_nombre.get("apellido_materno", "")
    apellido_paterno = info_nombre.get("apellido_paterno", "")
    edad = body["edad"]
    
    # Inserción del nuevo suscriptor en la base de datos
    with connection.cursor() as cursor:
        sql = "INSERT INTO suscriptores (telefono_celular, nombre, apellido_materno, apellido_paterno, edad) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (telefono_celular, nombre, apellido_materno, apellido_paterno, edad))
        connection.commit()

    return {
        "statusCode": 201,
        "body": json.dumps({"message": "Suscriptor creado exitosamente"})
    }

# Función para leer un suscriptor específico
def read_suscriptor(event):
    body = json.loads(event["body"])
    telefono_celular = body["suscriptor"].get("telefono_celular")
    
    # Consulta del suscriptor en la base de datos
    with connection.cursor() as cursor:
        sql = "SELECT * FROM suscriptores WHERE telefono_celular = %s"
        cursor.execute(sql, (telefono_celular,))
        result = cursor.fetchone()
        if result:
            return {
                "statusCode": 200,
                "body": json.dumps(result)
            }
        else:
            return {
                "statusCode": 404,
                "body": json.dumps({"message": "Suscriptor no encontrado"})
            }

# Función para obtener todos los suscriptores en la base de datos
def read_all_suscriptores():
    with connection.cursor() as cursor:
        sql = "SELECT * FROM suscriptores"
        cursor.execute(sql)
        result = cursor.fetchall()
        return {
            "statusCode": 200,
            "body": json.dumps(result)
        }

# Función para actualizar un suscriptor en la base de datos
def update_suscriptor(event):
    body = json.loads(event["body"])
    telefono_celular = body["telefono_celular"]  # Identificación del suscriptor
    suscriptor = body["suscriptor"]
    info_nombre = suscriptor["info_nombre"]
    nombre = info_nombre.get("nombre")
    apellido_materno = info_nombre.get("apellido_materno", "")
    apellido_paterno = info_nombre.get("apellido_paterno", "")
    edad = suscriptor.get("edad")
    
    # Actualización de los datos del suscriptor en la base de datos
    with connection.cursor() as cursor:
        sql = """
        UPDATE suscriptores 
        SET nombre = %s, apellido_materno = %s, apellido_paterno = %s, edad = %s 
        WHERE telefono_celular = %s
        """
        cursor.execute(sql, (nombre, apellido_materno, apellido_paterno, edad, telefono_celular))
        connection.commit()
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Suscriptor actualizado exitosamente"})
    }

# Función para eliminar un suscriptor de la base de datos
def delete_suscriptor(event):
    body = json.loads(event["body"])
    telefono_celular = body["telefono_celular"]
    
    # Eliminación del suscriptor en la base de datos
    with connection.cursor() as cursor:
        sql = "DELETE FROM suscriptores WHERE telefono_celular = %s"
        cursor.execute(sql, (telefono_celular,))
        connection.commit()
    
    return {
        "statusCode": 200,
        "body": json.dumps({"message": "Suscriptor eliminado exitosamente"})
    }
