from django.contrib import admin
from .models import usuario, articulo, comentario, categoria

# Register your models here.

admin.site.register(usuario)
admin.site.register(articulo)
admin.site.register(comentario)
admin.site.register(categoria)