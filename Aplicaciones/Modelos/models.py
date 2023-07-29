from django.db import models

# Create your models here.
class usuario(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    email = models.EmailField()
    foto_perfil = models.CharField(max_length=250)
    tipo_usuario = models.DecimalField(max_digits=1, decimal_places=1)

class articulo(models.Model):
    id_usuario = models.ForeignKey("usuario", on_delete=models.PROTECT)
    id_categoria = models.ForeignKey("categoria", on_delete=models.PROTECT)
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=1000)
    localidad = models.CharField(max_length=50)
    fecha_publicacion = models.DateField()
    imagen_portada = models.CharField(max_length=250)
    modalidad = models.CharField(max_length=50)

class comentario(models.Model):
    id_usuario = models.ForeignKey("usuario", on_delete=models.PROTECT)
    id_articulo = models.ForeignKey("articulo", on_delete=models.PROTECT)
    fecha_publicacion = models.DateField()
    fecha_edicion = models.DateField()
    contenido = models.CharField(max_length=500)

class categoria(models.Model):
    
    nombre = models.CharField(max_length=50)
    