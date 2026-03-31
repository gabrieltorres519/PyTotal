from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarea
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin # Atributos de usuario y restricción del acceso a listas del sitio
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import redirect


class Logueo(LoginView): # Al  igual que todas las clases de Django, LoginView viene con varios campos a llenar como variables
    template_name  = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pendientes')


class PaginaRegistro(FormView):
    template_name = 'base/registro.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('pendientes')

    def form_valid(self, form):
        usuario = form.save()
        if usuario is not None:
            login(self.request, usuario)
        return super(PaginaRegistro, self).form_valid(form)
    
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('pendientes')
        return super(PaginaRegistro, self).get(*args, **kwargs)     

# Todas las clases creadas para las diferentes vistas heredarán primero a LoginRequiredMixin para restringir su acceso

class ListaPendientes(LoginRequiredMixin, ListView): # Al heredar de la clase ListView y el modelo llamado Tarea, buscará por defecto templates/tarea_list.html para renderizar (epecificarlo en settings.py del proyecto (DIRS))
    model = Tarea # Modelo/Tabla de la que se tomarán  los registros (trae todos los registros en automático)
    context_object_name = 'tareas' # Cambiamos el nombre para que en los templates los registros no lleguen como object_list por default

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tareas'] = context['tareas'].filter(usuario=self.request.user) # 1er paso: Listado de tareas asociado al usuario logueado
        context['count'] = context['tareas'].filter(completo=False).count() # 2do paso: Conteo de tareas no completadas
        return context

class DetalleTarea(LoginRequiredMixin,DetailView):# tarea_detail.html porque es el nombre que se va a generar automáticamente para las vistas de detalle de la clase DetailView (se puede cambiar esta configuración)
    model = Tarea # Al traer todos los registros en automático, desde el html el objeto '{{object}}' muestra el registro en la bd según se reciba una PK desde la url
                  # El uso de estas cláses del framework Django facilita el crud de esta forma (model = modelo_db)

    context_object_name = 'tarea' # En lugar de {{object}} -> {{tarea}}
    template_name = 'base/tarea.html' # En lugar de buscar tarea_detail.html automáticamente por la clase DetailView


class CrearTarea(LoginRequiredMixin,CreateView):  # La clase CreateView automáticamente busca el sufijo _form.html
    model = Tarea 
    # La clase CreateView ya toma el modelo o tabla y lo convierte en un objeto formulario
    fields = ['titulo','descripcion','completo']
    success_url = reverse_lazy('pendientes') # Redireccionando al home (name en las urls)

    def form_valid(self, form): # Sobreescritura del método de la clase CreateView (formulario)
        form.instance.usuario = self.request.user # Llenar el campo de usuario con el usuario logueado por default
        return super(CrearTarea, self).form_valid(form) # Devolver los cambios     
    


class EditarTarea(LoginRequiredMixin,UpdateView):
    model = Tarea
    fields = ['titulo','descripcion','completo'] # Evitando que el campo de usuario sea editable
    success_url = reverse_lazy('pendientes')


class EliminarTarea(LoginRequiredMixin,DeleteView): # La clase de Django busca el archivo _confirm_delete.html
    model = Tarea
    context_object_name = 'Tarea'
    success_url = reverse_lazy('pendientes')