# RestDjango

## Django Rest Framework
https://www.django-rest-framework.org/


- pip install django
- pip install djangorestframework
- pip freeze > requirements.txt

## Configurando rest-framework

Para enlazar django-rest-framework al proyecto debemos ingresar a la carpeta del proyecto y al final de APPs agregar 'rest_framework' 

### Apuntes
🟢 Qué añade Django RF para desarrollar API's

Django REST agrega funcionalidades clave que hacen más fácil el desarrollo de APIs robustas, escalables y fácil de mantener:

Estructura del Proyecto: Crea una carpeta api/ en tu app para organizar serializers, views y routers.
Serializers: Usa ModelSerializer para simplificar la creación de serializers y validar datos.
Vistas y Rutas: Utiliza vistas basadas en clases y routers para manejar operaciones CRUD de manera eficiente.
Autenticación y Permisos: Configura el sistema de autenticación y establece permisos adecuados para controlar el acceso.
Throttling: Implementa throttling para proteger tu API y garantizar acceso justo.
Documentación: Genera documentación interactiva con herramientas como Swagger o Redoc.
Pruebas: Escribe pruebas automatizadas usando APITestCase para asegurar el correcto funcionamiento de la API.
Versionado: Considera implementar un esquema de versionado para manejar cambios futuros.
Manejo de Errores: Utiliza las excepciones de DRF para ofrecer respuestas coherentes en caso de errores.

