from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
  path(''       , views.index,  name='index'),
  path('comissoes/', views.comissoes, name='comissoes'),
  # path('produtos/', views.produtos, name='produtos'),
  # path('comissoes_btg/', views.comissoes_btg, name='comissoes_btg'),
  # path('comissoes_aai/', views.comissoes_aai, name='comissoes_aai'),
]
