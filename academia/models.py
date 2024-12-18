from django.db import models

# Definir el modelo Estudiante


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=150)
    rut = models.CharField(max_length=8)
    edad = models.IntegerField()
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre

# Definir el modelo Escuela
class Escuela(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=255)
    estudiante = models.ForeignKey(
        Estudiante, on_delete=models.CASCADE, related_name='escuelas')

    def __str__(self):
        return self.nombre
