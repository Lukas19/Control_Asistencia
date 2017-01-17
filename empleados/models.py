from django.db import models
from django.dispatch import receiver
import os

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=200)
    rut = models.IntegerField()
    cargo = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

class Documento(models.Model):
    nombre = models.CharField(max_length=200)
    dueño = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    archivo = models.FileField()
    fecha = models.DateField()

    def __str__(self):
        return self.nombre

    def archivo_link(self):
        if self.archivo:
            return "<a href='%s'>download</a>" % (self.archivo.url,)
        else:
            return "No attachment"
    archivo_link.allow_tags = True
    archivo_link.short_description = "File Link"

@receiver(models.signals.post_delete, sender=Documento)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Deletes file from filesystem
    when corresponding `Documento` object is deleted.
    """
    if instance.archivo:
        if os.path.isfile(instance.archivo.path):
            os.remove(instance.archivo.path)


