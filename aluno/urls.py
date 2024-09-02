from django.urls import path

from .views import cadastro_aluno, lista_alunos


urlpatterns = [
    path('', lista_alunos, name='lista_alunos'),
    path("cadastro", cadastro_aluno, name="cadastro_aluno"),
]
