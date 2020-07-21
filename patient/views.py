from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from django import forms
from django.contrib.auth import authenticate, get_user_model, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator, InvalidPage, EmptyPage
from .forms import *
import os

# Create your views here.

def gerenciar_paginacao(request, object_list):
    paginator = Paginator(object_list, 5)
    try:
        page_num = int(request.GET.get('page', '1'))
        if page_num < 1:
            page_num = 1
    except ValueError:
        page_num = 1
    try:
        current_page = paginator.page(page_num)
    except (InvalidPage, EmptyPage):
        current_page = paginator.page(paginator.num_pages)
    return current_page


@login_required
def notificacao_list(request):
    # IF responsável por modificar o campo situação atual
    if request.method == 'POST':
        notificacao = get_object_or_404(Notificacao, id=request.POST['notificacao_valor'])
        notificacao.situacao_atual = request.POST['situacao_notificacao']
        notificacao.save()
    notificacoes = gerenciar_paginacao(request, Notificacao.objects.filter(usuario=request.user).order_by('unidade_saude'))
    lista_notificacoes = Notificacao.objects.all()
    if (notificacoes and lista_notificacoes):
        context = {
            'notificacoes': notificacoes,
        }
    else:
        context = {}
    return render(request, "notification/notificacao_list.html", context)


@login_required
def paciente_list(request):
    pacientes = gerenciar_paginacao(request, Paciente.objects.filter(ubs=request.user.vinculo).order_by('nome'))
    lista_notificacoes = Notificacao.objects.all()
    if (pacientes and lista_notificacoes):
        context = {
            'pacientes': pacientes,
        }
    else:
        context = {}
    return render(request, "patient/home.html", context)


@login_required
def novo_paciente(request):
    if request.method == 'POST':
        form = PacienteRegisterForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)
            user = request.user
            paciente.ubs = user.vinculo
            paciente.save()
            request.session['paciente_cns'] = paciente.cns
            messages.success(
                request, f'Paciente {paciente.nome} registrado com sucesso! Prosseguindo com a notificação:')
            return redirect('patient:novo_notificacao')
    else:
        form = PacienteRegisterForm()
    ubs_mapa = get_list_or_404(Estabelecimento)
    env = os.environ
    GOOGLE_API_KEY = env.get('GOOGLE_API_KEY')
    context = {
        'ubs_mapa': ubs_mapa,
        'google_api_key': GOOGLE_API_KEY,
        'form': form
    }
    return render(request, 'patient/novo_paciente.html', context)


@login_required
def novo_notificacao(request):
    if request.method == 'POST':
        notificacao_form = NotificacaoForm(request.POST)
        if notificacao_form.is_valid():
            if(request.session.get('paciente_cns')):
                notificacao = notificacao_form.save(commit=False)
                paciente_notificacao = get_object_or_404(Paciente, cns=request.session.get('paciente_cns'))
                user = request.user
                notificacao.usuario = user
                notificacao.paciente = paciente_notificacao
                notificacao.save()
                del request.session['paciente_cns']
                messages.success(
                    request, f'{user.nome}, notificação realizada com sucesso!')
                return redirect('patient:notificacao_list')
            else:
                notificacao = notificacao_form.save(commit=False)
                user = request.user
                notificacao.usuario = user
                notificacao.save()
                messages.success(
                    request, f'{user.nome}, notificação realizada com sucesso!')
                return redirect('patient:notificacao_list')
    else:
        notificacao_form = NotificacaoForm()
        lista_ubs = Estabelecimento.objects.all()
    if(request.session.get('paciente_cns')):
        context = {
            'notificacao_form': notificacao_form,
            'paciente_cns': get_object_or_404(Paciente, cns=request.session.get('paciente_cns')),
            'lista_ubs': lista_ubs
        }
    else:
        context = {
            'notificacao_form': notificacao_form,
            'lista_ubs': lista_ubs
        }
    return render(request, 'notification/novo_notificacao.html', context)
    
