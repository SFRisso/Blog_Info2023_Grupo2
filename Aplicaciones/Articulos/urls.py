from django.urls import path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 

from .views import * 


apps_name='aplicaciones.articulos'

urlpatterns = [
    path("agregar_articulo/", AgregarArticulo.as_view(), name='agregar_articulo' ),
    path("modificar_articulo/",ModificarArticulos.as_view(),name="modificar_articulos"),
    path("eliminar_articulo/",EliminarArticulos.as_view(),name="eliminar_articulo"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
