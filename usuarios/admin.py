from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class UsuarioAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'ci_ruc', 'nombres')

admin.site.register(Usuario, UsuarioAdmin)

class EstudianteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'usuario', 'f_nacimiento')

admin.site.register(Estudiante, EstudianteAdmin)

class PadresAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('padres_estudiante', 'usuario', 'padres_familia', 'is_representante', 'parentesco', 'nivel_educacion', 'profesion')

admin.site.register(Padres, PadresAdmin)

class ParentescoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'parentesco')

admin.site.register(Parentesco, ParentescoAdmin)

class NivelEducativoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nivel_educativo')

admin.site.register(NivelEducativo, NivelEducativoAdmin)


class ProfesionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'profesion')

admin.site.register(Profesion, ProfesionAdmin)
