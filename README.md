# Sistema de Login con Flask y MySQL

Este es un sistema simple de autenticación desarrollado con Flask y MySQL que permite a los usuarios iniciar sesión y acceder a una página de bienvenida personalizada.

## Características

- Sistema de login con email y contraseña
- Manejo de sesiones de usuario
- Interfaz responsiva usando Bootstrap
- Mensajes de error para credenciales inválidas
- Función de cierre de sesión

## Estructura del Proyecto

```
├── app.py              # Aplicación principal de Flask
├── db_config.py        # Configuración de la base de datos
├── templates/          # Plantillas HTML
│   ├── login.html      # Página de inicio de sesión
│   └── welcome.html    # Página de bienvenida
```

## Requisitos

- Python 3.x
- Flask
- PyMySQL
- Base de datos MySQL

## Configuración de la Base de Datos

La aplicación espera una base de datos MySQL llamada `github` con una tabla `users` que debe contener los siguientes campos:
- name (varchar)
- email (varchar)
- password (varchar)

La configuración de la conexión a la base de datos se encuentra en `db_config.py`:
```python
host="localhost"
user="root"
password=""
database="github"
```

## Instalación

1. Clona este repositorio
2. Instala las dependencias:
```bash
pip install flask pymysql
```
3. Configura tu base de datos MySQL y crea la tabla `users`
4. Ejecuta la aplicación:
```bash
python app.py
```

## Uso

1. Accede a `http://localhost:5000` en tu navegador
2. Ingresa tus credenciales (email y contraseña)
3. Si las credenciales son correctas, serás redirigido a la página de bienvenida
4. Puedes cerrar sesión usando el botón "Cerrar sesión"

## Características de Seguridad

- Las sesiones están protegidas con una clave secreta
- Manejo de errores para intentos de acceso no autorizados
- Redirección automática a login para usuarios no autenticados

## Nota de Desarrollo

La aplicación está configurada en modo debug para desarrollo. Para producción, asegúrate de:
1. Deshabilitar el modo debug
2. Cambiar la clave secreta por una más segura
3. Implementar hash de contraseñas
4. Configurar HTTPS
