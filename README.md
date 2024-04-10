# Prueba Técnica Accenture

## Setup

Para ejecutar este proyecto en local, ejecuta los siguientes pasos (Linux):

1. Crea un entorno virtual de python: `python3 -m venv venv`
2. Activa el entorno virtual: `source venv/bin/activate`
3. Instala las dependencias: `pip install -r requirements.txt`
4. Ejecuta el servidor: `uvicorn main:app --reload`

Tras realizar los pasos, el servidor debería estar ejecutándose en `http://127.0.0.1:8000` 

## Documentación

Puedes encontrar la documentación de la API en `http://127.0.0.1:8000/docs`  y en `http://127.0.0.1:8000/redoc` 

![image](https://github.com/aritzjl/Accenture-Prueba-Tecnica/assets/129123101/f314feab-d7e0-4bb3-b5b9-5e2e93dc57d2)


## Pruebas

Para comprobar el funcionamiento de la API, puedes utilzar la extensión de **VSCode** llamada `Thunder Client` 

Hacemos un post de prueba
![image](https://github.com/aritzjl/Accenture-Prueba-Tecnica/assets/129123101/c537e602-948c-41cf-b36b-d775bee30222)



Y ahora volvemos a intentar crear otro usuario con el mismo DNI
![image](https://github.com/aritzjl/Accenture-Prueba-Tecnica/assets/129123101/f9946609-c46c-4905-bd92-024063d33970)


