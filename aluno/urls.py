from django.urls import path

from .views import cadastro_aluno, lista_alunos, editar_aluno


urlpatterns = [
    path('', lista_alunos, name='lista_alunos'),
    path("cadastro", cadastro_aluno, name="cadastro_aluno"),
    path('editar/<int:id>/', editar_aluno, name="editar_aluno"),
]
