from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Empleado



def index(request):
    template = loader.get_template('empleados/index.html')
    return HttpResponse(template.render())

def write(request, empleado_id):
    #Empleado.objects.get(id=empleado_id)
    return HttpResponse("Escribiremos en el CSV de %s" %empleado_id)



