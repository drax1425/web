from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index" ),
    path('contacto', contacto, name="contacto" ),
    path('singlenews', singlenews, name="singlenews" ),
    #login
    path('inicio', inicio, name="inicio" ),
    path('registrarse', registrarse, name="registrarse" ),
    #Planes
    path('planes', planes, name="planes" ),
    #Categorias
    path('categorias', categorias, name="Categorias" ),
    path('tecnologia', tecnologia, name="tecnologia" ),
    path('politica', politica, name="politica" ),
    path('internacional', internacional, name="internacional" ),
    path('entretenimiento', entretenimiento, name="entretenimiento" ),
    path('deporte', deporte, name="deporte" ),
    #Error 404
    path('error404', error404, name="error404" ),

    #inicio crud
    path('empleados', empleados, name="empleados"),
    path('empleados/add', empleadosadd, name="empleadosadd"),
    path('empleados/update/<str:rut>', empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<str:rut>', empleadosdelete, name="empleadosdelete"),
    #fin crud
    path('logout/', logout_view, name='logout'),
]
