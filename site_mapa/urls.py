from django.contrib import admin
from django.urls import path,include
from site_mapa.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [

    path('mapa/',mapa, name='mapa'),
]
