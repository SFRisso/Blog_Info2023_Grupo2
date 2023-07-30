from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from Aplicaciones.Comentarios.models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import *
from django.db.models import Q

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
    
    def get_queryset(self):
        queryset = Articulo.objects.all().order_by('-fecha_publicacion')
        order_by = self.request.GET.get('order_by', '')

        if order_by:
            if order_by.upper() == "ASC": 
                # Ascendente
                queryset = Articulo.objects.all().order_by('fecha_publicacion')
            else:
                # Descendente
                pass
        
        order_by_titulo = self.request.GET.get('order_by_titulo', '')
        if order_by_titulo:
            if order_by_titulo.upper() == "ASC": 
                queryset = Articulo.objects.all().order_by('titulo')
            else:
                queryset = Articulo.objects.all().order_by('-titulo')
        
        qset = []
        
        categoria = self.request.GET.get('categoria', '')
        
        if categoria:
            qset.append(Q(categoria__id=categoria))
    
        queryset = queryset.filter(*qset)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categoria.objects.all()
        return context
    

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






   







