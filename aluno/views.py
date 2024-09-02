from django.shortcuts import render

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