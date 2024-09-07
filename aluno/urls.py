from django.urls import path

from .views import cadastrar_aluno, lista_alunos, editar_aluno


urlpatterns = [
    path('', lista_alunos, name='lista_alunos'),
    path("cadastrar", cadastrar_aluno, name="cadastrar_aluno"),
    path('editar/<int:id>/', editar_aluno, name="editar_aluno"),
]
