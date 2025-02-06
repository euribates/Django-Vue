from django.contrib import admin
from django.urls import path

import commons.views

urlpatterns = [
    path("", commons.views.homepage),
    path("hello/", commons.views.hello, name='hello'),
    path("hello2/", commons.views.hello2, name='hello2'),
    path("counter/", commons.views.counter, name='counter'),
    path("counter2/", commons.views.counter2, name='counter2'),
    path("model/", commons.views.model, name='model'),
    path("tareas/", commons.views.tareas, name='tareas'),
    path("login/vanilla/", commons.views.login_vanilla, name="login_vanilla"),
    path("login/vue/", commons.views.login_vue, name="login_vue"),
]
