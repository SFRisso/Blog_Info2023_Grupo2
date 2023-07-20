from django.db import models
#from aplicaciones.usuarios.models import Usuarios
#from aplicaciones.categorias.models import Categorias
from django.utils import timezone


# Create your models here.
class Articulos(models.Model):
    id_articulo=models.CharField(primary_key=True, null=False,unique=True,max_length=20)

    #id_usuario=models.ForeignKey(Usuarios, on_delete=models.SET_NULL, null=True)
    
    #id_categoria=models.ForeignKey(Categorias,on_delete=models.SET_NULL, null=True) #DUDA
    
    titulo=models.CharField(max_length=50,null=False)
    contenido=models.TextField(verbose_name="Agrega información",null=False)
    localidad=models.TextField(verbose_name="Ingrese su localidad")
    fecha_publicacion=models.DateField(default=timezone.now)
    portada=models.ImageField(null=True,blank=True,upload_to="portada")
    modalidad=models.CharField(null=False, max_length=20)

    def __str__(self):
        return self.titulo
    