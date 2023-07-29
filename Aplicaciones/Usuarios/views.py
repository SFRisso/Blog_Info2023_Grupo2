from django.views.generic import ListView
from .models import *
from django.db.models import Q


class ListaArticulos(ListView):
    model = articulo
    template_name = "articulos/lista.html"
    context_object_name = "articulos"


    def get_queryset(self):
        queryset = articulo.objects.all().order_by('-fecha_publicacion')
        order_by = self.request.GET.get('order_by', '')

        if order_by:
            if order_by.upper() == "ASC": 
                # Ascendente
                queryset = articulo.objects.all().order_by('fecha_publicacion')
            else:
                # Descendente
                pass
        qset = []
        
        categoria = self.request.GET.get('categoria', '')
        
        if categoria:
            qset.append(Q(id_categoria__id=categoria))
    
        queryset = queryset.filter(*qset)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = categoria.objects.all()
        return context
    
   

