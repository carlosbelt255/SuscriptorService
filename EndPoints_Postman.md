Buscar suscriptor por numero de celular:

método POST: https://22vtim19z6.execute-api.us-east-2.amazonaws.com/test/suscriptores

json entrada:

{
    "suscriptor": {
        "telefono_celular": "7773008855"
    }
}

salida:

{
    "telefono_celular": "7773008855",
    "nombre": "Carlos",
    "apellido_materno": "Garcia",
    "apellido_paterno": "Lopez",
    "edad": 25
}


************************************************************************************************************************

Obtener lista de todos los suscriptores registrados en el sistema:

método GET: https://22vtim19z6.execute-api.us-east-2.amazonaws.com/test/suscriptores

respuesta:

[
    {
        "telefono_celular": "5555555555",
        "nombre": "Juan",
        "apellido_materno": "Garcia",
        "apellido_paterno": "Lopez",
        "edad": 25
    },
    {
        "telefono_celular": "7773008855",
        "nombre": "Carlos",
        "apellido_materno": "Garcia",
        "apellido_paterno": "Lopez",
        "edad": 25
    },
    {
        "telefono_celular": "7774568923",
        "nombre": "Enrique",
        "apellido_materno": "Lara",
        "apellido_paterno": "Lopez",
        "edad": 45
    },
    {
        "telefono_celular": "7774895623",
        "nombre": "Ericka",
        "apellido_materno": "Lara",
        "apellido_paterno": "Beltrán",
        "edad": 25
    },
    {
        "telefono_celular": "7777893400",
        "nombre": "Liliana",
        "apellido_materno": "Ramirez",
        "apellido_paterno": "Lopez",
        "edad": 45
    }
]

************************************************************************************************************************

Registrar un nuevo suscriptor en el sistema:

método POST: https://22vtim19z6.execute-api.us-east-2.amazonaws.com/test/suscriptores

json de entrada:

{
    "suscriptor": {
        "info_nombre": {
            "nombre": "Cristiano",
            "apellido_materno": "Ronaldo",
            "apellido_paterno": "Beltrán"
        },
        "edad": 46,
        "telefono_celular": "7779005623"
    }
}

json de respuesta:

{
    "message": "Suscriptor creado exitosamente"
}

************************************************************************************************************************

Modificar un suscriptor especificando su numero celular:

método PUT: https://22vtim19z6.execute-api.us-east-2.amazonaws.com/test/suscriptores

json de entrada:

{
    "telefono_celular": "5555555555",
    "suscriptor": {
        "info_nombre": {
            "nombre": "Martha",
            "apellido_materno": "Garcia",
            "apellido_paterno": "Lopez"
        },
        "edad": 30
    }
}

json de respuesta:

{
    "message": "Suscriptor actualizado exitosamente"
}

************************************************************************************************************************

Eliminar un suscriptor del sistema especificando su numero celular:

método DELETE:  https://22vtim19z6.execute-api.us-east-2.amazonaws.com/test/suscriptores

json de entrada:

{
    "telefono_celular": "5555555555"
}

json de respuesta:
{
    "message": "Suscriptor eliminado exitosamente"
}
