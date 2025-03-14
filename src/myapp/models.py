from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50) # Todo lo que tenga Field quiere decir que es un tipo de datos, aqui indica que es de tipo Char y que tiene un maximo de 50 caracteres
    apellido = models.CharField(max_length=50)
    