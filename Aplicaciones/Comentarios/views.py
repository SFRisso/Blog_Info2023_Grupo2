from django.views.generic import *
from .models import *
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime

# Create your views here.

class AgregarComentario(LoginRequiredMixin, CreateView):
    model=Comentario
    #field usuario temporalmente hasta que este el registro/login hecho
    fields=["contenido"]
    template_name= "ComentariosTemplates/agregar_comentario.html"
    success_url= reverse_lazy('Aplicaciones.Articulos:listar_articulos')
    
    def form_valid(self, form):
        form.instance.articulo = Articulo.objects.get(pk=self.kwargs['pk'])
        form.instance.usuario = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          articulo_pk= self.kwargs['pk']
          return reverse_lazy('Aplicaciones.Articulos:articulo_detalle', kwargs={'pk': articulo_pk})
    


class ModificarComentario(LoginRequiredMixin, UpdateView):
    model=Comentario
    #field usuario temporalmente hasta que este el registro/login hecho
    fields=["contenido"]
    template_name= "ComentariosTemplates/agregar_comentario.html"
    
    def form_valid(self, form):
        form.instance.fecha_edicion = str(timezone.now())
        return super().form_valid(form)
    
    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          articulo_pk= Comentario.objects.get(pk=self.kwargs['pk']).articulo.pk
          return reverse_lazy('Aplicaciones.Articulos:articulo_detalle', kwargs={'pk': articulo_pk})
    


class EliminarComentario(LoginRequiredMixin, DeleteView):
    model=Comentario
    template_name= "ComentariosTemplates/eliminar_comentario.html"
    def get_success_url(self):
          # if you are passing 'pk' from 'urls' to 'DeleteView' for company
          # capture that 'pk' as companyid and pass it to 'reverse_lazy()' function
          articulo_pk= Comentario.objects.get(pk=self.kwargs['pk']).articulo.pk
          return reverse_lazy('Aplicaciones.Articulos:articulo_detalle', kwargs={'pk': articulo_pk})