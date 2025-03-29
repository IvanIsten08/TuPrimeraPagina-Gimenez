from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cliente, Post, Categoria
from .formulario import AutorForm, PostForm, ComentarioForm, BuscarPostForm
from . import formulario
# Create your views here.

def saludar(request):
    return HttpResponse("hola desde Django!")

def saludar_con_etiqueta(request):
    return HttpResponse("<h1>hola desde Django con etiquetas!</h1>")

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize() # Capitalizo el nombre
    apellido = apellido.capitalize() # Capitalizo el apellido
    return HttpResponse(f"hola {nombre} {apellido} desde Django con parametros!")

def index(request):
    from datetime import datetime
    time_actual = datetime.now()
    contexto = {
        "time_actual": time_actual}
    return render(request, "myapp/index.html", contexto)

def tirar_dado(request):
    from datetime import datetime
    from random import randint
    
    tiro_de_dado = randint(1, 6)
    
    if tiro_de_dado == 6:
        mensaje = f'Has tirado el dado y has sacado ¡{tiro_de_dado}! ¡FELICIDADES!'
    else:
        mensaje = f'Has tirado el dado y has sacado {tiro_de_dado} Sigue intentandolo. Presiona F5 para volver a tirar.'
    
    datos = {
        'title': 'Tiro de Dados',
        'message': mensaje,
        'fecha': datetime.now().strftime('%H:%M:%S.%f'),
    }
    return render(request, 'myapp/dados.html', context=datos)


def ejercicio_1(request):
    datos_persona = {
        'nombre': 'Ivan',
        'apellido': 'Gimenez',
        'edad': 28,
    }
    return render(request, "myapp/ejercicio1.html", context=datos_persona)

def ejercicio_2(request):
    usuarios = [
        {'nombre': 'Ivan', 'email': 'ivan@example.com'},
        {'nombre': 'Pedro', 'email': 'pedro@example.com'},
        {'nombre': 'Maria', 'email': 'maria@example.com'},
        {'nombre': 'Luis', 'email': 'luis@example.com'},
    ]
    return render(request, "myapp/ejercicio2.html",{'usuarios': usuarios})

def cliente_list(request):
    clientes = Cliente.objects.all()  # Obtiene todos los clientes
    return render(request, 'myapp/cliente_list.html', {'clientes': clientes})

def agregar_autor(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_autor')
    else:
        form = AutorForm()
    return render(request, 'myapp/agregar_autor.html', {'form': form})

def agregar_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_post')
    else:
        form = PostForm()
    return render(request, 'myapp/agregar_post.html', {'form': form})

def agregar_comentario(request):
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('agregar_comentario')
    else:
        form = ComentarioForm()
    return render(request, 'myapp/agregar_comentario.html', {'form': form})

def buscar_post(request):
    form = BuscarPostForm(request.GET)
    posts = []
    if form.is_valid():
        titulo = form.cleaned_data['titulo']
        posts = Post.objects.filter(titulo__icontains=titulo)
    return render(request, 'myapp/buscar_post.html', {'form': form, 'posts': posts})

def inicio(request):
    posts = Post.objects.all()
    return render(request, 'myapp/inicio.html', {'posts': posts})

def categoria_list(request):
    categorias = Categoria.objects.all()
    context = {
        'categorias': categorias}
    return render(request, 'myapp/categoria_list.html', context)

def categoria_create(request):
    if request.method == 'GET':
        form = formulario.CategoriaForm()
    if request.method == 'POST':
        form = formulario.CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('myapp:categoria_list')
    return render(request, 'myapp/categoria_form.html', {'form': form})
