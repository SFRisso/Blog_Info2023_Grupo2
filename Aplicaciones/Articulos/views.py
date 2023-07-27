"from django.http import HttpResponse"
from django.shortcuts import render
from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class AgregarArticulo(CreateView):
    model=Articulo
    #field usuario temporalmente hasta que este el registro/login hecho
    fields=["usuario","titulo","contenido","localidad","imagen_portada","modalidad","categoria"]
    template_name= "ArticulosTemplates/agregar_articulo.html"
    success_url= reverse_lazy('listar_articulos')


class ModificarArticulos(UpdateView):
    model=Articulo
    #field usuario temporalmente hasta que este el registro/login hecho
    fields=["usuario","titulo","contenido","localidad","imagen_portada","modalidad","categoria"]
    template_name= "ArticulosTemplates/agregar_articulo.html"
    success_url= reverse_lazy('aplicaciones.articulos:modificar_articulo')


class EliminarArticulos(DeleteView):
    model=Articulo
    template_name= "ArticulosTemplates/eliminar_articulo.html"
    success_url= reverse_lazy('aplicaciones.articulos:eliminar_articulo')

   
class ListarArticulosView(ListView):
    model = Articulo
    template_name = 'ArticulosTemplates/listar_articulos.html'
    context_object_name = "articulos"
    paginate_by = 3












