from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login 
from django.contrib.admin.views.decorators import staff_member_required 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse 
from .models import Libro
from .forms import LibroForm 

# Create your views here. 

@login_required
@staff_member_required 
def inicio(request):
    return render(request, 'paginas/inicio.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('inicio')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')  

    return render(request, 'paginas/login.html')

@login_required 
@staff_member_required
def info(request):
    return render(request, "paginas/info.html") 

@login_required 
@staff_member_required
def libros(request): 
    libros = Libro.objects.all() 
    return render(
        request, 
        "libros/index.html", 
        {"libros":libros}
        ) 

def crear(request):
    form = LibroForm(request.POST or None, request.FILES or None)  
    if form.is_valid():
        form.save() 
        return redirect('libros')
    
    return render( 
        request, 
        "libros/crear.html", 
        {"form":form} 
        ) 

def edicion(request, id):
    libro = Libro.objects.get(id=id)
    return render(request, 'libros/edicion.html', {"libro":libro})

def editar(request):
    id = request.POST['numId'] 
    titulo = request.POST['txtTitulo'] 
    descripcion = request.POST['txtDescripcion'] 

    libro = Libro.objects.get(id=id) 

    imagen_nueva = request.FILES.get('imgFoto') 

    if imagen_nueva:
        libro.imagen = imagen_nueva

    libro.titulo = titulo 
    libro.descripcion = descripcion 
    libro.save() 
    return redirect('libros')

def eliminar(request, id):
    libro = Libro.objects.get(id=id) 
    libro.delete() 
    return redirect('libros') 

















