from django.db import models

# Create your models here.
class Aluno(models.Model):
    CURSO_CHOICES = (
        ('INFORMATICA', 'Informática'),
        ('ALIMENTOS', 'Alimentos'),
        ('APICULTURA', 'Apicultura'),
    )
    
    nome = models.CharField(max_length=255)
    data_nascimento = models.DateField(auto_now_add=True)
    matricula = models.CharField(max_length=255)
    email = models.EmailField()
    endereco = models.CharField(max_length=255)
    curso = models.CharField(max_length=255, choices=CURSO_CHOICES)
