from django.conf.urls import url

from . import views
from Asistencia_Personal import settings

urlpatterns = [
    url(r'^$',views.index, name='index'),
    url(r'^lector', views.lector, name='lector'),
]
