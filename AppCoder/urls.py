from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.cursos, name='cursos'),
    #path('cursoFormulario/', views.cursoFormulario, name='cursoFormulario'),
    # path('busquedaCamada/', views.busquedaCamada, name='BusquedaCamada'),
    # path('buscar2/', views.buscar2),
    path('buscando/', views.buscar, name='buscando'),
]