from django.urls import path
from .views import listar_alunos

urlpatterns = [
    path('', listar_alunos),
]