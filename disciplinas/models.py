from django.db import models

class Disciplina(models.Model):
    nome = models.CharField(max_length=200)
    codigo = models.CharField(max_length=50, unique=True)
    professor = models.CharField(max_length=200)
    periodo = models.CharField(max_length=20)