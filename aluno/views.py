from django.shortcuts import render, get_object_or_404, redirect

from .models import Aluno
from .forms import AlunoForm

# Create your views here.
def cadastro_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AlunoForm()
    
    context = {
        'form': form,
    }

    return render(request, 'cadastro_aluno.html', context)

def lista_alunos(request):
    alunos = Aluno.objects.all()
    return render(request, 'lista_alunos.html', {'alunos': alunos})

def editar_aluno(request, id):
    aluno = get_object_or_404(Aluno, id=id)
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            return redirect('lista_alunos')
    else:
        form = AlunoForm(instance=aluno)
    
    context = {
        'form': form,
    }
    return render(request, 'cadastro_aluno.html', context)
