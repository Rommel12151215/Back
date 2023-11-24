from django.db import models

class Reserva(models.Model):
      id = models.AutoField(primary_key=True)
      nombre = models.CharField(max_length=100)
      fecha = models.DateTimeField()
      numero_de_invitados = models.IntegerField()
