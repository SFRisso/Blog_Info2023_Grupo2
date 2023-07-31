from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Usuario(AbstractUser):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    foto_perfil = models.ImageField(null=True, blank=True, upload_to='usuarios', default='usuarios/user_default.png') 
    
    COLABORADOR = "CO"
    MIEMBRO = "MI"
    CHOICES = [
        (COLABORADOR, "Colaborador"),
        (MIEMBRO, "Miembro"),
    ]
    tipo_usuario = models.CharField(
        max_length=2,
        choices=CHOICES,
        default=MIEMBRO,
    )
    
    def __str__(self):
        return self.username