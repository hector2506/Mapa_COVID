from django.contrib import admin
from django.urls import path,include
from site_mapa.views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('accounts/',include('accounts.urls')),
    # path('core/',include('core.urls')),
    path('paciente/',include('patient.urls')),
    path('site-mapa/',include('site_mapa.urls')),

    # path('mapa_saude/',paciente_list, name='home'),
    # path('mapa_saude/login/',login_view, name='login'),
    # path('mapa_saude/register/',register_view, name='register'),
    # path('mapa_saude/logout/',logout_view, name='logout'),
    # path('mapa_saude/lista_notificacao/',notificacao_list, name='notificacao_list'),
    # path('mapa_saude/novo_paciente/',novo_paciente, name='novo_paciente'),
    # path('mapa_saude/novo_notificacao/',novo_notificacao, name='novo_notificacao'),
    # path('mapa_saude/mapa/',mapa, name='mapa'),
]
