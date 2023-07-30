from django.db import models
from Aplicaciones.Usuarios.models import Usuario 
from Aplicaciones.Articulos.models import Articulo
from django.utils import timezone

# Create your models here.
class Comentario(models.Model):
    usuario = models.ForeignKey("Usuarios.Usuario", on_delete=models.PROTECT)
    articulo = models.ForeignKey("Articulos.Articulo", on_delete=models.PROTECT)
    fecha_publicacion = models.DateTimeField(default= timezone.now)
    fecha_edicion = models.DateTimeField(null=True)
    contenido = models.CharField(max_length=500)