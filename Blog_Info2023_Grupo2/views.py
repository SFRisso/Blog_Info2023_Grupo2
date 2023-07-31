from django.shortcuts import render


def AcercaDe(request):
    template_name = 'acerca_de.html'
    return render(request,template_name)

def Contacto(request):
    template_name = 'contacto.html'
    return render(request,template_name)