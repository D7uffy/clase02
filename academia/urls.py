# URLS DEL APP ACADEMIA

from django.urls import path
from . import views

urlpatterns = [
    path('estudiante/<int:idEstudiante>',views.estudiante, name="detalleEstudiante"),
    path('listarestudiante/',views.listarestudiante, name="listarestudiante"),
]