from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=50) # Todo lo que tenga Field quiere decir que es un tipo de datos, aqui indica que es de tipo Char y que tiene un maximo de 50 caracteres
    apellido = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.apellido} {self.nombre}"
    
    
class Autor(models.Model):
    nombre = models.CharField(max_length=50)
    email  = models.EmailField()
    
    def __str__(self) -> str:
        return f"{self.nombre} {self.email}"
    
class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha_publicacion = models.DateField()
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.titulo
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    contenido = models.TextField()
    fecha = models.DateField()
    
    def __str__(self) -> str:
        return f"Comentario de {self.nombre} en {self.post.titulo}"
    
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    
    def __str__(self) -> str:
        return self.nombre