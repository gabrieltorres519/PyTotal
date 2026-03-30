from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea

urlpatterns = [path('', ListaPendientes.as_view(), name='pendientes'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tareas'), # /tarea/número de la tarea en la base de datos (pk--primary key)
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='Eliminar-tarea')] 

