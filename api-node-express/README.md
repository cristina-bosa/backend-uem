# API-NODE-EXPRESS

Desarrollo de una pequeña API en Express basado en una NoSQL DB (Mongo)

## Deployment

Para desplegar este proyecto en local es necesario realizar los siguientes pasos

```bash
  git clone https://github.com/cristina-bosa/backend-uem
  cd api-node-express
  npm i
  crear el fichero .env con las variables mencionadas
  npm run watch
```

## Environment Variables

Para levantar este proyecto, será necesario añadir la siguientes variables de entorno en el .env

`API_ANIME`: URL asociado a la API externa utilizada para la recopilación de datos. Para esta ocasión se ha usado
https://api.jikan.moe/v4/anime

`DATABASE`: Connection string generado a partir de la instancia de MongoDB a utilizar

`PORT`: Puerto para poder levantar el servidor.

## Features

Esta API proporciona las siguientes funcionalidades

- Cargar datos de anime procedentes de una fuente externa
- Consultar los animes cargados
- Consultar información de un anime
- Añadir a favoritos un anime
- Borrar de favoritos un anime
- Borrar un anime de la base de datos

## API Reference

#### Cargar datos de anime procedentes de una fuente externa

```http
  POST /api/anime/load
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |

| Status | Description                                                    |
| :----- | :------------------------------------------------------------- |
| 200    | Las entidades han sido recuperadas y almacenadas correctamente |
| 500    | Se ha producido un error en el servidor durante el procesado   |

#### Consultar los animes cargados

```http
  GET /api/anime/
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |

| Status | Description                                                   |
| :----- | :------------------------------------------------------------ |
| 200    | Las entidades han sido recuperadas y devueltas como respuesta |
| 404    | No se ha encontrado entidades en el sistema                   |
| 500    | Se ha producido un error en el servidor durante el procesado  |

#### Consultar información de un anime

```http
  GET /api/anime/:mal_id
```

| Parameter | Type  | Description   |
| :-------- | :---- | :------------ |
| `mal_id`  | `int` | **Required**. |

| Status | Description                                                  |
| :----- | :----------------------------------------------------------- |
| 200    | La entidad han sido recuperadas y devuelta correctamente     |
| 404    | No se ha encontrado ninguna entidad en el sistema            |
| 500    | Se ha producido un error en el servidor durante el procesado |

#### Añadir a favoritos un anime

```http
  PUT /api/anime/add-favorite/:mal_id
```

| Parameter | Type  | Description   |
| :-------- | :---- | :------------ |
| `mal_id`  | `int` | **Required**. |

| Status | Description                                                                |
| :----- | :------------------------------------------------------------------------- |
| 200    | La entidad ha sido encontrado y se ha realizado la operación correctamente |
| 404    | No se ha encontrado la entidad en el sistema                               |
| 500    | Se ha producido un error en el servidor durante el procesado               |

#### Borrar de favoritos un anime

```http
  PUT /api/anime/delete-favorite/:mal_id
```

| Parameter | Type  | Description   |
| :-------- | :---- | :------------ |
| `mal_id`  | `int` | **Required**. |

| Status | Description                                                                |
| :----- | :------------------------------------------------------------------------- |
| 200    | La entidad ha sido encontrado y se ha realizado la operación correctamente |
| 404    | No se ha encontrado la entidad en el sistema                               |
| 500    | Se ha producido un error en el servidor durante el procesado               |

#### Todos los favoritos

```http
  GET /api/anime/favorites
```

| Parameter | Type | Description |
| :-------- | :--- | :---------- |

| Status | Description                                                                |
| :----- | :------------------------------------------------------------------------- |
| 200    | La entidad ha sido encontrada y se ha realizado la operación correctamente |
| 404    | No se ha encontrado la entidad en el sistema                               |
| 500    | Se ha producido un error en el servidor durante el procesado               |

#### Borrar un anime

```http
  DELETE /api/anime/:mal_id
```

| Parameter | Type  | Description   |
| :-------- | :---- | :------------ |
| `mal_id`  | `int` | **Required**. |

| Status | Description                                                               |
| :----- | :------------------------------------------------------------------------ |
| 200    | La entidad ha sido encontrada y se ha eliminado correctamente             |
| 404    | No se ha encontrado la entidad en el sistema y por tanto no se ha borrado |
| 500    | Se ha producido un error en el servidor durante el procesado              |

## Tech Stack

**Server:** Node, Express, MongoDB

## Demo

![Demo](https://github.com/cristina-bosa/backend-uem/blob/main/api-node-express/demo.gif)
