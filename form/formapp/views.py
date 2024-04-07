from django.shortcuts import render, redirect
from .forms import PersonaForm

def formulario(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('formulario_exitoso')
    else:
        form = PersonaForm()
    return render(request, 'formapp/formulario.html', {'form': form})

def formulario_exitoso(request):
    return render(request, 'formapp/formulario_exitoso.html')
