from django.contrib import admin

from .models import Estudiante, Escuela


@admin.register(Estudiante)
class EstudiantenAdmin(admin.ModelAdmin):
    fields=["nombre","apellido","rut","edad","fecha_nacimiento"]
    list_display=["rut","nombre"]

@admin.register(Escuela)
class EscuelaAdmin(admin.ModelAdmin):
    fields=["nombre","direccion","estudiante"]
    list_display=["nombre"]
