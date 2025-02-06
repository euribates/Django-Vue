from django.shortcuts import render

# Create your views here.

def homepage(request):
    return render(request, 'commons/homepage.html', {
        'titulo': 'Integración Django / Vue3',
        })


def hello(request):
    return render(request, 'commons/hello.html', {
        'titulo': 'Hola Django, Vue3 style (verbatin)',
        })


def hello2(request):
    return render(request, 'commons/hello2.html', {
        'titulo': 'Hola Django, Vue3 style',
        'subtitulo': 'Ahora sin verbatin', 
        })


def counter(request):
    return render(request, 'commons/counter.html', {
        'titulo': 'Contador sencillo',
        })


def counter2(request):
    return render(request, 'commons/counter2.html', {
        'titulo': 'Contador doble',
        })


def model(request):
    return render(request, 'commons/model.html', {
        'titulo': 'Doble vinculación con v-model',
        })


def tareas(request):
    return render(request, 'commons/tareas.html', {
        'titulo': 'Modificación de los datos del modelo',
        })


def login_vanilla(request):
    return render(request, 'commons/login_vanilla.html', {
        'titulo': 'Login (Vanilla js)',
        })


def login_vue(request):
    return render(request, 'commons/login_vue.html', {
        'titulo': 'Login (Con Vue)',
        })
