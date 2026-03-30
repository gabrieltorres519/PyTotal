from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Tarea
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy


class Logueo(LoginView): # Al  igual que todas las clases de Django, LoginView viene con varios campos a llenar como variables
    template_name  = "base/login.html"
    field = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('pendientes')


class ListaPendientes(ListView): # Al heredar de la clase ListView y el modelo llamado Tarea, buscará por defecto templates/tarea_list.html para renderizar (epecificarlo en settings.py del proyecto (DIRS))
    model = Tarea # Modelo/Tabla de la que se tomarán  los registros (trae todos los registros en automático)
    context_object_name = 'tareas' # Cambiamos el nombre para que en los templates los registros no lleguen como object_list por default


class DetalleTarea(DetailView):# tarea_detail.html porque es el nombre que se va a generar automáticamente para las vistas de detalle de la clase DetailView (se puede cambiar esta configuración)
    model = Tarea # Al traer todos los registros en automático, desde el html el objeto '{{object}}' muestra el registro en la bd según se reciba una PK desde la url
                  # El uso de estas cláses del framework Django facilita el crud de esta forma (model = modelo_db)

    context_object_name = 'tarea' # En lugar de {{object}} -> {{tarea}}
    template_name = 'base/tarea.html' # En lugar de buscar tarea_detail.html automáticamente por la clase DetailView


class CrearTarea(CreateView):  # La clase CreateView automáticamente busca el sufijo _form.html
    model = Tarea 
    # La clase CreateView ya toma el modelo o tabla y lo convierte en un objeto formulario
    fields = '__all__'
    success_url = reverse_lazy('pendientes') # Redireccionando al home (name en las urls)


class EditarTarea(UpdateView):
    model = Tarea
    fields = '__all__'
    success_url = reverse_lazy('pendientes')


class EliminarTarea(DeleteView): # La clase de Django busca el archivo _confirm_delete.html
    model = Tarea
    context_object_name = 'Tarea'
    success_url = reverse_lazy('pendientes')