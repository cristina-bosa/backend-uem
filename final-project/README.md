# Final project

Este proyecto es una API REST basada en Django Rest Framework que sirve para la gestion de proyectos y sus tareas.

## Table of Contents

- [Installation](#installation)
- [Task-manager bot usage](#task-manager-bot-usage)
- [API usage](#api-usage)
- [API Reference](#api-reference)

## Installation

1. Clonar repositorio `git clone https://github.com/cristina-bosa/backend-uem`
3. cd final_project
4. Crear el entorno virtual `py -m venv env`
5. Activar el entorno virtual `source env/bin/activate` or `env\Scripts\activate`
6. Instalar dependencias `pip install -r requirements.txt`
7. Hacer migraciones `python manage.py migrate`
8. Comando para cargar la base de datos `py manage.py seeder`

## Task-manager bot usage

1. Levantar el bot de Telegram `python ./bot_telegram.py`.
2. Buscar el bot de Telegram `@Task_manager_uem_bot`.
2. Ejecutar el commando `/id` en el bot y guardar el id

Este id facilitado mediante el bot de telegram es necesario para poder registrarse en la API y poder enviar 
notificaciones al usuario.

## API Usage

1. Levantar el proyecto: `python manage.py runserver`.
2. `http://localhost:8000`.

## API Reference

### Authentication
#### Información de usuario

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


### Projects
#### Lista de proyectos

```http
GET /api/projects/
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Obtener un proyecto

```http
GET /api/projects/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Crear un proyecto

```http
POST /api/projects/
```

| Body          | Type  | Description              |
|:--------------|:------|:-------------------------|
| `name`        | `str` | Name del proyecto        |
| `description` | `str` | Descripción del proyecto |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido creadas correctamente                    |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Editar un proyecto

```http
PUT /api/projects/:id/
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body          | Type  | Description              |
|:--------------|:------|:-------------------------|
| `name`        | `str` | Name del proyecto        |
| `description` | `str` | Descripción del proyecto |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y actualizadas correctamente |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Borrar un proyecto

```http
DELETE /api/projects/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 204    | Las entidades han sido eliminadas correctamente                 |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 404    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Cambiar estado de un proyecto

```http
PUT /api/projects/:id/change-status/
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body     | Type  | Description               |
|:---------|:------|:--------------------------|
| `status` | `str` | Nuevo estado del proyecto |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 404    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Lista de tareas de un proyecto

```http
GET /api/projects/:id/tasks
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body     | Type  | Description               |
|:---------|:------|:--------------------------|

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 404    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |



### Tasks
#### Lista de tareas

```http
GET /api/task/
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Obtener una tarea

```http
GET /api/task/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Crear una tarea

```http
POST /api/task/
```

| Body          | Type  | Description              |
|:--------------|:------|:-------------------------|
| `name`        | `str`       | Name del tareas                                |
| `description` | `str`       | Descripción del tareas                         |
| `project`     | `int`       | Id del proyecto relacionado                    |
| `users`       | `list[int]` | Lista con los Ids de los usuarios relacionados |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido creadas correctamente                    |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Editar una tarea

```http
PUT /api/task/:id/
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body          | Type        | Description                                    |
|:--------------|:------------|:-----------------------------------------------|
| `name`        | `str`       | Name del tareas                                |
| `description` | `str`       | Descripción del tareas                         |
| `project`     | `int`       | Id del proyecto relacionado                    |
| `users`       | `list[int]` | Lista con los Ids de los usuarios relacionados |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y actualizadas correctamente |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Borrar una tarea

```http
DELETE /api/task/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido eliminadas correctamente                 |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Cambiar estado de un proyecto

```http
PUT /api/task/:id/change-status/
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body     | Type  | Description              |
|:---------|:------|:-------------------------|
| `status` | `str` | Nuevo estado de la tarea |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 202    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 404    | La entidad no ha sido encontrada |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Añadir usuarios a una tarea

```http
PUT /api/task/:id/add-users-task/
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body   | Type        | Description                             |
|:-------|:------------|:----------------------------------------|
| `user` | `list[str]` | Lista con los nuevos usuarios asociados |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 202    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos                                 |
| 404    | La entidad no ha sido encontrada |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Eliminar usuarios de una tarea

```http
DELETE /api/task/:id/delete-users-task/
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body   | Type        | Description                             |
|:-------|:------------|:----------------------------------------|
| `user` | `list[str]` | Lista con los nuevos usuarios asociados |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 202    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 404    | La entidad no ha sido encontrada |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Lista de tareas del usuario autenticado

```http
GET /api/task/me
```

| Body     | Type  | Description               |
|:---------|:------|:--------------------------|

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 404    | La entidad no ha sido encontrada |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Lista de comentarios de una tarea

```http
GET /api/task/:id/comments
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body     | Type  | Description               |
|:---------|:------|:--------------------------|

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 404    | La entidad no ha sido encontrada                                |
| 500    | Se ha producido un error en el servidor durante el procesado    |


### Comments
#### Lista de comentarios

```http
GET /api/comment/
```

| Body   | Type     | Description       |
| :----- | :------- | :---------------- |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |

#### Obtener un comentario

```http
GET /api/comment/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas correctamente                |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Crear un comentario

```http
POST /api/comment/
```

| Body       | Type  | Description                |
|:-----------|:------|:---------------------------|
| `commment` | `str` | Contenido del comentario   |
| `task`     | `int` | Id de la tarea relacionada |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido creadas correctamente                    |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Editar un comentario

```http
PUT /api/comment/:id/
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Body          | Type  | Description              |
|:--------------|:------|:-------------------------|
| `commment` | `str` | Contenido del comentario   |
| `task`     | `int` | Id de la tarea relacionada |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido recuperadas y actualizadas correctamente |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |


#### Borrar un comentario

```http
DELETE /api/comment/:id
```

| Parameter | Type  | Description      |
| :-------- | :---- | :--------------- |
| `id`      | `int` | PK de la entidad |

| Status | Description                                                     |
|:-------|:----------------------------------------------------------------|
| 200    | Las entidades han sido eliminadas correctamente                 |
| 403    | El usuario no se encuentra autenticado o no dispone de permisos |
| 500    | Se ha producido un error en el servidor durante el procesado    |
