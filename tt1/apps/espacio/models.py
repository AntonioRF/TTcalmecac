from django.db import models

# Create your models here.


class Espacio(models.Model):

	numero = models.IntegerField()
	nombre = models.CharField(max_length=50)
	capacidad = models.IntegerField()
	tipo = models.CharField(max_length=50)
	acceso_discapacitados = models.CharField(max_length=50)
	puede_utilizar = models.CharField(max_length=50)
	observaciones = models.TextField()
	