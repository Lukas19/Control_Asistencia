import csv
import datetime
import time

from django.shortcuts import redirect,render
# Create your views here.
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader
from django.contrib import messages
from django.views.decorators.csrf import csrf_protect

from .models import Empleado




def index(request):
    return render(request, 'empleados/index.html')

#@csrf_exempt
@csrf_protect
def lector(request):
    today = str(datetime.datetime.now().strftime("%d-%H:%M"))
    month = str(datetime.datetime.now().strftime("%m-%Y"))
    if request.method == 'GET':
        return render(request, 'empleados/lector.html')
    elif request.method == 'POST':
        empleado_nombre = request.POST.get('qr-value')
        nombre = empleado_nombre.split("_")
        nombre = str.join(" ",nombre)
        personal = Empleado.objects.get(nombre=nombre)
        archivo = open("media/"+empleado_nombre+"_"+month+".csv")
        numline = len(archivo.readlines())
        archivo.close()
        if nombre == personal.__str__(): #ADAPTAR A LA QUERY!
            with open("media/"+empleado_nombre+"_"+month+".csv", 'a', newline='') as fp:
                a = csv.writer(fp, delimiter=',')
                if (numline%5 != 0):
                    data = [[empleado_nombre, today]
                        ]
                    a.writerows(data)
                    #time.sleep(5)
                    return JsonResponse({'error': False, 'message': u'Actualizado con éxito.'})
                else:
                    data = [["---------"]
                            ]
                    a.writerows(data)
                    data = [[empleado_nombre, today]
                            ]
                    a.writerows(data)

                    #time.sleep(5)
                    return JsonResponse({'error': False, 'message': u'Actualizado con éxito.'})


