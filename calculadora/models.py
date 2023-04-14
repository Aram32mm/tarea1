from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

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


#Reto 
class Estudiante(models.Model):
    estudianteID = models.AutoField(primary_key=True)
    numeroLista = models.IntegerField() # Definición de campo único
    grupo = models.CharField(max_length=2) # Definición de campo único
    avanceJuegoID = models.ForeignKey('Juego', on_delete=models.CASCADE)

    def __str__(self):
        return f'Número de Lista {self.numeroLista} - Grupo {self.grupo}'

    class Meta:
        unique_together = ('numeroLista', 'grupo')
    
    # Función manejadora de la señal para actualizar el campo de progreso
    @receiver(post_save, sender='calculadora.Intentos') # Reemplaza 'mi_app' con el nombre de tu aplicación
    def actualizar_progreso(sender, instance, **kwargs):
        if instance.completado and instance.juegoID.juegoID > instance.estudianteID.avanceJuegoID.juegoID :
            estudiante = instance.estudianteID
            juego = instance.juegoID
            estudiante.avanceJuegoID = juego # Actualiza el campo de progreso
            estudiante.save() # Guarda el modelo Estudiante actualizado

class Juego(models.Model):
    juegoID = models.AutoField(primary_key=True)
    mundo = models.IntegerField()
    nivel = models.IntegerField()

    def __str__(self):
        return f'Mundo {self.mundo} - Nivel {self.nivel}'

class Intentos(models.Model):
    intentoID = models.AutoField(primary_key=True)
    estudianteID = models.ForeignKey('Estudiante', on_delete=models.CASCADE)
    juegoID = models.ForeignKey('Juego', on_delete=models.CASCADE)
    fechaHora = models.DateTimeField(auto_now_add=True)
    tiempoJugado = models.FloatField()
    completado = models.BooleanField()

    def __str__(self):
        return f'Intento {self.intentoID} - Estudiante {self.estudianteID} - Juego {self.juegoID} - Completado: {self.completado}'


