from django.db import models
from usuarios.models import *
from institucion.models import *

# Create your models here.
class Matricula(models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    ciclo_lectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    paralelo = models.ForeignKey(Paralelo, on_delete=models.CASCADE, null=True)
    observacion = models.TextField(blank=True, null=True, help_text='Observación sobre la matrícula')
    fecha = models.DateField(auto_now_add=True)
    matricula_aceptada = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Matricula"
        verbose_name_plural = "Matriculas"

    def __str__(self):
        return self.estudiante.usuario.nombres

class SolicitudIngreso(models.Model):
    TIPO_MATRICULA = [
    ('1', 'ORDINARIA'),
    ('2', 'EXTRAORDINARIA'),
    ]
    VIENE_OTRA_INSTITUCION = [
    ('1', 'SI'),
    ('2', 'NO'),
    ('3', 'PASE'),
    ]
    fecha = models.DateField(auto_now_add=True)
    representante = models.ForeignKey(Representante, on_delete=models.CASCADE, null=True)
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
    ciclo_lectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE, null=True)
    paralelo = models.ForeignKey(Paralelo, on_delete=models.CASCADE, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)
    tipo_matricula = models.CharField(max_length = 50, choices = TIPO_MATRICULA, default='2')
    viene_otra_institucion = models.CharField(max_length = 50, choices = VIENE_OTRA_INSTITUCION, default='1')
    f_aceptacion = models.DateField(blank=True, null=True)
    aprobacion = models.BooleanField(default=False)
    rector = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rector')

    class Meta:
        verbose_name = "SolicitudIngreso"
        verbose_name_plural = "SolicitudesIngresos"

    def __str__(self):
        return self.estudiante.usuario.nombres
