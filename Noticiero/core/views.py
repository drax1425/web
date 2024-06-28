
from django.shortcuts import render, redirect,get_object_or_404
from django.contrib import messages
from .models import *
from .forms import *
from django .core.paginator import Paginator
from django.contrib.auth import logout,login,authenticate
from django.contrib.auth import get_user_model


# Create your views here.
def index(request):
    return render(request, 'core/index.html')


def contacto(request):
    return render(request, 'core/contactos/contacto.html')

def singlenews(request):
    return render(request, 'core/Noticias/singlenews.html')

#Login
def inicio(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            if user.is_staff:
                # Si es administrador, redirigir a la página de inicio de administrador
                return redirect('empleados')
            else:
                # Si es usuario regular, redirigir a la página de inicio de usuario
                return redirect('index')
        else:
            # Manejar el caso de credenciales inválidas
            return render(request, 'core/Login/inicio.html', {'error': 'Credenciales inválidas'})

    return render(request, 'core/Login/inicio.html')

def logout_view(request):
    logout(request)
    return redirect('index')

User = get_user_model()

def registrarse(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.is_staff:
                # Redirigir a la página de administrador
                return redirect('empleados')
            else:
                # Redirigir a la página de usuario regular
                return redirect('index')
    else:
        form = CustomUserCreationForm()
    return render(request, 'core/Login/registrarse.html', {'form': form})

#Planes
def planes(request):
    return render(request, 'core/Subcripciones/planes.html')

#CATEGORIAS

def categorias(request):
    return render(request, 'core/Categorias/Categorias.html')

def tecnologia(request):
    return render(request, 'core/Categorias/subcategorias/tecnologia.html')

def politica(request):
    return render(request, 'core/Categorias/subcategorias/politica.html')

def internacional(request):
    return render(request, 'core/Categorias/subcategorias/internacional.html')

def entretenimiento(request):
    return render(request, 'core/Categorias/subcategorias/entretenimiento.html')

def deporte(request):
    return render(request, 'core/Categorias/subcategorias/deporte.html')

def error404 (request):
    return render(request, 'core/errores/error404.html')


def empleadosadd (request):
    aux = {
        'form' : PeriodistaForm()
    }

    if request.method == 'POST':
        formulario =PeriodistaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Periodista  creado ")
        else:
            aux['form'] = formulario
            messages.error(request,'Error Al Agregar Al Empleado')

    return render(request, 'core/crud/add.html', aux)


def empleadosupdate(request, rut):
    periodista = get_object_or_404(Periodista, rut=rut)
    if request.method == 'POST':
        formulario = PeriodistaForm(request.POST, instance=periodista)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Empleado actualizado correctamente')
            return redirect('empleados') 
        else:
            messages.error(request, 'Error al actualizar el empleado')

    aux = {
        'form': PeriodistaForm(instance=periodista)
    }
    return render(request, 'core/crud/update.html', aux)



def empleadosdelete(request, rut):
    periodista = get_object_or_404(Periodista, rut=rut)
    periodista.delete()
    
    return redirect('empleados') 

    
from django.core.paginator import Paginator

def empleados(request):
    periodista_list = Periodista.objects.all()
    paginator = Paginator(periodista_list, 5) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj  
    }

    return render(request, 'core/crud/listar.html', context)

