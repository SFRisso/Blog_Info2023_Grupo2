from django.db import models
from Aplicaciones.Usuarios.models import Usuario 
from Aplicaciones.Articulos.models import Articulo
from django.utils import timezone

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey("Usuarios.Usuario", on_delete=models.CASCADE)
    articulo = models.ForeignKey("Articulos.Articulo", on_delete=models.CASCADE)
    fecha_publicacion = models.DateTimeField(default= timezone.now)
    fecha_edicion = models.DateTimeField(null=True)
    texto = models.TextField(verbose_name='Comentario')