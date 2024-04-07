# L3Entrega2


# Tutorial para Crear un Formulario en Django

En este tutorial, aprenderemos a crear un formulario web utilizando Django, un framework de desarrollo web en Python. El formulario tendrá estilos utilizando CSS para mejorar la apariencia.

## Requisitos Previos

- Python instalado en tu sistema.
- Conocimientos básicos de HTML, CSS y Python.

## Paso 1: Configuración del Entorno Virtual

1. Crea un nuevo directorio para tu proyecto.
2. Abre una terminal en el directorio creado.
3. Ejecuta los siguientes comandos para configurar un entorno virtual:

    ```bash
    python -m venv venv
    ```

4. Activa el entorno virtual:

    - En Windows:

    ```bash
    venv\Scripts\activate
    ```

    - En macOS/Linux:

    ```bash
    source venv/bin/activate
    ```

## Paso 2: Instalación de Django y Creación del Proyecto

1. Instala Django usando pip:

    ```bash
    pip install django
    ```

2. Crea un nuevo proyecto Django:

    ```bash
    django-admin startproject mi_proyecto
    ```

3. Ingresa al directorio del proyecto:

    ```bash
    cd mi_proyecto
    ```

## Paso 3: Creación de la Aplicación y Configuración de la Base de Datos

1. Crea una nueva aplicación dentro del proyecto:

    ```bash
    python manage.py startapp formapp
    ```

2. Agrega la aplicación al archivo de configuración `settings.py`.

3. Realiza las migraciones necesarias para configurar la base de datos:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

## Paso 4: Creación del Modelo y Formulario

1. Define el modelo de Django en `models.py` dentro de la aplicación.

2. Crea un formulario utilizando el modelo en `forms.py`.

## Paso 5: Creación de las Vistas y Plantillas

1. Define las vistas necesarias en `views.py`.

2. Crea las plantillas HTML en el directorio `templates` de la aplicación.

3. Agrega estilos CSS para mejorar la apariencia de los formularios.

## Paso 6: Configuración de las URL

1. Define las URL para las vistas en `urls.py` dentro de la aplicación.

2. Incluye las URL de la aplicación en el archivo de configuración `urls.py` del proyecto.

## Paso 7: Ejecución del Servidor

1. Ejecuta el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

2. Abre tu navegador y visita `http://127.0.0.1:8000/` para ver el formulario en acción.

