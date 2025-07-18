# Proyecto de Autenticación Web con Flask y MySQL

Este proyecto es una aplicación web sencilla desarrollada en Python usando el framework Flask y una base de datos MySQL. Permite a los usuarios iniciar sesión mediante un formulario y acceder a una página de bienvenida personalizada. Incluye manejo de sesiones y validación de credenciales.

## Estructura de archivos

- `app.py`: Archivo principal de la aplicación Flask. Gestiona las rutas, la lógica de autenticación y las sesiones de usuario.
- `db_config.py`: Configuración de la conexión a la base de datos MySQL.
- `templates/login.html`: Plantilla HTML para el formulario de inicio de sesión.
- `templates/welcome.html`: Plantilla HTML para la página de bienvenida tras iniciar sesión.
- `GITHUB_GUIDE.md`: Guía de referencia rápida de comandos Git y GitHub (antes en este README).

## Requisitos

- Python 3.x
- Flask
- PyMySQL
- MySQL Server con una base de datos llamada `github` y una tabla `users` con los campos `name`, `email` y `password`.

## Instalación

1. Instala las dependencias de Python:
   ```bash
   pip install flask pymysql
   ```
2. Asegúrate de tener un servidor MySQL corriendo y crea la base de datos y tabla necesarias:
   ```sql
   CREATE DATABASE github;
   USE github;
   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(100),
       email VARCHAR(100),
       password VARCHAR(100)
   );
   ```
3. Ajusta los parámetros de conexión en `db_config.py` si es necesario.

## Ejecución

1. Inicia la aplicación ejecutando:
   ```bash
   python app.py
   ```
2. Accede a `http://localhost:5000` en tu navegador.

## Funcionamiento

### 1. Inicio de sesión
Al acceder a la raíz (`/`), se muestra el formulario de login. El usuario ingresa su correo y contraseña. Al enviar el formulario, se realiza una consulta a la base de datos para validar las credenciales.

### 2. Sesión y bienvenida
Si las credenciales son correctas, se almacena el nombre del usuario en la sesión y se redirige a `/welcome`, donde se muestra una página personalizada. Si no, se muestra un mensaje de error.

### 3. Cierre de sesión
El usuario puede cerrar sesión accediendo a `/logout`, lo que limpia la sesión y redirige al login.

## Archivos principales

### app.py
Contiene la lógica principal:
- Rutas `/`, `/login`, `/welcome`, `/logout`.
- Validación de usuario contra la base de datos.
- Manejo de sesiones y mensajes flash.

### db_config.py
Configura la conexión a MySQL usando PyMySQL. Cambia los parámetros según tu entorno.

### templates/
- `login.html`: Formulario de acceso.
- `welcome.html`: Página de bienvenida.

## Seguridad

- La contraseña de los usuarios se almacena en texto plano solo para fines demostrativos. Para producción, usa hash seguro.
- La clave secreta de Flask debe ser cambiada por una más robusta en producción.

---

Para dudas o mejoras, abre un issue o pull request.
