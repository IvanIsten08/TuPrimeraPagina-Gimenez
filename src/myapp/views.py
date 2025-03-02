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
