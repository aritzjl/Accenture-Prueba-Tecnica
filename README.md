# Prueba Técnica Accenture

## Setup

Para ejecutar este proyecto en local, ejecuta los siguientes pasos (Linux):

1. Crea un entorno virtual de python: `python3 -m venv venv`
2. Activa el entorno virtual: `source venv/bin/activate`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecuta el servidor: `uvicorn main:app --reload`

Tras realizar los pasos, el servidor debería estar ejecutandose en `http://127.0.0.1:8000` 

## Documentación

Puedes encontrar la documentación de la API en `http://127.0.0.1:8000/docs`  y en `http://127.0.0.1:8000/redoc` 

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dca3253-0e96-4032-821c-b20545e84ed2/672f8a0c-27e3-4546-b779-b04610c98b0f/Untitled.png)

## Pruebas

Para comprobar el funcionamiento de la API, puedes utilzar la extensión de **VSCode** llamada `Thunder Client` 

Hacemos un post de prueba

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dca3253-0e96-4032-821c-b20545e84ed2/90a2c384-0059-4ee5-abf9-dc1a3114d3f8/Untitled.png)

Y ahora volvemos a intentar crear otro usuario con el mismo DNI

![Untitled](https://prod-files-secure.s3.us-west-2.amazonaws.com/6dca3253-0e96-4032-821c-b20545e84ed2/5f6d27d2-0fb6-40b2-b0e8-9b73e2e08831/Untitled.png)
