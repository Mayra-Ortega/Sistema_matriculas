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
