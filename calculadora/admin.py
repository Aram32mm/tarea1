from django.contrib import admin
from .models import Reto, Jugadores, Usuario, Partida, Estudiante, Juego, Intentos


# Register your models here.
admin.site.register(Reto)
admin.site.register(Jugadores)
admin.site.register(Usuario)
admin.site.register(Partida)
#Reto
admin.site.register(Estudiante)
admin.site.register(Juego)
admin.site.register(Intentos)

