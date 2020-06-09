from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
from patient.models import Notificacao
import os



@login_required
def mapa(request):
    env = os.environ
    GOOGLE_API_KEY = env.get('GOOGLE_API_KEY')
    escolha_notificacao = request.POST.getlist('escolha')
    notificacoes_mapa = get_list_or_404(Notificacao)
    context = {
        'notificacoes_mapa': notificacoes_mapa,
        'escolha_notificacao': escolha_notificacao,
        'google_api_key': GOOGLE_API_KEY
    }
    return render(request, 'mapa.html', context)
