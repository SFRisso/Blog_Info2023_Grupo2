from django.urls import path
from .views import * 

app_name='Aplicaciones.Comentarios'

urlpatterns = [
    path("agregar_comentario/<int:pk>", AgregarComentario.as_view(), name='agregar_comentario' ),
    path("modificar_comentario/<int:pk>",ModificarComentario.as_view(),name="modificar_comentario"),
    path("eliminar_comentario/<int:pk>",EliminarComentario.as_view(),name="eliminar_comentario"),
]

