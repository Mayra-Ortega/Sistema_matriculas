from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Institucion(models.Model):
	nombre = models.CharField(max_length=50, help_text='Nombre de su empresa.')
	slogan = models.TextField(blank=True, null=True, help_text='Frase Slogan de su negocio.')
	rector = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
	descripcion = models.TextField(blank=True, null=True, help_text='Describa el campo ocupacional y área de su empresa.')
	direccion = models.CharField(max_length=150, null=True)
	telefono = models.CharField(max_length=20, null=True)
	sitio_web = models.URLField(blank=True, null=True, help_text='Página web de su empresa.')

	class Meta:
		verbose_name = "Institucion"
		verbose_name_plural = "Instituciones"

	def __str__(self):
		return self.nombre


class CicloLectivo(models.Model):
	inicio = models.DateField(help_text='Inicio del año lectivo')
	fin = models.DateField(help_text='Fin del año lectivo')
	observacion= models.CharField(max_length=300, help_text='Observación sobre el año lectivo')
	ciclo_actual = models.BooleanField(default=True, help_text='Es el año lectivo actual con el que trabajará')


	class Meta:
		verbose_name = "Ciclo"
		verbose_name_plural = "Ciclos"

	def __str__(self):
		return self.observacion

class InstitucionCicloLectivo(models.Model):
	institucion = models.ForeignKey(Institucion, on_delete=models.CASCADE, null=True)
	ciclo_lectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = "InstitucionCicloLectivo"
		verbose_name_plural = "InstitucionesCiclosLectivos"

	def __str__(self):
		return self.institucion.nombre


class Curso(models.Model):
	nombre= models.CharField(max_length=300)
	ciclo_lectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = "Curso"
		verbose_name_plural = "Cursos"

	def __str__(self):
		return self.nombre


class Paralelo(models.Model):
	nombre= models.CharField(max_length=50)
	curso = models.ForeignKey(Curso, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = "Paralelo"
		verbose_name_plural = "Paralelos"

	def __str__(self):
		return self.nombre


class PreguntaFrecuente(models.Model):
	pregunta = models.CharField(max_length=500)
	respuesta = models.CharField(max_length=500)
	class Meta:
		verbose_name = "PreguntaFrecuente"
		verbose_name_plural = "PreguntasFrecuentes"

	def __str__(self):
		return self.pregunta
