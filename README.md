# API de Suscriptores

Esta API ofrece un conjunto de servicios para gestionar un registro de suscriptores almacenado en una base de datos MySQL alojada en AWS RDS. Implementada en una función Lambda en AWS, esta API permite realizar operaciones CRUD (crear, leer, actualizar y eliminar) para administrar suscriptores de forma remota y eficiente. Se expone a través de API Gateway, lo que facilita el acceso a los endpoints y asegura una escalabilidad adecuada.

## Funcionalidad de la API

### Operaciones CRUD soportadas

1. **Buscar suscriptor por número de celular**: Consulta a la base de datos para obtener los datos de un suscriptor específico usando su número de celular como identificador único.
2. **Obtener lista de todos los suscriptores**: Recupera todos los registros de suscriptores almacenados en la base de datos.
3. **Registrar un nuevo suscriptor**: Permite agregar un nuevo suscriptor al sistema, validando que todos los campos necesarios estén completos y en el formato correcto.
4. **Modificar un suscriptor**: Actualiza la información de un suscriptor específico basado en el número de celular proporcionado.
5. **Eliminar un suscriptor**: Elimina el registro de un suscriptor específico identificado por su número de celular.

### Estructura de Respuestas

- **Códigos de respuesta HTTP**: Se utilizan códigos como `200` para éxito, `201` para creación de recurso, `400` para errores en los datos de entrada y `500` para errores internos.
- **Mensajes JSON**: Las respuestas se estructuran en formato JSON para facilitar la interpretación y la integración con otras aplicaciones.

---

## Requerimientos del Sistema

### AWS

1. **AWS RDS**: Configura una instancia de MySQL con las credenciales necesarias y acceso adecuado para la Lambda.
2. **AWS Lambda**: Función que alberga el código de la API, con las siguientes configuraciones:
   - **Memory**: Ajustar según las necesidades de procesamiento, generalmente 128-256 MB son suficientes para este tipo de operaciones.
   - **Timeout**: Aproximadamente 10 segundos, considerando tiempos de espera de red y consultas.
3. **AWS API Gateway**: API REST configurada para recibir solicitudes y redirigirlas a la Lambda, con configuración de métodos HTTP y habilitación de CORS si es necesario.

### Dependencias

- **Python**: La función Lambda debe utilizar Python 3.8 o superior.
- **pymysql**: Se requiere para la conexión de Lambda con MySQL en RDS. Este paquete puede incluirse en un layer o empaquetarse con la función Lambda.

---
