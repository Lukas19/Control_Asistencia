from django.contrib import admin
# Register your models here.
from .models import *

class DocumentoAdmin(admin.ModelAdmin):
    list_display = ['dueño','fecha']
    list_filter = ['dueño','fecha']

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'cargo']
    list_filter = ['cargo']

admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Empleado, EmpleadoAdmin)
