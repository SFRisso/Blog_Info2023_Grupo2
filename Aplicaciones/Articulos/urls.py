from django.urls import path
from .views import * 

apps_name='aplicaciones.articulos'

urlpatterns = [
    path("agregar_articulo/", AgregarArticulo.as_view(), name='agregar_articulo' ),
    path("modificar_articulo/",ModificarArticulos.as_view(),name="modificar_articulos"),
    path("eliminar_articulo/",EliminarArticulos.as_view(),name="eliminar_articulo"),
]