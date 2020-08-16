from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.db.models.signals import post_save
from django.dispatch import receiver
from institucion.models import Institucion, CicloLectivo



class Usuario(models.Model):
	ci_ruc = models.CharField(max_length= 13, help_text='Cedula o RUC')
	nombres = models.CharField(max_length=200)
	apellidos = models.CharField(max_length=200)
	direccion = models.CharField(max_length= 200, null=True, blank=True)
	telefono = models.CharField(max_length=20, null=True, blank=True)
	celular = models.CharField(max_length=20, null=True, blank=True)

	class Meta:
		verbose_name = "Usuario"
		verbose_name_plural = "Usuarios"

	def __str__(self):
		return "%s %s" %(self.nombres, self.apellidos)

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usuario')
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='usuario_estudiante')
    f_nacimiento = models.DateField(help_text='Fecha de nacimiento')
    lugar_nacimiento = models.CharField(max_length= 13, help_text='Sector/Canton/Provincia')
    institucion = models.ForeignKey(Institucion, blank=True, null=True, on_delete=models.CASCADE)
    img_perfil = models.ImageField(upload_to='static/images/users', help_text='Escoja una Imagen de perfil')

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self):
        return self.usuario.nombres


class UsuarioCicloLectivo(models.Model):
	estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, null=True)
	ciclo_lectivo = models.ForeignKey(CicloLectivo, on_delete=models.CASCADE, null=True)

	class Meta:
		verbose_name = "UsuarioCicloLectivo"
		verbose_name_plural = "UsuariosCicloLectivo"

	def __str__(self):
		return self.estudiante.nombre


class Parentesco(models.Model):
    parentesco =  models.CharField(max_length =100)
    class Meta:
    	verbose_name = "Parentesco"
    	verbose_name_plural = "Parentescos"

    def __str__(self):
    	return self.parentesco

class NivelEducativo(models.Model):
    nivel_educativo =  models.CharField(max_length =100)
    class Meta:
    	verbose_name = "NivelEducativo"
    	verbose_name_plural = "NivelesEducativos"

    def __str__(self):
    	return self.nivel_educativo

class Profesion(models.Model):
    profesion =  models.CharField(max_length =100)
    class Meta:
    	verbose_name = "Profesion"
    	verbose_name_plural = "Profesiones"

    def __str__(self):
    	return self.profesion



class Padres(models.Model):
    PADRES_FAMILIA = [
    ('M', 'Mamá'),
    ('P', 'Papá'),
    ]
    padres_estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE, related_name= 'padres_estudiante')
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='datos_padre')
    padres_familia = models.CharField(max_length = 50, choices = PADRES_FAMILIA, default='P')
    is_representante = models.BooleanField(default=False, help_text='Es representante del estudiante')
    parentesco = models.ForeignKey(Parentesco, on_delete=models.CASCADE)
    nivel_educacion = models.ForeignKey(NivelEducativo, on_delete=models.CASCADE)
    profesion = models.ForeignKey(Profesion, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Padres"
        verbose_name_plural = "Padres"

        def __str__(self):
            return self.usuario.ci_ruc

class Representante(models.Model):
	representante = models.ForeignKey(Padres, on_delete=models.CASCADE, related_name = 'representante_padres')
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='user')

	class Meta:
		verbose_name = "Representante"
		verbose_name_plural = "Representantes"

	def __str__(self):
	    return self.user.username
