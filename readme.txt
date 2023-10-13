# UrbanPathGen

Bienvenido a la documentación de UrbanPathGen, una herramienta para generar trayectorias de drones en entornos urbanos.

## Tabla de Contenidos

- [Configuración y Uso](#configuración-y-uso)
  - [Instalación](#instalación)
  - [Estructura del Repositorio](#estructura-del-repositorio)
- [Ejemplos de Uso](#ejemplos-de-uso)
  - [example](#example)
  - [generate_one_image](#generate_one_image)
- [Licencia](#licencia)

## Configuración y Uso

En este capítulo se describe la puesta en marcha y utilización de UrbanPathGen.

### Instalación

Para la instalación de UrbanPathGen, se deben seguir los siguientes pasos:

1. Instalar Python junto con el instalador pip desde [Python]. Se debe corroborar que la versión instalada soporte PyTorch, esto se puede verificar desde [PyTorch]. Para el desarrollo de UrbanPathGen, se utilizó Python 3.10.
2. Clonar el repositorio de UrbanPathGen, el cual se puede encontrar en [UrbanPathGen].
3. Seguir las instrucciones de instalación de CUDA, detalladas en [CUDA].
4. Seguir las instrucciones de instalación de PyTorch, detalladas en [PyTorch].
5. Instalar los paquetes necesarios para el programa. Para esto, se puede ejecutar el comando `pip install -r requirements.txt` desde la carpeta raíz de UrbanPathGen.
6. Descargar el modelo de MiDaS a utilizar. Para esto, dirigirse a la carpeta `Trajectory Generation/torch_models` y ejecutar el script `force_refresh_model.py`. El modelo que viene configurado por defecto es `DPT_Hybrid`, sin embargo, se pueden seleccionar otros modelos disponibles, los cuales se pueden ver en el archivo `see_available_models.py`.

### Estructura del Repositorio

Al entrar en el repositorio, se encuentran dos carpetas:

#### Registro de Pruebas

Esta carpeta contiene el registro de pruebas realizadas para el desarrollo. Además de dos scripts:

- `calc_average_time`: Permite ingresar la salida de la consola y calcular el tiempo medio de análisis para cada iteración en una ejecución.
- `graph`: Se utiliza para graficar datos, en este caso, una lista de tiempos promedio en función de la cantidad de drones.

#### Trajectory Generation

Es la carpeta que contiene todo el desarrollo de UrbanPathGen. Además de todos los archivos necesarios para su ejecución, los cuales se explicaron previamente, contiene las siguientes carpetas:

- `image_analysis`: En esta carpeta, se guarda la salida generada por el script `generate_one_image`.
- `old_methods`: Contiene métodos obsoletos para el cálculo de trayectorias. Se puede ignorar.
- `test_images`: Permite cargar imágenes de prueba para el programa.
- `test_videos`: Permite cargar videos de prueba para el programa.
- `tmp_images`: Guarda temporalmente los archivos generados por el script `generate_one_image`.
- `torch_models`: Contiene scripts que permiten cargar un modelo y verificar los modelos y transformaciones existentes.
- `video_frames`: En esta carpeta se guardan los frames de los flujos de video existente en caso de que la opción esté activada.

Además, en la carpeta `Trajectory Generation` se encuentran dos archivos, `example` y `generate_one_image`, los cuales corresponden a los casos de uso posibles, los cuales se explican en la documentación.

## Ejemplos de Uso

### example

Este archivo contiene los datos necesarios para la ejecución del programa. Para esta ejecución, se debe crear una instancia de dron por cada dron real disponible. Para esto, se define una lista llamada `drones` que contiene las instancias de cada uno de los drones. Las instancias se definen con los atributos indicados en la sección "Clase UAV". Algunos de estos atributos corresponden a parámetros de hardware, los cuales deben ser indicados en función de los equipos disponibles.

### generate_one_image

Este módulo genera una imagen compuesta por la imagen original, la estimación de profundidad de dicha imagen y las rutas identificadas en la imagen.

## Licencia

Este proyecto se distribuye bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).