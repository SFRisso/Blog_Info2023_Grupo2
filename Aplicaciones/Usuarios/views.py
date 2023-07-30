from django.shortcuts import render
from .models import articulo
from django.db.models import Q

# Create your views here.

def index(request):
    queryset = request.GET.get("buscar")
    articulos = articulo.objects.filter(estado = True)
    if queryset:
        articulos = articulo.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(contenido__icontains = queryset) |
            Q(localidad__icontains = queryset) |
            Q(modalidad__icontains = queryset)
        ).distinct()
    return render(request,'index/index.html',{'articulos':articulos})