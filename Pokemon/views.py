from django.shortcuts import render
from .forms import *
# Create your views here.
def index(req):
    
    return render(req, "index.html")

def listaPokemon(req):
    listaPokemon = []

    if "nombrePokemon" in req.GET:
        # Si se proporciona un parámetro "nombrePokemon" en la URL, realizamos la búsqueda
        pokemonBuscado = req.GET["nombrePokemon"]
        listaPokemon = Pokemon.objects.filter(nombre__icontains=pokemonBuscado)
    else:
        # Si no se proporciona un parámetro "nombrePokemon", mostramos la lista completa de Pokémon
        listaPokemon = Pokemon.objects.all()
    
    if not listaPokemon:
        return render(req, "listaPokemon.html", {"listaPokemon": listaPokemon, "mensaje":"Ningun pokemon coincide"})
    
    return render(req, "listaPokemon.html", {"listaPokemon": listaPokemon})

def formularioPokemon(req):
    if req.method == 'POST':
        formPoke = PokemonForm(req.POST)
        if formPoke.is_valid():
            formPoke.save()
            formPoke = PokemonForm()
            return render(req, "formularioPokemon.html", {'mensaje': "Pokemon creado exitosamente", 'formPoke': formPoke})
    else:
        formPoke = PokemonForm()
        return render(req, "formularioPokemon.html", {'formPoke': formPoke})


def listaEntrenador(req):
    listaEntrenador = Entrenador.objects.all()
    return render(req, "listaEntrenador.html", {"listaEntrenador" : listaEntrenador})

def formularioEntrenador(req): 
    if req.method == 'POST':
        formEntr = EntrenadorForm(req.POST)
        if formEntr.is_valid():
            # guardamos los datos ingresados dentro del formulario
            formEntr.save()
            
            # vaciamos el formulario
            formEntr = EntrenadorForm()
            return render(req, "formularioEntrenador.html", {'mensaje': "Entrenador creado exitosamente", 'formEntr': formEntr})
        
    else:
        formEntr = EntrenadorForm()
        return render(req, "formularioEntrenador.html", {'formEntr': formEntr})

def listaEnfrentamiento(req):
    listaEnfrentamiento = Enfrentamiento.objects.all()
    return render(req, "listaEnfrentamiento.html", {"listaEnfrentamiento" : listaEnfrentamiento})

def formularioEnfrentamiento(req):
    if req.method == 'POST':
        # Llenamos el formulario y hacemos una request post
        formEnfr = EnfrentamientoForm(req.POST)
        if formEnfr.is_valid():
            formEnfr.save()
            formEnfr = EnfrentamientoForm()
            return render(req, "formularioEnfrentamiento.html", {'mensaje': "Enfrentamiento creado exitosamente", 'formEnfr': formEnfr})
    else:
        # Cargamos el formulario vacio cuando recien cargamos la pagina
        formEnfr = EnfrentamientoForm()
        return render(req, "formularioEnfrentamiento.html", {'formEnfr' : formEnfr})