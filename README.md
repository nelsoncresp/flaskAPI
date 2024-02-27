# API de Personas

Esta API proporciona endpoints para gestionar información de personas.

## Endpoints

### Listar todas las personas

- **URL:** `/personas`
- **Método:** `GET`
- **Respuesta exitosa:** `200 OK`

   Retorna la lista de todas las personas.

### Obtener una persona por su ID

- **URL:** `/personas/<id>`
- **Método:** `GET`
- **Parámetros de la URL:**
  - `id` (int): ID único de la persona.
- **Respuesta exitosa:** `200 OK`
- **Respuesta no encontrada:** `404 Not Found`

   Retorna los detalles de una persona por su ID.

### Añadir una nueva persona

- **URL:** `/personas`
- **Método:** `POST`
- **Datos esperados en el cuerpo de la solicitud (JSON):**
  - `nombre` (str): Nombre de la persona.
  - `edad` (int): Edad de la persona.
  - `ciudad` (str): Ciudad de la persona.
- **Respuesta exitosa:** `201 Created`
- **Respuesta de error:** `400 Bad Request`

   Añade una nueva persona.

### Actualizar una persona existente

- **URL:** `/personas/<id>`
- **Método:** `PUT`
- **Parámetros de la URL:**
  - `id` (int): ID único de la persona.
- **Datos esperados en el cuerpo de la solicitud (JSON):**
  - `nombre` (str): Nuevo nombre de la persona.
  - `edad` (int): Nueva edad de la persona.
  - `ciudad` (str): Nueva ciudad de la persona.
- **Respuesta exitosa:** `200 OK`
- **Respuesta no encontrada:** `404 Not Found`

   Actualiza los detalles de una persona existente.

### Eliminar una persona

- **URL:** `/personas/<id>`
- **Método:** `DELETE`
- **Parámetros de la URL:**
  - `id` (int): ID único de la persona.
- **Respuesta exitosa:** `200 OK`
- **Respuesta no encontrada:** `404 Not Found`

   Elimina una persona por su ID.

## Configuración

1. Instala las dependencias: `pip install -r requirements.txt`
2. Ejecuta la aplicación: `python app.py`
3. La API estará disponible en `http://localhost:4000`

---
