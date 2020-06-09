from django.urls import path
from django.contrib.auth import views as auth_views
from accounts.views import *

app_name = "accounts"

urlpatterns = [
    path('login/',login_view, name='login'),
    path('register/',register_view, name='register'),
    path('logout/',logout_view, name='logout'),
] 
