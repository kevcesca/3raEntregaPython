from django.db import models


# Create your models here.
class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    numPokedex = models.IntegerField()
    imageUrl = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class Entrenador(models.Model):
    nombre = models.CharField(max_length=50)
    pokemon1 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entrenador_pokemon1')
    pokemon2 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entrenador_pokemon2')
    pokemon3 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entrenador_pokemon3')
    pokemon4 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entrenador_pokemon4')
    pokemon5 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entrenador_pokemon5')
    pokemon6 = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='entrenador_pokemon6')
    
    def __str__(self):
        return self.nombre

class Enfrentamiento(models.Model):
    ganador = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='enfrentamientos_ganados')
    entrenador1 = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='enfrentamientos_entrenador1')
    entrenador2 = models.ForeignKey(Entrenador, on_delete=models.CASCADE, related_name='enfrentamientos_entrenador2')
    fecha_combate = models.DateField()
    finalizado = models.BooleanField()
    
    def __str__(self):
        return f"Enfrentamiento entre {self.entrenador1} y {self.entrenador2}"