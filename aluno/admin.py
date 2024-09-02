from django.contrib import admin

from .models import Aluno

# Register your models here.
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'email', 'curso')
    list_filter = ('nome', 'matricula', 'email', 'curso')
