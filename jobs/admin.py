from django.contrib import admin

# Register your models here.
from .models import Jugador, Cancha, Juego
admin.site.register(Jugador)
admin.site.register(Cancha)
admin.site.register(Juego)
