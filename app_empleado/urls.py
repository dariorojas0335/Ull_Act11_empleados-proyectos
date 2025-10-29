from django.urls import path
from . import views

app_name = 'app_empleado'

urlpatterns = [
    path('', views.listar_empleados, name='listar_empleados'),
    path('empleado/<int:empleado_id>/', views.detalle_empleado, name='detalle_empleado'),
    path('crear/', views.crear_empleado, name='crear_empleado'),
    path('editar/<int:empleado_id>/', views.editar_empleado, name='editar_empleado'),
    path('borrar/<int:empleado_id>/', views.borrar_empleado, name='borrar_empleado'),
]