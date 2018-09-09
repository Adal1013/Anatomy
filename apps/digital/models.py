from django.db import models

# Create your models here.
class Organo(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 400)
    imagen = models.CharField(max_length = 50)

class Parte(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField(max_length = 400)
    organo = models.ForeignKey(Organo)
