# Mystical Meals

Una API sencilla para gestionar recetas de cocina. Hay tres tipos de usuarios: los administradores, chef y clientes. Los administradores pueden crear, modificar y eliminar recetas, así como también crear y eliminar usuarios. Los chef pueden crear, modificar y eliminar recetas, pero no pueden crear o eliminar usuarios. Los clientes pueden ver las recetas y darlle un rating.  

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

1. Clonar repositorio `git clone https://github.com/cristina-bosa/backend-uem`
2. cd `git completed-server-django`
3. Crear el entorno virtual: `python -m venv env`.
4. Activar el entorno virtual: `source env/bin/activate` (for Unix-based systems) or `env\Scripts\activate` (for Windows).
5. Instalar las dependencias: `pip install -r requirements.txt`.
6. Crear a DB in PostgreSQL
7. Configurar esa BD en el settings del servidor.
8. Crear las migraciones: `python manage.py makemigrations`.
9. Lanzar las migraciones: `python manage.py migrate`.
10. Comando para cargar la base de datos `python manage.py seeder`

## Usage

1. Levantar el proyecto: `python manage.py runserver`.
2. `http://localhost:8000`.


## Features

### Authentication
#### Profile user

```http
GET /api/auth/me
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente             |
| 403    | El usuario no se encuentra autenticado                       |
| 500    | Se ha producido un error en el servidor durante el procesado |


#### Register

```http
POST /api/auth/register/
```

| Body       | Type  | Description                 |
|:-----------|:------|:----------------------------|
| `username` | `str` | Username para el nuevo user |
| `email`    | `str` | Email del usuario           |
| `password` | `str` | Password del usuario        |
```json
{
  "username": "test",
  "password": "test",
  "email": "test@test.com"
}
```

| Status | Description                                                    |
|:-------|:---------------------------------------------------------------|
| 201    | Las entidades han sido recuperadas y almacenadas correctamente |
| 400    | Faltan datos necesarios para la creación del usuario           |
| 500    | Se ha producido un error en el servidor durante el procesado   |


#### Login

```http
POST /api/auth/login
```

| Body       | Type  | Description                              |
|:-----------|:------|:-----------------------------------------|
| `username` | `str` | Username asociado al usuario del sistema |
| `password` | `str` | Password asociada al usuario del sistema |
```json
{
  "username": "test",
  "password": "test",
}
```

| Status | Description                                                    |
|:-------|:---------------------------------------------------------------|
| 202    | Las entidades han sido recuperadas y almacenadas correctamente |
| 403    | Las credenciales no fueron aportadas                           |
| 500    | Se ha producido un error en el servidor durante el procesado   |



#### Logout

```http
POST /api/auth/logout
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 202    | El usuario ha cerrado sesion correctamente                   |
| 403    | Las credenciales no fueron aportadas                         |
| 500    | Se ha producido un error en el servidor durante el procesado |

### Recetas
#### Create recipe
```http
POST /api/recipes/
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |
| `name` | `str` | Nombre de la receta |
| `instructions` | `str` | Instrucciones para preparar la receta |
| `time` | `str` | Tiempo que se tardaría en crear esa receta |
| `difficulty` | `int` | Dificultad de la receta |
| `owner` | `int` | Dueño de la receta |
| `category` | `int` | Categoria de la receta |
```json
{
  "name": "Gyozas",
  "instructions": "Instrucciones de como preparar unas ricas y jugosas gyozas",
  "time": "01:00",
  "difficulty": 6,
  "owner": 1,
  "category": 1
}
```

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Add ingredients to recipe
```http
POST /api/recipes/:id/add-ingredients
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |
| `ingredients` | `[]` | Nombre de la receta |
```json
{
  "ingredients": [
    {"ingredient": 1, "quantity": 11},
    {"ingredient": 3, "quantity": 33},
    {"ingredient": 5, "quantity": 55}
  ]
}
``` 

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |
#### Delete ingredients to recipe
```http
POST /api/recipes/:id/delete-ingredients
```

| Body   | Type     | Description            |
| :----- | :------- |:-----------------------|
| `ingredients` | `[]` | PK de los ingredientes |
```json
{
  "ingredients": [1, 5]
}
```
| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Get recipe
```http
GET /api/recipes/:id
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Get all
```http
GET /api/recipes
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Delete recipe
```http
DELETE /api/recipes/:id
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Update receta
```http
POST /api/recipes/id
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |
```json
{
  "name": "Gyozas",
  "instructions": "Instrucciones de como preparar unas ricas y jugosas gyozas",
  "time": "10:00",
  "difficulty": 6,
  "owner": 1,
  "category": 1
}
```

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Get all my recipes
```http
GET /api/recipes/me
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Top recipes
```http
GET /api/top-recipes
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |

### Ingredients, Categories

Se ha creado un CRUD básico para las entidades de ingredientes y categorías.
#### Ingredients
```http 
GET /api/ingredients
POST /api/ingredients/
GET /api/ingredients/:id
PUT /api/ingredients/:id
DELETE /api/ingredients/:id
```
#### Categories
```http
GET /api/categories
POST /api/categories/
GET /api/categories/:id
PUT /api/categories/:id
DELETE /api/categories/:id
```

### Ratings
