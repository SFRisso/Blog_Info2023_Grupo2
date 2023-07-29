from django.urls import path
from .views import *


app_name = 'articulos'

urlpatterns = [
    path('', ListaArticulos.as_view(), name = 'index'),
]
