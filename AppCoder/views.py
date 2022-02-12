from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Estudiante, Profesor
from AppCoder.forms import CursoFormulario, EstudiantesFormulario, ProfesoresFormulario
	


def inicio(request):
	return render(request,'AppCoder/inicio.html')

def profesores(request):
	if request.method == 'POST':
		miFormulario = ProfesoresFormulario(request.POST) #aquí mellega toda la información del html
		print(miFormulario)

		if miFormulario.is_valid:   #Si pasó la validación de Django
			informacion = miFormulario.cleaned_data
			profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
			email=informacion['email'], profesion=informacion['profesion'])
			profesor.save()
			return render(request, 'AppCoder/inicio.html') #Vuelvo al inicio o a donde quieran

	else:
		miFormulario= ProfesoresFormulario() #Formulario vacio para construir el html

	return render(request, 'AppCoder/profesores.html', {'miFormulario':miFormulario})	

def estudiantes(request):
	if request.method == 'POST':
		miFormulario = EstudiantesFormulario(request.POST) #aquí mellega toda la información del html
		print(miFormulario)

		if miFormulario.is_valid:   #Si pasó la validación de Django
			informacion = miFormulario.cleaned_data
			estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],email=informacion['email'])
			estudiante.save()
			return render(request, 'AppCoder/inicio.html') #Vuelvo al inicio o a donde quieran

	else:
		miFormulario= EstudiantesFormulario() #Formulario vacio para construir el html

	return render(request, 'AppCoder/estudiantes.html', {'miFormulario':miFormulario})	

def cursos(request):
	if request.method == 'POST':
		miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html
		print(miFormulario)

		if miFormulario.is_valid:   #Si pasó la validación de Django
			informacion = miFormulario.cleaned_data
			curso = Curso (nombre=informacion['curso'], camada=informacion['camada']) 
			curso.save()
			return render(request, 'AppCoder/inicio.html') #Vuelvo al inicio o a donde quieran

	else:
		miFormulario= CursoFormulario() #Formulario vacio para construir el html

	return render(request, 'AppCoder/cursos.html', {'miFormulario':miFormulario})

def buscar(request):
	if  request.GET["camada"]:
		camada = request.GET['camada'] 
		cursos = Curso.objects.filter(camada__icontains=camada)
		return render(request, "AppCoder/buscando.html", {"cursos":cursos, "camada":camada})
	else: 
		respuesta = "No enviaste datos"

	return HttpResponse(respuesta)


def infoBuscar(request):
	return render(request,'AppCoder/infoBuscar.html')