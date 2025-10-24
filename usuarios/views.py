from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirigir a la página de login
    else:
        form = UserCreationForm()
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def inicio(request):
    return render(request, 'usuarios/inicio.html')

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html')

@login_required
def modulos(request):
    return render(request, 'usuarios/modulos.html')

@login_required
def modulo1(request):
    return render(request, 'Modulo/modulo1.html')

@login_required
def modulo2(request):
    return render(request, 'Modulo/modulo2.html')

@login_required
def modulo3(request):
    return render(request, 'Modulo/modulo3.html')

@login_required
def modulo4(request):
    return render(request, 'Modulo/modulo4.html')

@login_required
def modulo5(request):
    return render(request, 'Modulo/modulo5.html')

@login_required
def modulo6(request):
    return render(request, 'Modulo/modulo6.html')

@login_required
def modulo7(request):
    return render(request, 'Modulo/modulo7.html')

 
def login_view(request):
    return render(request, 'inicio/login.html') 
