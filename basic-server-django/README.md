# api

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
POST /api/house
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
GET /api/house
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
GET /api/house/:id
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
PUT /api/house/:id
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
DELETE /api/house/:id
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
POST /api/being_type
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
GET /api/being-type
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
GET /api/being-type/:id
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
PUT /api/being-type/:id
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
DELETE /api/being-type/:id
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
POST /api/story
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
GET /api/story
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
GET /api/story/:id
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
PUT /api/story/:id
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
DELETE /api/story/:id
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
POST /api/being
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
GET /api/being
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
GET /api/being/:id
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
PUT /api/being/:id
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
DELETE /api/being/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                  |
| :----- | :----------------------------------------------------------- |
| 204    | La entidad fue eliminada correctamente                       |
| 404    | La entidad no fue encontrada                                 |
| 500    | Se ha producido un error en el servidor durante el procesado |

### Filtrar historias

```http
GET /api/story-filter/
```

| Body         | Type     | Description            |
| :----------- | :------- | :--------------------- |
| `house`      | `string` | Nombre de la casa      |
| `being_type` | `string` | Nombre del tipo de ser |
| `being`      | `string` | Nombre del ser         |

| Status | Description                                                  |
| :----- | :----------------------------------------------------------- |
| 200    | La entidad fue encontrada                                    |
| 500    | Se ha producido un error en el servidor durante el procesado |
