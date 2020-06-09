from multiselectfield import MultiSelectField
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from datetime import date
from accounts.models import *

# Create your models here.

class Paciente(models.Model):
    sexo = [
        ("Masculino", "Masculino"),
        ("Feminino", "Feminino"),
        ("Ignorado", "Ignorado")
    ]
    gestacao = [
        ("1", "1º Trimestre"),
        ("2", "2º Trimestre"),
        ("3", "3º Trimestre"),
        ("4", "Idade gestacional ignorada"),
        ("5", "Não"),
        ("6", "Não se aplica"),
        ("9", "Ignorado")
    ]
    uf = [
        ("RO","Rondônia"),("AC","Acre"),("AM","Amazonas"),("RR","Roraima"),("PA","Pará"),("AP","Amapá"),("TO","Tocantins"),
        ("MA","Maranhão"),("PI","Piauí"),("CE","Ceará"),("RN","Rio Grande do Norte"),("PB","Paraíba"),("PE","Pernambuco"),
        ("AL","Alagoas"),("SE","Sergipe"),("BA","Bahia"),("MG","Minas Gerais"),("ES","Espírito Santo"),("RJ","Rio de Janeiro"),
        ("SP","São Paulo"),("PR","Paraná"),("SC","Santa Catarina"),("RS","Rio Grande do Sul"),("MS","Mato Grosso do Sul"),
        ("MT","Mato Grosso"),("GO","Goiás"),("DF","Distrito Federal"),
    ]
    ubs = models.ForeignKey(Estabelecimento, related_name='paciente_ubs', on_delete=models.CASCADE, default=None,null=True)
    cns = models.CharField('CNS', unique=True, max_length=15, default=None)
    nome = models.CharField(max_length=50)
    sexo = models.CharField(max_length=25, choices=sexo, default="Ignorado")
    data_nascimento = models.DateField(auto_now=False, auto_now_add=False, default=None)
    ocupacao = models.CharField(max_length=50, default=None)
    gestacao = models.CharField(max_length=25, choices=gestacao, default="9")
    uf = models.CharField(max_length=25, choices=uf, default="PI")
    municipio = models.CharField(max_length=25, default=None)
    cep = models.CharField(max_length=8,default=None)
    def __str__(self):
        return self.nome

class Notificacao(models.Model):
    SINAIS_CLÍNICOS = ((1, 'Tosse'),
               (2, 'Febre'),
               (3, 'Cansaço'),
               (4, 'Congestão Nasal'),
               (5, 'Diarreia'),
               (6, 'Dores corporais'),
               (7, 'Dificuldade para respirar'))
               
    DOENCAS_PRE_EXISTENTES = ((1, 'Diabetes'),
               (2, 'Doenças Cardiovasculares'),
               (3, 'Doenças Respiratórias'),
               (4, 'Doenca Renal Cronica'),
               (5, 'Hipertensao Arterial'))

    situacao = [
        ("Suspeito", "Suspeito"),
        ("Confirmado", "Confirmado"),
        ("Curado", "Curado"),
        ("Óbito", "Óbito")
    ]
    usuario = models.ForeignKey(User, related_name='agravo_usuario', on_delete=models.CASCADE, default=None)
    paciente = models.ForeignKey(Paciente, related_name='paciente_notificacao', on_delete=models.CASCADE, default=None)
    unidade_saude = models.ForeignKey(Estabelecimento, related_name='unidade_saude', on_delete=models.CASCADE, default=None)
    data_primeiros_sintomas = models.DateField(default=None)
    data_notificacao = models.DateField(default=date.today) 
    sinais_clinicos = MultiSelectField(choices=SINAIS_CLÍNICOS, default=None)
    doencas_pre_existentes = MultiSelectField(choices=DOENCAS_PRE_EXISTENTES, default=None)
    situacao_atual = models.CharField(max_length=25, choices=situacao, default='Suspeito')

    def __str__(self):
        return ("Notificação " + str(self.id))