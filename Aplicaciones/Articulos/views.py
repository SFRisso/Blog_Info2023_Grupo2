from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from Aplicaciones.Comentarios.models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import *

# Create your views here.

class AgregarArticulo(CreateView):
    model=Articulo
    #field usuario temporalmente hasta que este el registro/login hecho
    fields=["usuario","titulo","contenido","localidad","imagen_portada","modalidad","categoria"]
    template_name= "ArticulosTemplates/agregar_articulo.html"
    success_url= reverse_lazy('Aplicaciones.Articulos:listar_articulos')


class ModificarArticulo(UpdateView):
    model=Articulo
    #field usuario temporalmente hasta que este el registro/login hecho
    fields=["titulo","contenido","localidad","imagen_portada","modalidad","categoria"]
    template_name= "ArticulosTemplates/agregar_articulo.html"
    success_url= reverse_lazy('Aplicaciones.Articulos:listar_articulos')


class EliminarArticulo(DeleteView):
    model=Articulo
    template_name= "ArticulosTemplates/eliminar_articulo.html"
    success_url= reverse_lazy('Aplicaciones.Articulos:listar_articulos')

   
class ListarArticulosView(ListView):
    model = Articulo
    template_name = 'ArticulosTemplates/listar_articulos.html'
    context_object_name = "articulos"
    paginate_by = 5
    ordering = ['-fecha_publicacion']

class ArticuloDetalle(DetailView):
    model = Articulo
    template_name =  'ArticulosTemplates/articulo.html'
    context_object_name = 'articulo'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        comentarios = Comentario.objects.all().filter(articulo=self.kwargs['pk']).order_by('-fecha_publicacion')
        page = self.request.GET.get('page')
        context['comentarios'] = Paginator(comentarios, 2).get_page(page)
        return context













