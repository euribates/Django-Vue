## Ejemplo de uso de Django y Vue.js

El proyecto de ejemplo esta en la carpeta [./web/](./web).

La presentación esta en [./presentacion/presentacion-django-vue.odp](En formato
Libre-Office).

### Para instalar la web

En primer lugar, cambiarnos al directorio `web`:

    cd web

Luego tenemos que preparar un entorno virtual, lo podemos hacer con pyenv:

    $ pyenv virtualenv 3.12.4 dj-vue
    $ pyenv activate dj-vue
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
    $ python3 manage.py check

    
Para ejecutar la web, lo de siempre:

    python3 manage.py runserver



