from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=200)
    ra = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    curso = models.CharField(max_length=100)