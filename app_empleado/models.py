from django.db import models


class Empleado(models.Model):
    nombres_emp = models.CharField(max_length=100)
    ap_p_emp = models.CharField(max_length=100)
    ap_m_emp = models.CharField(max_length=100, blank=True)
    direccion_emp = models.CharField(max_length=200, blank=True)
    correo_emp = models.EmailField(max_length=100, blank=True)
    puesto_emp = models.CharField(max_length=100, blank=True)
    proyectos_emp = models.IntegerField(default=0)
    foto_empleado = models.ImageField(upload_to='img_empleados/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombres_emp} {self.ap_p_emp}"

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"


class Proyecto(models.Model):
    nombre_pr = models.CharField(max_length=100)
    direccion_pr = models.CharField(max_length=200, blank=True)
    fecha_ini = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)
    estado_pr = models.CharField(max_length=50, blank=True)
    presupuesto_pr = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE, related_name='proyectos', blank=True, null=True)

    def __str__(self):
        return self.nombre_pr

    class Meta:
        verbose_name = "Proyecto"
        verbose_name_plural = "Proyectos"