from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns 
from .views import RegistarUsuario
from django.contrib.auth.views import LoginView, LogoutView

app_name='Aplicaciones.Usuarios'

urlpatterns = [
    path("registrar/", RegistarUsuario.as_view(), name='registrar_usuario' ),
    path('iniciar_sesion/', LoginView.as_view(template_name="UsuariosTemplates/login.html"), name='iniciar_sesion'),
    path('cerrar_sesion/', LogoutView.as_view(), name='cerrar_sesion'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)