from django.contrib import admin
from django.urls import path,include
from .views import *
from django.contrib.auth import views as auth_views

app_name = "patient"

urlpatterns = [
    path('lista',paciente_list, name='home'),
    path('novo-paciente/',novo_paciente, name='novo_paciente'),
    path('lista-notificacao/',notificacao_list, name='notificacao_list'),
    path('novo-notificacao/',novo_notificacao, name='novo_notificacao'),
]
