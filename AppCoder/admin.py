from django.contrib import admin
from  .models import * #importamos el archivo models

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
