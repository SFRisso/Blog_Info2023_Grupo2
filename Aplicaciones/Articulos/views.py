from django.forms.models import BaseModelForm
"from django.http import HttpResponse"
from django.shortcuts import render
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin





# Create your views here.

class AgregarArticulo(CreateView,LoginRequiredMixin):
    model=Articulos
    fields=["titulo","contenido","localidad","portada","modalidad"]
    template_name= "ArticulosTemplate/agregar_articulo.html"
    success_url= reverse_lazy('inicio')



class ModificarArticulos(UpdateView,LoginRequiredMixin):
    model=Articulos
    fields=["titulo","contenido","localidad","portada","modalidad"]
    template_name= "ArticulosTemplate/agregar_articulo.html"
    success_url= reverse_lazy('aplicaciones.articulos:modificar_articulo')


class EliminarArticulos(DeleteView, LoginRequiredMixin):
    model=Articulos
    template_name= "ArticulosTemplate/eliminar_articulo.html"
    success_url= reverse_lazy('aplicaciones.articulos:eliminar_articulo')





