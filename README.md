# Student Card API

API REST construida con **FastAPI** para consultar y registrar estudiantes. Proyecto del módulo 0 del curso de FastAPI.

---

## Requisitos

- Python 3.8+
- FastAPI
- Uvicorn
- Pydantic (con soporte para `email-validator`)

Instala las dependencias:

```bash
pip install fastapi uvicorn "pydantic[email]"
```

---

## Ejecutar el servidor

Desde la carpeta `app/`:

```bash
uvicorn main:app --reload
```

El servidor quedará disponible en `http://127.0.0.1:8000`.

---

## Documentación interactiva

FastAPI genera documentación automática:

| Interfaz | URL |
|----------|-----|
| Swagger UI | http://127.0.0.1:8000/docs |
| ReDoc | http://127.0.0.1:8000/redoc |

---

## Endpoints

### `GET /students`

Retorna la lista de todos los estudiantes. Acepta un filtro opcional por estado.

**Query params:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `active` | `bool` (opcional) | Filtra por estudiantes activos (`true`) o inactivos (`false`) |

**Ejemplo:**
```
GET /students?active=true
```

---

### `GET /students/{id}`

Retorna un estudiante por su ID.

**Path params:**

| Parámetro | Tipo | Descripción |
|-----------|------|-------------|
| `id` | `int` | ID del estudiante |

**Respuestas:**
- `200 OK` — Estudiante encontrado
- `404 Not Found` — Estudiante no existe

---

### `POST /students`

Registra un nuevo estudiante.

**Body (JSON):**

```json
{
  "name": "Nombre completo",
  "email": "correo@ejemplo.com",
  "program": "Nombre del programa",
  "active": true
}
```

| Campo | Tipo | Validación |
|-------|------|------------|
| `name` | `string` | Mínimo 1 carácter |
| `email` | `string` | Formato de email válido |
| `program` | `string` | Mínimo 1 carácter |
| `active` | `bool` | — |

**Respuestas:**
- `201 Created` — Estudiante creado, retorna el objeto con su `id` asignado

---

## Modelo de datos

```json
{
  "id": 1,
  "name": "Javier Esteban Perez Gomez",
  "email": "javierperez232@gmail.com",
  "program": "Análisis y Desarrollo de Software",
  "active": true
}
```

---

## Estructura del proyecto

```
modulo-0-fundamentos/
├── app/
│   ├── main.py        # Aplicación principal
│   └── README.md      # Este archivo
```
