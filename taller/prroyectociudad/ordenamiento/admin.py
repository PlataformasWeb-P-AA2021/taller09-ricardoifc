from django.contrib import admin
from ordenamiento.models import Parroquia, Barrio
from import_export.admin import ImportExportModelAdmin

# Se crea una clase que hereda
# de ModelAdmin para el modelo
# Parroquia

class ParroquiaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('id', 'nombre', 'tipo')

admin.site.register(Parroquia, ParroquiaAdmin)

class BarrioAdmin(admin.ModelAdmin):

    list_display = ('id', 'nombre', 'numViviendas', 'numParques', 'numEdificios', 'parroquia')

admin.site.register(Barrio, BarrioAdmin)