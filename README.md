# API

Esta API funciona como intermediaria entre las aplicaciones y la API de BigBlueButton.

El usuario final nunca deberá ni podrá tener acceso a esta API. Todas las llamadas deben ser realizadas desde el código de la aplicación.

## Seguridad

En esta primera beta no hay un mecanismo de autenticacion para validar las llamadas remotas. Solamente se limitaran por la IP del servidor que hace el request.

# Configuraciones:
Dentro del archivo `settings.py`

## Crear una sala

Parametros:
- **name** (opcional): El nombre de la sala
- **moderator_pw** (opcional): La contraseña para el **rol de moderador**. Si no se provee un valor se generara automáticamente.
- **attendee_pw** (opcional): La contraseña para al **rol de usuario regular**. Si no se provee un valor se generara automáticamente.
- **welcome_msg** (opcional): El mensaje de bienvenida en la ventana de chat
- **logout_url** (opcional): La url a la cual se redireccionara al usuario cuando salga de la sala.
- **duration** (opcional): La duración máxima **en minutos** de la sala. Luego de este tiempo la sala se cerrara automáticamente

**Metodo**: `GET`

### Ejemplo

`curl -v -L "http://127.0.0.1:5000/create?welcome_msg=Bienvenidos+al+seminario+de+Peugeot%21%21&name=Seminario+Peugeot&logout_url=http%3A%2F%2Fwww.ignitiontechnology.com%2F"`

Si la operación es exitosa se obtendra la siguiente respuesta:

```
{
  "attendeePW": "W8fsVmM1",
  "createDate": "Sun Nov 29 19:14:43 EST 2015",
  "createTime": "1448842483320",
  "duration": "0",
  "hasBeenForciblyEnded": "false",
  "hasUserJoined": "false",
  "meetingID": "900dabe7-494a-4a97-b573-314e0b3b4c5e",
  "message": null,
  "messageKey": null,
  "moderatorPW": "rIsm19lA",
  "returncode": "SUCCESS"
}
```

En caso de existir un error el key **returncode** devolvera **FAILURE**

### Acceder al salón

Parametros:

- **MEETING_ID** (requerido): El id del salón
- **full_name** (requerido): El nombre y apellido del usuario
- **password** (requerido): La contraseña para acceder al salón. Esta contraseña setea el rol del usuario dentro de la sala (moderador o usuario regular)

**Metodo**: `GET`

`curl -v -L "http://127.0.0.1:5000/join/MEETING_ID/?full_name=daniel_gonzales&password=abcd1234"`

Si la operación es exitosa se obtendra la siguiente respuesta:
```
{
  "result": "SUCCESS", 
  "url": "http://159.203.111.109/bigbluebutton/api/join?fullName=daniel&password=JoVKaq9a&checksum=ff61dddf2456bf45baf5f96249ff1b4a1f5a5a04"
}
```

```
{
  "message": "You need to send the user's full name and password to join the room",
  "result": "FAIL"
}
```
