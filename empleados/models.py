from django.db import models
# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.IntegerField()
    cargo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    dueño = models.ForeignKey(Empleado)
    fecha = models.DateTimeField()
