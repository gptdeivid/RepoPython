
Este proyecto es una aplicación web simple de inicio de sesión desarrollada con Flask y MySQL. Permite a los usuarios autenticarse mediante un formulario de login y, si las credenciales son correctas, acceder a una página de bienvenida. Incluye manejo de sesiones y mensajes de error para credenciales incorrectas.

## Estructura de Archivos

- `app.py`: Archivo principal de la aplicación Flask. Define las rutas, la lógica de autenticación y el manejo de sesiones.
- `db_config.py`: Configuración de la conexión a la base de datos MySQL.
- `templates/login.html`: Plantilla HTML para el formulario de inicio de sesión.
- `templates/welcome.html`: Plantilla HTML para la página de bienvenida tras iniciar sesión.
- `README.md`: Documentación del proyecto (este archivo).
- `README_git.md`: Documentación de comandos y flujo de trabajo de GitHub (ver más abajo).

## Funcionamiento de la Aplicación

1. **Inicio de sesión** (`/` y `/login`):
   - El usuario accede a la ruta raíz (`/`) y se muestra el formulario de login.
   - Al enviar el formulario, se procesa en la ruta `/login` (método POST).
   - Se verifica el email y la contraseña contra la base de datos MySQL (tabla `users`).
   - Si las credenciales son correctas, se guarda el nombre del usuario en la sesión y se redirige a `/welcome`.
   - Si son incorrectas, se muestra un mensaje de error y se vuelve al login.

2. **Página de bienvenida** (`/welcome`):
   - Si el usuario está autenticado (hay un `username` en la sesión), se muestra la página de bienvenida con su nombre.
   - Si no está autenticado, se redirige al login.

3. **Cerrar sesión** (`/logout`):
   - El usuario puede cerrar sesión, lo que limpia la sesión y lo redirige al login.

## Requisitos

- Python 3.x
- Flask
- PyMySQL
- MySQL (con una base de datos llamada `github` y una tabla `users` con los campos `email`, `password` y `name`)

## Instalación y Ejecución

1. Instala las dependencias:
   ```bash
   pip install flask pymysql
   ```
2. Configura tu base de datos MySQL y ajusta los datos de conexión en `db_config.py` si es necesario.
3. Ejecuta la aplicación:
   ```bash
   python app.py
   ```
4. Accede a `http://localhost:5000` en tu navegador.

## Seguridad
- La contraseña se compara en texto plano. Para producción, se recomienda usar hash de contraseñas.
- La clave secreta de Flask debe ser cambiada por una más segura en producción.

## Créditos
Desarrollado por gptdeivid.

---

**Nota:** La documentación original sobre comandos de Git y GitHub se ha movido a `README_git.md`.
