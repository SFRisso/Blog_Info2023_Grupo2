from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from Aplicaciones.Comentarios.models import Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.shortcuts import *
from django.db.models import Q

# Create your views here.

class AgregarArticulo(LoginRequiredMixin, CreateView):
    model=Articulo
    fields=["titulo","contenido","localidad","imagen_portada","modalidad","categoria"]
    template_name= "ArticulosTemplates/agregar_articulo.html"
    success_url= reverse_lazy('Aplicaciones.Articulos:listar_articulos')
    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ModificarArticulo(LoginRequiredMixin, UpdateView):
    model=Articulo
    fields=["titulo","contenido","localidad","imagen_portada","modalidad","categoria"]
    template_name= "ArticulosTemplates/agregar_articulo.html"
    success_url= reverse_lazy('Aplicaciones.Articulos:listar_articulos')


class EliminarArticulo(LoginRequiredMixin, DeleteView):
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
       
       #ordenar por fecha de publicación 
        order_by = self.request.GET.get('order_by', '')
        if order_by:
            if order_by.upper() == "ASC": 
                queryset = Articulo.objects.all().order_by('fecha_publicacion')
            else:
                pass
        
        #ordernar alfabeticamente
        order_by_titulo = self.request.GET.get('order_by_titulo', '')
        if order_by_titulo:
            if order_by_titulo.upper() == "ASC": 
                queryset = Articulo.objects.all().order_by('titulo')
            else:
                queryset = Articulo.objects.all().order_by('-titulo')
         
        #barra de busqueda       
        buscar = self.request.GET.get('buscar')
        if buscar:
            queryset = Articulo.objects.filter(
                Q(titulo__icontains = buscar) |
                Q(contenido__icontains = buscar) |
                Q(localidad__icontains = buscar) |
                Q(modalidad__icontains = buscar)
            ).distinct()
        
        #filtrar por categorias
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






   







