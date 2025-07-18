# Sesion 2 Github

Git es el sistema de control de versiones distribuido de código abierto que facilita las actividades de GitHub en tu laptop o computadora de escritorio. Esta hoja de referencia resume las instrucciones de línea de comandos de Git más utilizadas para una consulta rápida.

## Instalación

**GitHub para Windows** https://windows.github.com

**GitHub para Mac** https://mac.github.com

**Git para Todas las Plataformas** http://git-scm.com

_Las distribuciones de Git para sistemas Linux y POSIX están disponibles en el sitio web oficial de Git SCM._

## Configurar herramientas

Configura la información de usuario para todos los repositorios locales:

```bash
$ git config --global user.name "[nombre]"
# Establece el nombre que quieres adjuntar a tus commits

$ git config --global user.email "[correo electrónico]"
# Establece el correo electrónico que quieres adjuntar a tus commits

$ git config --global color.ui auto
# Habilita la coloración útil de la salida de línea de comandos
```

## Crear repositorios

Al comenzar con un nuevo repositorio, solo necesitas hacerlo una vez, ya sea localmente para luego subirlo a GitHub, o clonando un repositorio existente:

```bash
$ git init
# Convierte un directorio existente en un repositorio git

$ git clone [url]
# Clona (descarga) un repositorio que ya existe en GitHub, incluyendo todos los archivos, ramas y commits
```

## El archivo .gitignore

A veces puede ser una buena idea excluir archivos para que no sean rastreados con Git. Esto se hace típicamente en un archivo especial llamado `.gitignore`.

Puedes encontrar plantillas útiles para archivos `.gitignore` en github.com/github/gitignore.

## Ramas

Las ramas son una parte importante del trabajo con Git. Cualquier commit que hagas será en la rama en la que actualmente estés "checked out". Usa `git status` para ver cuál es esa rama.

```bash
$ git branch [nombre-rama]
# Crea una nueva rama

$ git checkout [nombre-rama]
# Cambia a la rama especificada y actualiza el directorio de trabajo

$ git merge [rama]
# Combina el historial de la rama especificada en la rama actual.
# Esto se suele hacer en solicitudes de extracción (pull requests),
# pero es una operación importante de Git.

$ git branch -d [nombre-rama]
# Elimina la rama especificada
```

## Sincronizar cambios

Sincroniza tu repositorio local con el repositorio remoto en GitHub.com:

```bash
$ git fetch
# Descarga todo el historial de las ramas de seguimiento remotas

$ git merge
# Combina la rama de seguimiento remoto en la rama local actual

$ git push
# Sube todos los commits de la rama local a GitHub

$ git pull
# Actualiza tu rama de trabajo local actual con todos los nuevos commits
# de la rama remota correspondiente en GitHub
# `git pull` es una combinación de `git fetch` y `git merge`
```

## Hacer cambios

Examina e inspecciona la evolución de los archivos del proyecto:

```bash
$ git log
# Muestra el historial de versiones para la rama actual

$ git log --follow [archivo]
# Muestra el historial de versiones para un archivo, incluyendo renombres

$ git diff [primera-rama]...[segunda-rama]
# Muestra las diferencias de contenido entre dos ramas
```
