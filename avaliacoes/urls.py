from django.urls import path
from .views import listar_avaliacoes, listar_avaliacoes_pendentes

urlpatterns = [
    path('', listar_avaliacoes),
    path('pendentes/', listar_avaliacoes_pendentes),
]

from django.urls import path
from .views import listar_avaliacoes, listar_avaliacoes_pendentes, resumo_disciplinas

urlpatterns = [
    path('', listar_avaliacoes),
    path('pendentes/', listar_avaliacoes_pendentes),
    path('resumo/', resumo_disciplinas), 
]