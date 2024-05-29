# Mythology

Está pequeña API está orientada a la mitología.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Reference](#api-reference)

## Installation

1. Clonar repositorio `git clone https://github.com/cristina-bosa/backend-uem`
2. cd basic-server-django
3. cd basic_server_django
4. Crear el entorno virtual `py -m venv env`
5. Activar el entorno virtual `source env/bin/activate` or `env\Scripts\activate`
6. Instalar dependencias `pip install -r requirements.txt`
7. Hacer migraciones `python manage.py migrate`
8. Comando para cargar la base de datos `py manage.py seeder`

## Usage

1. Levantar el proyecto: `python manage.py runserver`.
2. `http://localhost:8000`.

## API Reference

### House

#### Crear una casa

```http
POST /mythology/house
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |
| `name` | `string` | Nombre de la casa |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Consultar todas las casas

```http
GET /mythology/house
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Consultar una casa

```http
GET /mythology/house/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Editar una casa

```http
PUT /mythology/house/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |
| `name` | `string` | Nombre de la casa |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Borrar una casa

```http
DELETE /mythology/house/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                  |
| :----- | :----------------------------------------------------------- |
| 204    | La entidad fue eliminada correctamente                       |
| 404    | La entidad no fue encontrada                                 |
| 500    | Se ha producido un error en el servidor durante el procesado |

### BeingType

#### Crear un tipo de ser

```http
POST /mythology/being_type
```

| BODY   | Type     | Description            |
| :----- | :------- | :--------------------- |
| `name` | `string` | Nombre del tipo de ser |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Consultar todos los tipos de seres

```http
GET /mythology/being_type
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Consultar un tipo de ser

```http
GET /mythology/being_type/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Editar un Tipo de ser

```http
PUT /mythology/being_type/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body   | Type     | Description            |
| :----- | :------- | :--------------------- |
| `name` | `string` | Nombre del tipo de ser |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Borrar un tipo de ser

```http
DELETE /mythology/being_type/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                  |
| :----- | :----------------------------------------------------------- |
| 204    | La entidad fue eliminada correctamente                       |
| 404    | La entidad no fue encontrada                                 |
| 500    | Se ha producido un error en el servidor durante el procesado |

### Story

#### Crear una historia

```http
POST /mythology/story
```

| Body      | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `title`   | `string` | Título de la historia    |
| `content` | `string` | Contenido de la historia |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Consultar todas las historias

```http
GET /mythology/story
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Consultar una historia

```http
GET /mythology/story/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Editar una historia

```http
PUT /mythology/story/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body      | Type     | Description              |
| :-------- | :------- | :----------------------- |
| `title`   | `string` | Título de la historia    |
| `content` | `string` | Contenido de la historia |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Borrar una historia

```http
DELETE /mythology/story/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                  |
| :----- | :----------------------------------------------------------- |
| 204    | La entidad fue eliminada correctamente                       |
| 404    | La entidad no fue encontrada                                 |
| 500    | Se ha producido un error en el servidor durante el procesado |

### Being

#### Crear un ser

```http
POST /mythology/being
```

| Body       | Type     | Description                           |
| :--------- | :------- | :------------------------------------ |
| `name`     | `string` | Nombre del ser                        |
| `type_id`  | `int`    | Relación con la tabla correspondiente |
| `story_id` | `int`    | Relación con la tabla correspondiente |
| `house_id` | `int`    | Relación con la tabla correspondiente |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Consultar todas las historias

```http
GET /mythology/being
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Consultar una historia

```http
GET /mythology/being/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 204    | No han sido encontrado entidades                               |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Editar una historia

```http
PUT /mythology/being/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body       | Type     | Description                           |
| :--------- | :------- | :------------------------------------ |
| `name`     | `string` | Nombre del ser                        |
| `type_id`  | `int`    | Relación con la tabla correspondiente |
| `story_id` | `int`    | Relación con la tabla correspondiente |
| `house_id` | `int`    | Relación con la tabla correspondiente |

| Status | Description                                                     |
| :----- | :-------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente  |
| 400    | El contenido de la petición no es válido o le falta informacion |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Borrar una historia

```http
DELETE /mythology/being/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                  |
| :----- | :----------------------------------------------------------- |
| 204    | La entidad fue eliminada correctamente                       |
| 404    | La entidad no fue encontrada                                 |
| 500    | Se ha producido un error en el servidor durante el procesado |
