from django.db import models
from Aplicaciones.Usuarios.models import Usuario
from django.utils import timezone


# Create your models here.
class Articulo(models.Model):
    usuario = models.ForeignKey("Usuarios.Usuario", on_delete=models.PROTECT)
    categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=1000)
    localidad = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(default= timezone.now)
    imagen_portada = models.ImageField(null=True,blank=True,upload_to="portada")
    modalidad = models.CharField(max_length=50)
    
    def __str__(self):
        return self.titulo
    
class Categoria(models.Model): 
    nombre = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre