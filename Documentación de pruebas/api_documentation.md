# Documentación de API (FastAPI - /docs)

Todos los endpoints descritos a continuación pueden encontrarse documentados en el dominio **/docs**, ya que la documentación está generada con FastAPI. Además, se han realizado pruebas unitarias en cada uno de ellos utilizando **pytest** para garantizar su correcto funcionamiento.

---

## Autenticación (Auth)

### Endpoints:
- **GET /registro** - Permite a los usuarios registrarse proporcionando sus datos personales en un formulario. Los datos ingresados se validan antes de ser almacenados en la base de datos.
- **GET /noti** - Recupera todas las notificaciones relevantes para el usuario, incluyendo alertas de citas próximas y recordatorios importantes.
- **GET /** - Carga la página principal donde los usuarios pueden iniciar sesión ingresando sus credenciales.
- **POST /login/** - Endpoint que autentica a los usuarios mediante sus credenciales y genera un token de sesión para futuras solicitudes seguras.
- **GET /test** - Verifica la sesión actual del usuario y devuelve una respuesta de prueba confirmando si el usuario está autenticado.

---

## CRUD Afiliados

### Endpoints:
- **POST /create/affiliate** - Registra un nuevo afiliado, validando sus datos antes de almacenarlos en la base de datos.
- **GET /all/affiliate** - Devuelve una lista de todos los afiliados registrados en el sistema, con información detallada.
- **GET /filter/affiliate** - Filtra los afiliados según criterios como nombre, identificación y estado de afiliación.
- **PUT /update/affiliate** - Permite actualizar la información de un afiliado existente, como su dirección o contacto.
- **DELETE /delete/affiliate** - Elimina a un afiliado de la plataforma de manera permanente.

---

## CRUD Citas Médicas

### Endpoints:
- **GET /all/citas** - Recupera la lista completa de citas médicas registradas en el sistema.
- **GET /filter/citas** - Aplica filtros para encontrar citas según fecha, paciente o especialista.
- **POST /create/cita** - Registra una nueva cita médica en el sistema, asegurando la disponibilidad del especialista.
- **PUT /update/cita** - Permite modificar información de una cita existente, como la fecha o el especialista asignado.
- **DELETE /delete/cita** - Elimina una cita médica del sistema, cancelando su registro de manera permanente.

---

## CRUD Especialistas

### Endpoints:
- **GET /all/especialistas** - Devuelve la lista de especialistas registrados, con detalles sobre sus especialidades y disponibilidad.
- **GET /filter/specialist** - Filtra especialistas por especialidad, ubicación o experiencia.
- **POST /create/specialist** - Registra un nuevo especialista en la base de datos.
- **PUT /update/specialist** - Permite modificar la información de un especialista existente.
- **DELETE /delete/specialist** - Elimina un especialista del sistema de manera permanente.

---

## CRUD Medicamentos

### Endpoints:
- **GET /all/medicamentos** - Recupera una lista completa de los medicamentos disponibles en la plataforma.
- **GET /filter/medications** - Filtra medicamentos por tipo, uso o disponibilidad.
- **POST /create/medications** - Agrega un nuevo medicamento a la base de datos.
- **POST /user/medications** - Asigna un medicamento a un usuario específico.
- **PUT /update/medications** - Permite modificar los detalles de un medicamento existente.
- **DELETE /delete/medications** - Elimina un medicamento del inventario de la base de datos.

---

## Configuración de Cuenta Usuario y Admin

### Endpoints:
- **POST /update/admin** - Actualiza la configuración y datos de la cuenta de un administrador.
- **GET /admin/config** - Recupera la configuración actual de la cuenta administrativa.
- **POST /update/user** - Modifica la información personal de un usuario registrado.
- **DELETE /delete/user** - Elimina una cuenta de usuario y todos sus datos asociados.

---

## Otras Páginas y Funcionalidades

### Páginas informativas:
- **GET /conocenos** - Proporciona información sobre la plataforma y sus objetivos.
- **GET /inicio/politicas_privacidad** - Muestra la política de privacidad.
- **GET /inicio/terminos_condiciones** - Presenta los términos y condiciones de uso.
- **GET /inicio/redes_sociales** - Contiene enlaces a las redes sociales oficiales de la plataforma.

---

Cada uno de estos endpoints ha sido probado utilizando **pytest**, asegurando su correcto funcionamiento y estabilidad en el sistema.
