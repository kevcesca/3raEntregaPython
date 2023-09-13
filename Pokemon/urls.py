from django.contrib import admin
from django.urls import path
from Pokemon.views import *

urlpatterns = [
    path("", index, name="Index"),
    path("lista-pokemon", listaPokemon, name="ListaPokemon"),
    path("lista-entrenador", listaEntrenador, name="ListaEntrenador"),
    path("lista-enfrentamiento", listaEnfrentamiento, name="ListaEnfrentamiento"),
    path("formulario-pokemon", formularioPokemon, name="FormularioPokemon"),
    path("formulario-entrenador", formularioEntrenador, name="FormularioEntrenador"),
    path("formulario-enfrentamiento", formularioEnfrentamiento, name="FormularioEnfrentamiento"),
    
]
