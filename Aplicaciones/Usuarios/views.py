from django.views.generic import CreateView
from .models import Usuario
from django.urls import reverse_lazy
from .forms import RegistrarUsuarioForm

# Create your views here.

class RegistarUsuario(CreateView):
    model=Usuario
    #field usuario temporalmente hasta que este el registro/login hecho
    template_name= "UsuariosTemplates/registrar_usuario.html"
    form_class = RegistrarUsuarioForm
    success_url= reverse_lazy('Aplicaciones.Articulos:listar_articulos')