from django.contrib import admin
from .models import Enfrentamiento, Entrenador, Pokemon

# Register your models here.
admin.site.register(Enfrentamiento)
admin.site.register(Pokemon)
admin.site.register(Entrenador)