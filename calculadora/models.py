from django.db import models

# Create your models here.
class Reto(models.Model):
    nombre = models.CharField(max_length=30)
    minutos_jugados = models.IntegerField()

class Jugadores(models.Model):
    grupo = models.CharField(max_length=2)
    num_lista = models.IntegerField()

class Usuario(models.Model):
    id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=50)

    def __str__(self):
        return str(self.id)

class Partida(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateField(auto_now_add=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    minutos_jugados = models.IntegerField()
    puntaje = models.IntegerField()

    def __str__(self):
        return str(self.id)
