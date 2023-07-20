
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('articulos/', include('Aplicaciones.Articulos.urls')),

]
