# UFM Market Trends SDK

Bienvenido al _Software Development Kit_ (SDK) del reporte semestral de Guatemala de UFM Market Trends. 
Este SDK tiene los siguientes objetivos:

1. Agilizar la colección y procesamiento de datos.
2. Facilitar la delegación de tareas.
3. Reutilizar algoritmos y análises (y garantizar su consistencia).
5. Servir como una herramienta educativa para futuros pasantes de UFM Market Trends en temas de economía, Data Science, e ingeniería de datos.
7. Transferir el conocimiento y experiencia a futuras generaciones de analistas de UFM Market Trends.

## Requerimientos

El código está escrito en el lenguaje de programación Python, versión 3.

## Instalación y uso

Para instalar la versión más reciente, corre el siguiente comando:

`pip install git+https://github.com/UFM-Market-Trends/UFM-Market-Trends-SDK.git`

Para instalar una versión específica, corre el siguiente comando:

`pip install git+https://github.com/UFM-Market-Trends/UFM-Market-Trends-SDK.git@0.0.1`

## Contribuciones

Los cambios y mejoras son bienvenidos. Si quieres proponer uno, debes hacer un  [_pull request_](https://guides.github.com/activities/hello-world/#pr) en este repositorio. Si tienes alguna duda sobre este proceso, o cualquier comentario en general, puedes enviar un correo a jose@tecuntecs.com. Para que un pull request sea aprobado, debe observarse con cuidado la siguiente guía de estilo.

### Guía de estilo
Si bien la naturaleza de este recurso es la investigación económica, nos apegamos a las **mejores prácticas de la ingeniería de software al pie de la letra**:

- El código (e.g., variables, funciones, etc.) debe ser escrito 100% en **inglés**. (Ej. `year` en lugar de `ano`).
- El código debe regirse a la [guía de estilo oficial](https://www.python.org/dev/peps/pep-0008/) de Python, de la cual se destaca:
  - El uso de [_Snake case_](https://en.wikipedia.org/wiki/Snake_case) para nombrar variables y funciones. (Ej. `current_balance`).
  - El uso de _CapWords_ (_upper_ [_Camel case_](https://en.wikipedia.org/wiki/Camel_case)) para nombrar clases (Ej. `DatabaseModel`).
  - El uso de mayúsculas para definir constantes. (Ej. `AGRICULTURE = "agriculture"`)
- Comentarios pueden (y se aconseja) ser escritos en **español**. Se recomienda su uso siempre y cuando sean concisos e informativos. (Ej., `# Cálculo de la variación interanual (acum. 3 meses)`)

### Desarrollo

1. Abre una terminal en tu ordenador desde un folder de tu elección. 
Si no estás familiarizado con el uso de terminales, 
lee este [artículo](https://towardsdatascience.com/terminals-consoles-command-line-for-absolute-beginners-de7853c7f5e8).

2. Clona el repositorio en dicho folder con el siguiente comando:

`git git clone https://github.com/UFM-Market-Trends/UFM-Market-Trends-SDK.git`

Si has tenido éxito, el resultado es una copia del repositorio dentro de un folder 
nombrado `UFM-Market-Trends-SDK`. 

3. Accede al subdirectorio `ufmtrends_sdk` desde tu terminal. 
Posiblemente corriendo la siguiente serie de comandos:

`cd UFM-Market-Trends-SDK`

`cd ufmtrends_sdk`

o simplemente `cd UFM-Market-Trends-SDK/ufmtrends_sdk`

4. Ejecuta el siguiente comando para crear un entorno virtual.
Si no estás familiarizado con los entornos virtuales, lee este
[artículo](https://python.land/virtual-environments/virtualenv).

`python -m venv ./virtual_environment`

5. Activa el entorno virtual corriendo el siguiente comando.

(Linux y MacOS)

`source virtual_environment/bin/activate`

(Windows)

`env\Scripts\activate.bat`

(Cuidado: En Linux y MacOS corres el comando en base al directorio local que 
hemos llamado `virtual_environment`, pero en Windows corres el comando en base 
al script global `env` automáticamente instalado en tu ordenador por el 
comando `venv` en el paso 4.)

* Para instalar las dependencias necesarias y empezar a desarrolar la librería, 
ejecuta el comando `pip install -r requirements.txt`.
* Si añades una dependencia nueva como parte de tu contribución, no olvides 
ejecutar el comando `pip freeze > requirements.txt`. De este modo, 
futuros contribuidores al 
proyecto podran replicar el mismo entorno virtual que utilizaste. 
* Para desactivar el entorno virtual, simplemente ejecuta el 
comando `deactivate` (por obvias razones, este comando solo funciona mientras 
estás dentro del entorno virtual).

## Licencia

UFM Market Trends reserva el copyright ⓒ y propiedad intelectual de este software.
Este paquete se brinda al público bajo la licencia Creative Commons (CC). 
Por favor cita apropiadamente cualquier uso o modificación de este paquete en cualquier 
publicación o uso interno.
