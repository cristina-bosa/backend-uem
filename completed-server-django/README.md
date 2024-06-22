# Mystical Meals

Una API sencilla para gestionar recetas de cocina. Hay tres tipos de usuarios: los administradores, los chef y los clientes. Los administradores pueden crear, modificar y eliminar recetas, así como también crear y eliminar usuarios. Los chef pueden crear, modificar y eliminar recetas, pero no pueden crear o eliminar usuarios. Los clientes pueden ver las recetas y darlle un rating.  

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)

## Installation

1. Clone the repository.
2. Create a virtual environment: `python -m venv env`.
3. Activate the virtual environment: `source env/bin/activate` (for Unix-based systems) or `env\Scripts\activate` (for Windows).
4. Install the dependencies: `pip install -r requirements.txt`.
5. Create a DB in PostgreSQL
6. Configure in settings user, name y databas ename.
7. Run database migrations: `python manage.py makemigrations`.
8. Run database migrations: `python manage.py migrate`.
9. Run `python manage.py seeder`

## Usage

1. Start the development server: `python manage.py runserver`.


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

| Status | Description                                                  |
|:-------|:-------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado |
#### Delete ingredients to recipe
```http
POST /api/recipes/:id/delete-ingredients
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

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

#### Get update
```http
POST /api/recipes/id
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

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
