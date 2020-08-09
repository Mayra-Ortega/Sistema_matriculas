from django.contrib import admin

from .models import *
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class InstitucionAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre')

admin.site.register(Institucion, InstitucionAdmin)


class CicloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'inicio', 'fin', 'observacion')

admin.site.register(CicloLectivo, CicloAdmin)


class CursoAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre', 'ciclo_lectivo')

admin.site.register(Curso, CursoAdmin)


class ParaleloAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre', 'curso')

admin.site.register(Paralelo, ParaleloAdmin)
