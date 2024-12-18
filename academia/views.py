from django.shortcuts import render
from .models import Estudiante 


#def estudiante(request):
    #contexto = {'nombre': 'Juan', 'edad':18}
    #return render(request, 'index.html',contexto)

def estudiante(request,idEstudiante):
    # Obtener el estudiante por su ID
    estudiante = Estudiante.objects.get(id=idEstudiante)
    print(estudiante)
    contexto = {'stu': estudiante}
    # Pasar el contexto a la plantilla
    return render(request, 'index.html',contexto)

def listarestudiante(request):
    todos_estudiantes = Estudiante.objects.all()
    contexto = {'todos': todos_estudiantes}
    return render(request, 'lista_estudiante.html',contexto)








