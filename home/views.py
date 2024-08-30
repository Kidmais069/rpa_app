from django.shortcuts import render, redirect
from admin_datta.forms import RegistrationForm, LoginForm, UserPasswordChangeForm, UserPasswordResetForm, UserSetPasswordForm
from django.contrib.auth.views import LoginView, PasswordChangeView, PasswordResetConfirmView, PasswordResetView
from django.views.generic import CreateView
from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

from .models import *

import pandas as pd
import os


@login_required(login_url='/accounts/login/')
def index(request):

  context = {
    'segment'  : 'index',
    #'products' : Product.objects.all()
  }
  return render(request, "pages/index.html", context)

# @login_required(login_url='/accounts/login/')
# def comissoes(request):
#   context = {
#     'segment': 'comissoes'
#   }
#   return render(request, "pages/dynamic-tables.html", context)

@login_required(login_url='/accounts/login/')
def comissoes(request):
    # df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=['a', 'b', 'preco']))
    df = pd.read_csv(os.path.join(os.path.dirname(__file__), 'movimentacoes.csv'))

    context = {
        'titulo_pagina': 'Análise de Produtos',
        'indicadores': [
            {'titulo': 'Total de Produtos', 'valor': len(df)},
            # {'titulo': 'Média de Preço', 'valor': f'R$ {df["Valor unitário"].mean():.2f}'},s
            {'titulo': 'Quantidade de clientes', 'valor': f'{df["Código do Cliente"].nunique():.0f}'},
            {'titulo': 'Volume Operado', 'valor': f'{df["Volume Operado"].sum():.2f}'},
            {'titulo': 'Corretagem Total', 'valor': f'{df["Corretagem AAI"].sum():.2f}'},
            # Adicione mais indicadores conforme necessário
        ],
        'colunas_dataframe': df.columns.tolist(),
        'dados_dataframe': df.values.tolist(),
    }
    return render(request, "pages/dynamic-tables.html", context)

@login_required(login_url='/accounts/login/')
def produtos(request):
  context = {
    'segment': 'comissoes'
  }
  return render(request, "pages/dynamic-tables.html", context)

# @login_required(login_url='/accounts/login/')
# def comissoes_btg(request):
#   context = {
#     'segment': 'comissoes'
#   }
#   return render(request, "pages/dynamic-tables.html", context)

# @login_required(login_url='/accounts/login/')
# def comissoes_aai(request):
#   context = {
#     'segment': 'comissoes'
#   }
#   return render(request, "pages/dynamic-tables.html", context)
