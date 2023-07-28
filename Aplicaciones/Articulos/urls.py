from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 


from .views import * 


app_name='Aplicaciones.Articulos'

urlpatterns = [
    path("agregar_articulo/", AgregarArticulo.as_view(), name='agregar_articulo' ),
    path("modificar_articulo/<int:pk>",ModificarArticulo.as_view(),name="modificar_articulo"),
    path("eliminar_articulo/<int:pk>",EliminarArticulo.as_view(),name="eliminar_articulo"),
    path("", ListarArticulosView.as_view(), name="listar_articulos"),
    path("articulo_detalle/<int:pk>", ArticuloDetalle.as_view(), name='articulo_detalle'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)