from django.shortcuts import render, get_object_or_404, redirect
from .models import Empleado
from .forms import EmpleadoForm

def listar_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleados.html', {'empleados': empleados})

def detalle_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    return render(request, 'detalle_empleado.html', {'empleado': empleado})

def crear_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('app_empleado:listar_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'formulario_empleado.html', {'form': form, 'titulo': 'Crear Empleado'})

def editar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        form = EmpleadoForm(request.POST, request.FILES, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('app_empleado:detalle_empleado', empleado_id=empleado.id)
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'formulario_empleado.html', {'form': form, 'titulo': 'Editar Empleado'})

def borrar_empleado(request, empleado_id):
    empleado = get_object_or_404(Empleado, id=empleado_id)
    if request.method == 'POST':
        empleado.delete()
        return redirect('app_empleado:listar_empleados')
    return render(request, 'confirmar_borrar.html', {'empleado': empleado})