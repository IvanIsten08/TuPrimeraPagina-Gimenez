from django.shortcuts import render
from django.http import HttpResponse
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
    time_actual = datetime.now().year
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