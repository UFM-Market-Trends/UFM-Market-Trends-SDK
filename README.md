# UFM Market Trends SDK

## Instalación

Para instalar la versión más reciente, corre el siguiente comando:

`pip install git+https://github.com/UFM-Market-Trends/UFM-Market-Trends-SDK.git`

Para instalar una versión específica, corre el siguiente comando:

`pip install git+https://github.com/UFM-Market-Trends/UFM-Market-Trends-SDK.git@0.0.1`

## Desarrollo

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
