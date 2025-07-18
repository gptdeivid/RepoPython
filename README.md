# 🎨 Sistema de Login Moderno con Flask

Un sistema de login visualmente impactante con efectos modernos, modo oscuro/claro y animaciones suaves.

## ✨ Características

- **🌓 Dark/Light Mode**: Toggle dinámico entre temas
- **💫 Glassmorphism**: Efectos de cristal y desenfoque
- **🎭 Animaciones CSS**: Transiciones suaves y micro-interacciones
- **🔒 Iconos Animados**: Font Awesome con efectos hover
- **⏳ Loading Spinner**: Spinner personalizado durante login
- **📢 Toast Notifications**: Notificaciones elegantes
- **📱 Responsive**: Funciona en móvil y desktop

## 🚀 Instalación y Uso

### Requisitos
- Python 3.7+
- Flask (se instala automáticamente)

### Pasos para ejecutar:

1. **Clona o descarga el proyecto**
```bash
git clone <repo-url>
cd RepoPython
```

2. **Instala Flask** (única dependencia)
```bash
pip install flask
# o
pip install -r requirements.txt
```

3. **Ejecuta la aplicación**
```bash
python app.py
```

4. **Abre tu navegador** en: `http://localhost:5000`

## 👤 Usuarios de Prueba

| Email | Contraseña | Rol |
|-------|------------|-----|
| `admin@test.com` | `admin123` | Administrador |
| `user@test.com` | `user123` | Usuario |
| `demo@demo.com` | `demo` | Demo |

## 🎯 Funcionalidades

### 🔐 Autenticación
- Login con validación de credenciales
- Sesiones de usuario
- Logout seguro
- Mensajes de error elegantes

### 🎨 Interfaz Visual
- **Glassmorphism**: Efectos de transparencia y desenfoque
- **Gradientes animados**: Backgrounds dinámicos
- **Hover effects**: Interacciones visuales
- **Toggle theme**: Cambio entre modo claro/oscuro
- **Loading states**: Feedback visual durante procesos

### 📱 Responsive Design
- Adaptable a móviles y tablets
- Tipografía escalable
- Layout flexible

## 🛠️ Estructura del Proyecto

```
RepoPython/
├── app.py                 # Aplicación Flask principal
├── requirements.txt       # Dependencias
├── static/
│   ├── style.css         # Estilos principales
│   └── test.html        # Página de prueba estática
├── templates/
│   ├── login.html       # Página de login
│   └── welcome.html     # Dashboard de usuario
└── README.md           # Este archivo
```

## 🔧 Personalización

### Cambiar colores del tema:
Edita las variables CSS en `static/style.css`:
```css
/* Cambia estos valores */
--primary-color: #663399;
--secondary-color: #ff69b4;
--dark-bg: #232526;
```

### Agregar nuevos usuarios:
Modifica el diccionario `USERS` en `app.py`:
```python
USERS = {
    'nuevo@email.com': {
        'password': 'mi_password',
        'name': 'Nuevo Usuario'
    }
}
```

## 🎭 Efectos Visuales Incluidos

- ✅ **Page transitions**: Animaciones de entrada
- ✅ **Form animations**: Efectos en inputs y botones  
- ✅ **Icon animations**: Iconos que rotan y escalan
- ✅ **Button effects**: Transformaciones 3D
- ✅ **Loading spinner**: Spinner personalizado con gradientes
- ✅ **Toast notifications**: Notificaciones deslizantes
- ✅ **Glassmorphism**: Efectos de cristal translúcido
- ✅ **Theme toggle**: Transición suave entre temas

## 📊 Sin Base de Datos

Esta versión **NO requiere base de datos**. Los usuarios están almacenados en memoria para simplicidad. Para producción, considera integrar con:
- SQLite (local)
- PostgreSQL (producción)
- MongoDB (NoSQL)

## 🚀 Próximas Mejoras

- [ ] Dashboard con gráficos
- [ ] Sistema de roles avanzado
- [ ] Recuperación de contraseña
- [ ] Registro de nuevos usuarios
- [ ] API REST
- [ ] Tests automatizados

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Por favor:
1. Fork el proyecto
2. Crea tu rama de feature
3. Commit tus cambios
4. Push a la rama
5. Abre un Pull Request

---

**💡 Tip**: Para desarrollo, la aplicación se ejecuta en modo debug. Para producción, cambia `debug=False` en `app.py`.

¡Disfruta de tu sistema de login moderno! 🎉
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
