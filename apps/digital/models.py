from django.db import models

# Create your models here.
class Organo(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    imagen = models.CharField(max_length = 50)

    def __str__(self):
        return "{} - {}".format(self.id, self.nombre)


class Parte(models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField()
    organo = models.ForeignKey(Organo)

    def __str__(self):
        return "{} - {}".format(self.id, self.nombre)
