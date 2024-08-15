# Flask APP CLI

Paquete de ayuda para la creacion de proyectos Backend de Python con Flask, 
siguiendo una arquitectura de directorios recomendada.

## Tener en cuenta antes de utilizar:

> El paquete fue desarrollado en una versión de Python 3.11 y testeado con versiones anteriores

## Como funciona

Basta con instalar el paquete de ```flask-app-cli``` de manera global en tu sistema 
y ejecutar el comando ```new-project``` para crear el directorio principal de tu 
proyecto, se debe ejecutar de la siguiente manera:

```bash
flask-app-cli new-project --name testPython
```
### Parametros adicionales

* **--name** Etiqueta para asignar el nombre del proyecto
* **--root** Etiqueta para asignar el nombre del directorio root de la aplicación, por defecto es ```app```

## Estructura de directorios del proyecto

Dentro de la estructura de directorios, se crean los archivos ```__init__.py```, como tambien
el archivo ```.env```, los archivos ```run.py``` y ```wsgi.py```, el archivo de configuracion 
de la aplicacion y ajustes iniciales para la base de datos.

Una vez se ejecute el comando, recibirá informacion correspondiente al proceso realizado 
y a las acciones ejecutadas:

```text
El proyecto testPython se a creado correctamente!
Se creó el siguiente directorio en el proyecto./testPython/src
Se ha creado el siguiente archivo../testPython/src/__init__.py
Se ha creado el siguiente archivo../testPython/src/run.py
El archivo ./testPython/src/run.py fue modificado!
...
```
Como tambien al final el proceso una recomendacion:

```text
Recomendación:

La solución que brinda Flask App Cli, es una referencia en la arquitectura de directorios,
esto quiere decir, que puedes modificarla y ajustarla según sea la necesidad del proyecto que
acabas de generar.

```

> Tener en cuenta: el proyecto generado cuenta con una estructura de carpetas o directorios,
> no quiere decir, que deba seguir el desarrollo de su proyecto con la estructura generada,
> Puede utilizarla si lo desea, en caso contrario, sientase libre de modificar la estructura 
> (Agregar, Modificar, Eliminar) según la necesidad de su proyecto.

Y por ultimo, el proceso para correr el proyecto generado:

```text
El proceso de creación del proyecto testPython finalizó correctamente!

Acceda a la raíz del proyecto:
cd testPython
Crear el entorno virtual: (Recuerda agregar este directorio en el archivo .gitignore)
python -m venv .venv
Activar el entorno virtual: (Windows)
.venv/Scripts/activate
Instalar las dependencias:
pip install -r requirements.txt
```
## Al finalizar los pasos, debera tener en cuenta lo siguiente:

* El proyecto corre en por defecto en el host: ```127.0.0.1```
* El proyecto corre en por defecto en el puerto: ```5000```
* Al ejecutar el proyecto y llamar al servicio raiz este le devolvera un json de esta forma
  ```json
  {
    "ok": true,
    "message": "Hola Mundo!"
  }
  ```
Listo, ya puedes continuar con tu desarrollo.

