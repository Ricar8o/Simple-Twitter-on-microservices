# Simple-Twitter-on-microservices

Para este ejercicio desplegaremos un API con microservicios para simular el comportamiento básico de una app cómo Twitter. Usaremos las tecnologías AWS API Gateway, AWS Lambda Functions y el framework de python `fastapi` para la implementación.

## Diseño

### Conceptos

Primero identificamos los conceptos básicos para que la app funcione y cómo se relacionan estos.

<p align="center">
  <img src="img/app-concepts.png" />
</p>

Después de definir los conceptos ahora podemos definir que acciones se deberían poder realizar en el aplicativo.

### Métodos y recursos

**Posts (publicaciones)**

- *GET* /feed-> Obtener publicaciones para el feed del usuario

- *POST* /posts -> Crear publicaciones

- *GET* /posts/{id} -> Obtener publicación

- *PUT* /posts/{id} -> Editar una publicación existente

- *DELETE* /posts/{id} -> Eliminar publicación

**Comments (Comentarios)**

- *POST* /posts/{id}/comments -> Agregar comentario a una publicación

- *GET* /posts/{id}/comments -> Obtener comentarios de publicación

**Likes**

- *POST* /posts/{id}/like-> Darle Me gusta a una la publicación

- *DELETE* /posts/{id}/like -> Quitar el Me gusta de una publicación


**Users (Usuarios)**

- *POST* /users/{id}/follow -> Seguir a usuario

- *POST* /users/{id}/unfollow -> Dejar de seguir a usuario

- *GET* /users/{id}/followers -> Obtener seguidores

- *GET* /users/{id}/following -> Obtener seguidos

- *GET* /users/{id}/posts-> Obtener publicaciones del usuario

También necesitamos que un usuario pueda iniciar sesión y registrarse


**Auth (Autenticación)**

- *POST* /register -> Registrar usuarios

- *POST* /login -> Iniciar sesión


### Arquitectura

Estas funciones de la aplicación estarán repartidas en 3 microservicios.


![prototype-design.png](img/Prototipo-Twitter-ARQUITECTURA.png)

Como usaremos API Gateway le asignáremos un prefijo a cada microservicio.

**Microservicios:**

**Auth API**

  - **Prefijo:** auth-api/v1
  - **Recursos:** Auth

**Posts API**

  - **Prefijo:** posts-api/v1
  - **Recursos:** Comments, Posts, Likes


**Users API**

  - **Prefijo:** users-api/v1
  - **Recursos:** Users

## Implementación
Para la implementación se realizarán los 3 microservicios usando el framework de python [FastApi](https://fastapi.tiangolo.com/es/).

También se usara la herramienta de python virtualenv para generar los paquetes que serán subidos a las lambdas al momento del despliegue.

### Virtual environment

**Instalación**

[Guía de instalación](https://virtualenv.pypa.io/en/latest/installation.html)

```Bash
# En algunos sistemas linux se instala así para ejecutarlo como comando de terminal
sudo apt install python3-virtualenv
```

**Usando el ambiente virtual**

```Bash
# Create environment with python3.10
virtualenv -p python3.10 env

# Access environmet
source ./env/bin/activate

# Exit environment
deactivate
```

### Instalar los paquetes necesarios para ejecutar la aplicación

**Instalando usando un archivo con una lista de paquetes**

```Bash
pip install -r requirements.txt
```

**Instalando directamente los paquetes**

```Bash
pip install fastapi
pip install "uvicorn[standard]"
```

[Uvicorn](https://www.uvicorn.org) es una implementación de servidor web ASGI para Python.

```Bash
# En algunos sistemas linux se instala así para ejecutarlo como comando de terminal
sudo apt install uvicorn
```


## Ejecutando algún servicio

```Bash
# Accedemos a la carpeta del servicio
cd src/services/<service-name>

# Desplegamos el API usando uvicorn
uvicorn app.main:app --reload

# Desplegando el servicio en un puerto diferente
uvicorn app.main:app --reload --port 8001

```
