from django.urls import path
from AppCoder import views

urlpatterns = [
    path('inicio/', views.inicio, name='inicio'),
    path('profesores/', views.profesores, name='profesores'),
    path('cursos/', views.cursos, name='cursos'),
    path('estudiantes/', views.estudiantes, name='estudiantes'),
    path('buscando/', views.buscar, name='buscando'),
    path('infoBuscar/', views.infoBuscar, name='infoBuscar'),
]