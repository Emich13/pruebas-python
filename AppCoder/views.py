from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso
from AppCoder.forms import CursoFormulario

def inicio(request):
	return render(request,'AppCoder/inicio.html')

def profesores(request):
	return render(request,'AppCoder/profesores.html')

def cursos(request):
	if request.method == 'POST':

		miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html
		print(miFormulario)

		if miFormulario.is_valid:   #Si pasó la validación de Django
			informacion = miFormulario.cleaned_data
			curso = Curso (nombre=informacion['curso'], 
			camada=informacion['camada']) 
			curso.save()
			return render(request, 'AppCoder/inicio.html') #Vuelvo al inicio o a donde quieran

	else:
		miFormulario= CursoFormulario() #Formulario vacio para construir el html

	return render(request, 'AppCoder/cursos.html', {'miFormulario':miFormulario})


def buscar(request):
	if  request.GET["camada"]:
		camada = request.GET.get['camada'] 
		cursos = Curso.objects.filter(camada__icontains=camada)
		return render(request, "AppCoder/buscando.html", {"cursos":cursos, "camada":camada})
	else: 
		respuesta = "No enviaste datos"

	#No olvidar from django.http import HttpResponse
	return HttpResponse(respuesta)

# def busquedaCamada(request):
# 	return render(request,'AppCoder/busquedaCamada.html')

# def buscar2 (request):
# 	respuesta = f"Estoy buscando la camada N° {request.GET['camada']}"
# 	return HttpResponse(respuesta)