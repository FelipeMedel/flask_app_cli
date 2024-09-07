# Flask APP CLI

Paquete de ayuda para la creación de proyectos Backend de Python con Flask, 
siguiendo una arquitectura de directorios recomendada.

## Tener en cuenta antes de utilizar:

> El paquete fue desarrollado en una versión de Python 3.11

## Como funciona

1. Clona el repositorio
2. Ubicáte en la raíz del proyecto y ejecuta el siguiente comando
   ```bash
   pip install --editable .
   ```
   En caso de no funcionar el comando anterior, ejecuta el setup con el comando ```python```
   ```bash
   python setup.py
   ```
De esta manera, se habrá instalado el paquete de ```flask-app-cli``` de manera global en tu sistema.
Para hacer uso del paquete debes usar siempre el comando ```flask_app_cli```.

Por ejemplo, para crear un proyecto nuevo, debes ejecutar el siguiente comando:

```bash
flask_app_cli  new --name <name_project>
```
### Parámetros adicionales

* **--name** (Requerido) Etiqueta para asignar el nombre del proyecto
* **--root** (Opcional) Etiqueta para asignar el nombre del directorio root de la aplicación ```por defecto: app```
* **--database** (Opcional) Etiqueta para crear la configuración de base de datos ```por defecto: false```
* **--multitenant** (Opcional) Etiqueta para configurar multiple base de datos ```por defecto: false```

## Estructura de directorios del proyecto

Dentro de la estructura de directorios, se crean los archivos ```__init__.py```, como también
el archivo ```.env```, los archivos ```run.py``` y ```wsgi.py```, el archivo de configuración 
de la aplicación y ajustes iniciales para la base de datos.

Una vez se ejecute el comando, recibirá información correspondiente al proceso realizado 
y a las acciones ejecutadas:

```text
El proyecto testPython se a creado correctamente!
Se creó el siguiente directorio en el proyecto./testPython/src
Se ha creado el siguiente archivo../testPython/src/__init__.py
Se ha creado el siguiente archivo../testPython/src/run.py
El archivo ./testPython/src/run.py fue modificado!
...
```
Como también al final del proceso, recibirán una recomendación:

```text
Recomendación:

La solución que brinda Flask App Cli, es una referencia en la arquitectura de directorios,
esto quiere decir, que puedes modificarla y ajustarla según sea la necesidad del proyecto que
acabas de generar.

```

> Tener en cuenta: el proyecto generado cuenta con una estructura de carpetas o directorios,
> no quiere decir, que deba seguir el desarrollo de su proyecto con la estructura generada,
> Puede utilizarla si lo desea, en caso contrario, siéntase libre de modificar la estructura 
> (Agregar, Modificar, Eliminar) según la necesidad de su proyecto.

Y por último, el proceso para correr el proyecto generado, verás el siguiente mensaje:

```text
El proceso de creación del proyecto <name_project> finalizó correctamente!
```
Y debajo, encontrarás unos pasos para ejecutar el proyecto generado.

### Pasos de construcción y ejecución

1. Acceda a la raíz del proyecto:
    ```bash
    cd <name_project>
    ```
2. Crear el entorno virtual: (Recuerda agregar este directorio en el archivo ```.gitignore```)
    ```bash
    python -m venv .venv
    ```
 
3. Activar el entorno virtual: (Windows)
    ```bash
    .venv/Scripts/activate
    ```
   3.1 Activar el entorno virtual: (Linux, Mac):
      ```bash
      source .venv/bin/activate
      ```
   
4. Instalar las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

5. Ejecutar la aplicación:
   ```bash
   python ./src/run.py
   ```

6. El proyecto se ejecutará en: ```http://127.0.0.1:5000```

## Al finalizar los pasos, debera tener en cuenta lo siguiente:

* El proyecto corre en por defecto en el host: ```127.0.0.1```
* El proyecto corre en por defecto en el puerto: ```5000```
* Al ejecutar el proyecto y llamar al servicio raíz este le devolverá un json de esta forma
```json
  {
    "ok": true,
    "message": "Hola Mundo!"
  }
```

También puedes realizar la petición a la siguiente ruta: ```http://127.0.0.1:5000/api/v1/test``` esto
debe arrojar la siguiente respuesta:
```json
  {
    "ok": true,
    "message": "Testing blueprint - Flask App Cli!"
  }
```
Lo que indicará que el registro de rutas por medio de Blueprints funciona correctamente.

## Construir la documentación del API 

Requisitos para generar la documentación:

* Tener instalado [ApiDoc](https://apidocjs.com/) 

El siguiente comando se debe ejecutar dentro de la carpeta ```documentation```

```bash
apidoc -i api_documentation -o dist -f ".*\\.py$" --debug
```

## Creación de modelos

Pendiente por agregar la documentación pertinente para la creación de modelos de migración y
generación de los modelos en el proyecto con SQLAlchemy


Listo, ya puedes continuar con tu desarrollo.

