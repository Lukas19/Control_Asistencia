from django.contrib import admin
# Register your models here.

from .models import Empleado,Documento

admin.site.register(Empleado)
admin.site.register(Documento) #Despliega el CRUD de Documento

