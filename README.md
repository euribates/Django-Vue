## Ejemplo de uso de Django y Vue.js

El proyecto de ejemplo está en la carpeta [./web/](./web).

La presentación está en [./presentacion/](presentacion). Está
disponible en formato Libre-Office y en PDF.

### Para instalar la web

En primer lugar, cambiarnos al directorio `web`:

    cd web

Luego tenemos que preparar un entorno virtual, lo podemos hacer con [pyenv](https://github.com/pyenv/pyenv):

    $ pyenv virtualenv 3.12.4 dj-vue
    $ pyenv activate dj-vue
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
    $ python3 manage.py check

    
Para ejecutar la web, lo de siempre:

    python3 manage.py runserver



