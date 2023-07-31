from django.views.generic import UpdateView, DeleteView, CreateView
from .models import Comentario
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import datetime
from django.shortcuts import render
from .forms import ComentarioForm
from django.utils import timezone

# Create your views here.

def AgregarComentario(request):
    form = ComentarioForm(request.POST or None)
    if form.is_valid():
        form.save()

    contexto = {
        'form': form,
    }
    template_name = 'ComentariosTemplates/agregar_comentario.html'
    return render(request, template_name, contexto)

'''class AgregarComentario(LoginRequiredMixin, CreateView):
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
          articulo_pk= self.kwargs['pk']
          return reverse_lazy('Aplicaciones.Articulos:articulo_detalle', kwargs={'pk': articulo_pk})'''
    
class ModificarComentario(LoginRequiredMixin, UpdateView):
    model=Comentario
    fields=["texto"]
    template_name= "ComentariosTemplates/modificar_comentario.html"
    
    def form_valid(self, form):
        form.instance.fecha_edicion = str(timezone.now())
        return super().form_valid(form)
    
    def get_success_url(self):
          articulo_id= Comentario.objects.get(pk=self.kwargs['pk']).articulo.id
          return reverse_lazy('Aplicaciones.Articulos:articulo_detalle', kwargs={'id': articulo_id})
    
class EliminarComentario(LoginRequiredMixin, DeleteView):
    model=Comentario
    template_name= "ComentariosTemplates/eliminar_comentario.html"
    def get_success_url(self):
          articulo_id= Comentario.objects.get(pk=self.kwargs['pk']).articulo.id
          return reverse_lazy('Aplicaciones.Articulos:articulo_detalle', kwargs={'id': articulo_id})