from django import forms
from .models import Pokemon, Entrenador, Enfrentamiento


class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ['nombre', 'tipo', 'numPokedex', 'imageUrl']

class EntrenadorForm(forms.ModelForm):
    class Meta:
        model = Entrenador
        fields = ['nombre', 'pokemon1', 'pokemon2', 'pokemon3', 'pokemon4', 'pokemon5', 'pokemon6']

class EnfrentamientoForm(forms.ModelForm):
    class Meta:
        model = Enfrentamiento
        fields = ['ganador', 'entrenador1', 'entrenador2', 'fecha_combate', 'finalizado']
